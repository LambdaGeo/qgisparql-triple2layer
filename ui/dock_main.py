import traceback
import os
import re
import rdflib
from rdflib import Graph, Namespace

from qgis.PyQt.QtWidgets import (
    QDockWidget, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QFileDialog, QSizePolicy,
    QTableWidget, QTableWidgetItem, QHeaderView, QInputDialog
)
from qgis.PyQt.QtCore import Qt, QVariant, QSettings
from qgis.core import Qgis, QgsMessageLog, QgsProject, QgsTask, QgsApplication, QgsMapLayerProxyModel, QgsVectorLayer
from qgis.gui import QgsMapLayerComboBox

from ..core.sparql_client import SparqlClient
from ..core.layer_converter import LayerConverter
from ..core.rdf_converter import RDFConverter

class SparqlFetchTask(QgsTask):
    def __init__(self, client, source_type, source_val, query, geom_col, layer_name):
        super().__init__(f"Fetching from {source_val}", QgsTask.CanCancel)
        self.client = client
        self.source_type = source_type
        self.source_val = source_val
        self.query = query
        self.geom_col = geom_col
        self.layer_name = layer_name
        self.records = []
        self.error_msg = ""
        self.trace = ""

    def run(self):
        QgsMessageLog.logMessage(f"Task Thread Started: {self.source_val}", "QGISSparql", Qgis.Info)
        try:
            if self.source_type == "data.world":
                self.records = self.client.query_data_world(self.source_val, self.query)
                self.st_type = "DICT"
            else:
                self.records = self.client.query_endpoint(self.source_val, self.query)
                self.st_type = "SPARQL"
            return True
        except Exception as e:
            self.error_msg = str(e)
            self.trace = traceback.format_exc()
            return False

class SparqlExportTask(QgsTask):
    def __init__(self, converter, layer, file_path, base_namespace, attr_mapping, id_attr):
        super().__init__(f"Exporting {layer.name()}", QgsTask.CanCancel)
        self.converter = converter
        self.layer = layer
        self.file_path = file_path
        self.base_namespace = base_namespace
        self.attr_mapping = attr_mapping
        self.id_attr = id_attr
        self.success = False
        self.error_msg = ""

    def run(self):
        try:
            QgsMessageLog.logMessage(f"Export Thread Started for {self.file_path}", "QGISSparql", Qgis.Info)
            features = list(self.layer.getFeatures())
            triple_data = self.converter.features_to_triples(features, self.attr_mapping, self.id_attr)
            g = self.converter.build_graph(triple_data, self.base_namespace, prefixes={"geo": "http://www.opengis.net/ont/geosparql#"})
            rdf_str = self.converter.serialize(g, format="turtle")
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(rdf_str)
            self.success = True
            return True
        except Exception as e:
            self.error_msg = str(e)
            QgsMessageLog.logMessage(f"Export Thread Error: {str(e)}\n{traceback.format_exc()}", "QGISSparql", Qgis.Critical)
            return False

class SparqlDockWidget(QDockWidget):
    def __init__(self, iface, parent=None):
        super(SparqlDockWidget, self).__init__("QGISSparql Unified", parent)
        self.iface = iface
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.setObjectName("QGISSparqlUnifiedDock")

        self.sparql_client = SparqlClient()
        self.layer_converter = LayerConverter()
        self.rdf_converter = RDFConverter()
        self.vocab_properties = ["Select URI...", "http://purl.org/linked-data/cube#measureType", "http://purl.org/linked-data/cube#dataSet"]

        self.setup_ui()

    def setup_ui(self):
        self.main_container = QWidget()
        self.main_layout = QVBoxLayout(self.main_container)
        self.tabs = QTabWidget()
        self.tab_import = QWidget()
        self.tab_export = QWidget()
        self.setup_import_tab()
        self.setup_export_tab()
        self.tabs.addTab(self.tab_import, "Triple → Layer")
        self.tabs.addTab(self.tab_export, "Layer → Triple")
        self.main_layout.addWidget(self.tabs)
        self.setWidget(self.main_container)

    def setup_import_tab(self):
        layout = QVBoxLayout(self.tab_import)
        layout.addWidget(QLabel("Source Type:"))
        self.import_source_type = QComboBox()
        self.import_source_type.addItems(["SPARQL Endpoint", "data.world"])
        self.import_source_type.currentTextChanged.connect(self.on_source_type_changed)
        layout.addWidget(self.import_source_type)

        self.lbl_source = QLabel("SPARQL Endpoint URL:")
        layout.addWidget(self.lbl_source)
        self.import_source_url = QLineEdit("https://dbpedia.org/sparql")
        layout.addWidget(self.import_source_url)
        
        self.lbl_token = QLabel("data.world API Token:")
        self.import_token = QLineEdit()
        self.import_token.setEchoMode(QLineEdit.Password)
        settings = QSettings()
        self.import_token.setText(settings.value("qgissparql/dw_token", ""))
        layout.addWidget(self.lbl_token)
        layout.addWidget(self.import_token)
        self.lbl_token.hide()
        self.import_token.hide()

        self.import_query = QTextEdit()
        self.import_query.setPlainText("SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10")
        self.import_query.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.import_query)
        
        layout.addWidget(QLabel("Geometry Variable (if any):"))
        self.import_geom_col = QLineEdit("geom")
        layout.addWidget(self.import_geom_col)

        layout.addWidget(QLabel("Output Layer Name:"))
        self.import_layer_name = QLineEdit("SPARQL_Layer")
        layout.addWidget(self.import_layer_name)
        
        self.btn_import = QPushButton("Execute Import")
        self.btn_import.setStyleSheet("font-weight: bold; height: 30px;")
        self.btn_import.clicked.connect(self.execute_import)
        layout.addWidget(self.btn_import)
        layout.addStretch()

    def on_source_type_changed(self, source_type):
        if source_type == "data.world":
            self.lbl_source.setText("Dataset ID (owner/id):")
            self.lbl_token.show()
            self.import_token.show()
            self.import_source_url.setPlaceholderText("e.g. user/dataset")
            self.import_query.setPlainText("SELECT * FROM tables")
        else:
            self.lbl_source.setText("SPARQL Endpoint URL:")
            self.lbl_token.hide()
            self.import_token.hide()
            self.import_source_url.setPlaceholderText("")
            self.import_query.setPlainText("SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10")

    def execute_import(self):
        source_type = self.import_source_type.currentText()
        source_val = self.import_source_url.text().strip()
        query = self.import_query.toPlainText().strip()
        geom_col = self.import_geom_col.text().strip()
        layer_name = self.import_layer_name.text().strip()
        if not source_val or not query or not layer_name:
            self.iface.messageBar().pushMessage("Error", "Fill required fields.", level=Qgis.Warning)
            return
        self.btn_import.setEnabled(False)
        self.current_task = SparqlFetchTask(self.sparql_client, source_type, source_val, query, geom_col, layer_name)
        self.current_task.taskCompleted.connect(self.on_task_finished)
        self.current_task.taskTerminated.connect(self.on_task_failed)
        QgsApplication.taskManager().addTask(self.current_task)

    def on_task_finished(self):
        task = self.sender()
        self.btn_import.setEnabled(True)
        if not task.records:
            self.iface.messageBar().pushMessage("Warning", "No records found.", level=Qgis.Warning)
            return
        try:
            first_row = task.records[0]
            attr_mappings = []
            keys = first_row.keys() if isinstance(first_row, dict) else []
            for key in keys:
                if key != task.geom_col:
                    attr_mappings.append((key, QVariant.String, key))
            layer = self.layer_converter.create_memory_layer(layer_name=task.layer_name, records=task.records, geo_column=task.geom_col, attr_mappings=attr_mappings, source_type=task.st_type)
            if layer and layer.isValid():
                QgsProject.instance().addMapLayer(layer)
                self.iface.messageBar().pushMessage("Success", "Layer imported.", level=Qgis.Success)
        except Exception as e:
            QgsMessageLog.logMessage(f"Layer creation error: {str(e)}\n{traceback.format_exc()}", "QGISSparql", Qgis.Critical)

    def on_task_failed(self):
        self.btn_import.setEnabled(True)
        task = self.sender()
        self.iface.messageBar().pushMessage("Error", f"Fetch failed: {task.error_msg}", level=Qgis.Critical)

    def setup_export_tab(self):
        layout = QVBoxLayout(self.tab_export)
        layout.addWidget(QLabel("Select Vector Layer:"))
        self.export_layer_cb = QgsMapLayerComboBox()
        self.export_layer_cb.setFilters(QgsMapLayerProxyModel.VectorLayer)
        self.export_layer_cb.layerChanged.connect(self.on_export_layer_changed)
        layout.addWidget(self.export_layer_cb)
        
        layout.addWidget(QLabel("Base Namespace URI:"))
        self.export_namespace = QLineEdit("http://example.org/resource/")
        layout.addWidget(self.export_namespace)
        
        layout.addWidget(QLabel("Subject ID Attribute:"))
        self.export_id_attr = QComboBox()
        layout.addWidget(self.export_id_attr)

        layout.addWidget(QLabel("Common Vocabularies:"))
        self.common_vocabs = QComboBox()
        self.common_vocabs.addItem("Select common vocabulary...")
        self.common_vocabs_urls = {
            "DataCube (qb)": ("qb", "https://raw.githubusercontent.com/UKGovLD/publishing-statistical-data/master/specs/src/main/vocab/cube.ttl", "ttl"),
            "GeoSPARQL (geo)": ("geo", "https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl", "ttl"),
            "SKOS": ("skos", "http://www.w3.org/2004/02/skos/core#", "xml"),
            "FOAF": ("foaf", "http://xmlns.com/foaf/0.1/", "xml")
        }
        self.common_vocabs.addItems(self.common_vocabs_urls.keys())
        self.common_vocabs.currentTextChanged.connect(self.on_common_vocab_selected)
        layout.addWidget(self.common_vocabs)

        self.btn_load_vocab = QPushButton("Load External Vocabulary...")
        self.btn_load_vocab.clicked.connect(self.load_vocabulary_dialog)
        layout.addWidget(self.btn_load_vocab)

        layout.addWidget(QLabel("Attribute Mapping:"))
        self.export_mapping_table = QTableWidget(0, 3)
        self.export_mapping_table.setHorizontalHeaderLabels(["Field", "Type", "Predicate/URI"])
        self.export_mapping_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.export_mapping_table)
        
        self.btn_export = QPushButton("Export to RDF (Turtle)")
        self.btn_export.setStyleSheet("font-weight: bold; height: 30px;")
        self.btn_export.clicked.connect(self.execute_export)
        layout.addWidget(self.btn_export)
        
        self.on_export_layer_changed(self.export_layer_cb.currentLayer())

    def on_export_layer_changed(self, layer):
        self.export_id_attr.clear()
        self.export_id_attr.addItem("")
        self.export_mapping_table.setRowCount(0)
        if layer and isinstance(layer, QgsVectorLayer):
            fields = layer.fields()
            self.export_mapping_table.setRowCount(len(fields))
            for i, field in enumerate(fields):
                self.export_id_attr.addItem(field.name())
                self.export_mapping_table.setItem(i, 0, QTableWidgetItem(field.name()))
                combo_type = QComboBox()
                combo_type.addItems(["Auto", "Vocabulary", "None"])
                # Captura row=i no momento da definição
                combo_type.currentTextChanged.connect(lambda _, row=i: self.on_mapping_type_changed(row))
                self.export_mapping_table.setCellWidget(i, 1, combo_type)
                self.export_mapping_table.setCellWidget(i, 2, QLineEdit())

    def on_mapping_type_changed(self, row):
        combo_type = self.export_mapping_table.cellWidget(row, 1)
        if not combo_type: return
        map_type = combo_type.currentText()
        if map_type == "Vocabulary":
            combo_uri = QComboBox()
            combo_uri.setEditable(True)
            combo_uri.addItems(self.vocab_properties)
            self.export_mapping_table.setCellWidget(row, 2, combo_uri)
        elif map_type == "None":
            le = QLineEdit()
            le.setPlaceholderText("(not mapped)")
            le.setEnabled(False)
            self.export_mapping_table.setCellWidget(row, 2, le)
        else:
            self.export_mapping_table.setCellWidget(row, 2, QLineEdit())

    def on_common_vocab_selected(self, name):
        if name in self.common_vocabs_urls:
            prefix, url, fmt = self.common_vocabs_urls[name]
            self.load_vocabulary_from_url(prefix, url, fmt)

    def load_vocabulary_from_url(self, prefix, url, fmt):
        self.iface.messageBar().pushMessage("Info", f"Loading {prefix} vocabulary...", level=Qgis.Info, duration=3)
        try:
            g = Graph()
            g.parse(url, format=fmt)
            self.extract_vocabulary_concepts(g, prefix)
            self.iface.messageBar().pushMessage("Success", f"Loaded {prefix} vocabulary.", level=Qgis.Success)
        except Exception as e:
            self.iface.messageBar().pushMessage("Error", f"Could not load {prefix}: {e}", level=Qgis.Critical)

    def extract_vocabulary_concepts(self, g, prefix):
        q = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX qb: <http://purl.org/linked-data/cube#>
            SELECT DISTINCT ?p WHERE {
                { ?p rdf:type owl:DatatypeProperty } UNION
                { ?p rdf:type owl:ObjectProperty } UNION
                { ?p rdf:type rdf:Property } UNION
                { ?p rdf:type rdfs:Property } UNION
                { ?p rdf:type qb:MeasureProperty } UNION
                { ?p rdf:type qb:AttributeProperty } UNION
                { ?p rdf:type qb:DimensionProperty }
            } ORDER BY ?p
        """
        for r in g.query(q):
            uri = str(r["p"])
            if uri not in self.vocab_properties:
                self.vocab_properties.append(uri)
        
        for row in range(self.export_mapping_table.rowCount()):
            widget = self.export_mapping_table.cellWidget(row, 2)
            if isinstance(widget, QComboBox):
                current = widget.currentText()
                widget.clear()
                widget.addItems(self.vocab_properties)
                if current in self.vocab_properties: widget.setCurrentText(current)

    def load_vocabulary_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Vocabulary", "", "RDF Files (*.ttl *.owl *.rdf *.xml)")
        if not file_path: return
        prefix, ok = QInputDialog.getText(self, "Vocabulary Prefix", "Enter prefix:")
        if not ok or not prefix: return
        try:
            g = Graph()
            g.parse(file_path, format='turtle' if file_path.endswith('.ttl') else 'xml')
            self.extract_vocabulary_concepts(g, prefix)
            self.iface.messageBar().pushMessage("Success", "Loaded vocabulary from file.", level=Qgis.Success)
        except Exception as e:
            self.iface.messageBar().pushMessage("Error", f"Failed to load: {e}", level=Qgis.Critical)

    def execute_export(self):
        layer = self.export_layer_cb.currentLayer()
        base_namespace = self.export_namespace.text().strip()
        id_attr = self.export_id_attr.currentText()
        if not layer or not base_namespace:
            self.iface.messageBar().pushMessage("Error", "Check inputs.", level=Qgis.Warning)
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Turtle", "", "Turtle Files (*.ttl)")
        if not file_path: return
        attr_mapping = {}
        for row in range(self.export_mapping_table.rowCount()):
            field_name = self.export_mapping_table.item(row, 0).text()
            map_type = self.export_mapping_table.cellWidget(row, 1).currentText()
            if map_type == "None":
                continue
            widget_val = self.export_mapping_table.cellWidget(row, 2)
            map_val = widget_val.currentText().strip() if isinstance(widget_val, QComboBox) else widget_val.text().strip()
            if map_type == "Auto":
                attr_mapping[field_name] = f"{base_namespace}{field_name}"
            else:
                attr_mapping[field_name] = map_val if map_val else f"{base_namespace}{field_name}"
        self.btn_export.setEnabled(False)
        self.current_export_task = SparqlExportTask(self.rdf_converter, layer, file_path, base_namespace, attr_mapping, id_attr)
        self.current_export_task.taskCompleted.connect(self.on_export_task_finished)
        self.current_export_task.taskTerminated.connect(self.on_export_task_failed)
        QgsApplication.taskManager().addTask(self.current_export_task)

    def on_export_task_finished(self):
        self.btn_export.setEnabled(True)
        task = self.sender()
        self.iface.messageBar().pushMessage("Success", f"RDF saved: {task.file_path}", level=Qgis.Success)

    def on_export_task_failed(self):
        self.btn_export.setEnabled(True)
        task = self.sender()
        self.iface.messageBar().pushMessage("Error", f"Export failed: {task.error_msg}", level=Qgis.Critical)
