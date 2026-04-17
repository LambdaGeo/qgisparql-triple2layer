def classFactory(iface):
    from .plugin import QGISSparqlPlugin
    return QGISSparqlPlugin(iface)