# -*- coding: utf-8 -*-
from qgis.core import (
    QgsVectorLayer, QgsField, QgsGeometry, 
    QgsFeature, QgsProject, Qgis, QgsMessageLog
)
from qgis.PyQt.QtCore import QVariant

class LayerConverter:
    """Handles the conversion from triple/record data to QGIS layers."""

    @staticmethod
    def get_value(row, key, source_type):
        """Extracts a value from a record based on source type (SPARQL/DICT)."""
        if source_type == "SPARQL":
            val = row.get(key, {})
            return val.get("value", "") if isinstance(val, dict) else str(val)
        return str(row.get(key, ""))

    def create_memory_layer(self, layer_name, records, geo_column, attr_mappings, crs_id="EPSG:4326", source_type="SPARQL"):
        if not records:
            return None

        # 1. Detect Geometry Type
        geom_type_str = None
        for row in records:
            wkt = self.get_value(row, geo_column, source_type)
            if wkt:
                temp_geom = QgsGeometry.fromWkt(wkt)
                if not temp_geom.isNull():
                    type_map = {
                        Qgis.GeometryType.Point: "Point",
                        Qgis.GeometryType.Line: "LineString",
                        Qgis.GeometryType.Polygon: "Polygon"
                    }
                    geom_type_str = type_map.get(temp_geom.type(), "Unknown")
                    break

        if not geom_type_str:
            raise Exception(f"Could not detect geometry in column '{geo_column}'. Check if WKT is valid.")

        # 2. Construct URI and create layer
        uri = f"{geom_type_str}?crs={crs_id}"
        layer = QgsVectorLayer(uri, layer_name, "memory")
        if not layer.isValid():
            return None
            
        pr = layer.dataProvider()
        fields = [QgsField(name, vtype) for name, vtype, _ in attr_mappings]
        pr.addAttributes(fields)
        layer.updateFields()

        # 3. Populate Features
        features = []
        for row in records:
            fet = QgsFeature(layer.fields())
            wkt = self.get_value(row, geo_column, source_type)
            if wkt:
                fet.setGeometry(QgsGeometry.fromWkt(wkt))
            
            attrs = [self.get_value(row, col, source_type) for _, _, col in attr_mappings]
            fet.setAttributes(attrs)
            features.append(fet)

        pr.addFeatures(features)
        layer.updateExtents()
        return layer
