import os
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QAction, QMenu
from qgis.PyQt.QtGui import QIcon

from .ui.dock_main import SparqlDockWidget

class QGISSparqlPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.dock_widget = None
        self.main_action = None
        self.import_action = None
        self.export_action = None

    def initGui(self):
        """Inicializa a interface e cria o menu QGISSPARQL."""
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        icon = QIcon(icon_path)
        
        # 1. Cria a Dock Widget IMEDIATAMENTE (escondida)
        if self.dock_widget is None:
            self.dock_widget = SparqlDockWidget(self.iface, self.iface.mainWindow())
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)
            self.dock_widget.visibilityChanged.connect(self.on_dock_visibility_changed)
            self.dock_widget.hide()

        # 2. Cria as Ações para o Menu

        self.import_action = QAction("Import (Triple → Layer)", self.iface.mainWindow())
        self.import_action.triggered.connect(self.show_import)

        self.export_action = QAction("Export (Layer → Triple)", self.iface.mainWindow())
        self.export_action.triggered.connect(self.show_export)

        # 3. Adiciona ao Menu Vetorial (criando um menu customizado)
        self.iface.addPluginToVectorMenu("QGISSPARQL", self.import_action)
        self.iface.addPluginToVectorMenu("QGISSPARQL", self.export_action)
        self.iface.addPluginToVectorMenu("QGISSPARQL", self.main_action)
        
        # Ícone na barra de ferramentas abre a dock geral
        self.iface.addToolBarIcon(self.main_action)

    def unload(self):
        self.iface.removePluginVectorMenu("QGISSPARQL", self.import_action)
        self.iface.removePluginVectorMenu("QGISSPARQL", self.export_action)
        self.iface.removePluginVectorMenu("QGISSPARQL", self.main_action)
        self.iface.removeToolBarIcon(self.main_action)
        
        if self.dock_widget:
            self.iface.removeDockWidget(self.dock_widget)
            self.dock_widget.deleteLater()

    def on_dock_visibility_changed(self, visible):
        if self.main_action:
            self.main_action.setChecked(visible)

    def show_import(self):
        if self.dock_widget:
            self.dock_widget.tabs.setCurrentIndex(0)
            self.dock_widget.show()
            self.dock_widget.raise_()

    def show_export(self):
        if self.dock_widget:
            self.dock_widget.tabs.setCurrentIndex(1)
            self.dock_widget.show()
            self.dock_widget.raise_()

    def toggle_dock(self):
        if self.dock_widget:
            is_visible = self.dock_widget.isVisible()
            self.dock_widget.setVisible(not is_visible)
            if not is_visible:
                self.dock_widget.raise_()

    def run(self):
        """O método run apenas chama o toggle se necessário."""
        self.toggle_dock()
