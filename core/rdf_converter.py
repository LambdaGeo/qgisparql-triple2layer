# -*- coding: utf-8 -*-
import uuid
import re
from rdflib import Namespace, Literal, URIRef, RDF, Graph

class RDFConverter:
    """Handles the conversion from QGIS layers to RDF graphs."""

    @staticmethod
    def is_valid_url(s):
        """Simple URL validation."""
        regex = re.compile(
            r'^(?:http|ftp)s?://' 
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, str(s)) is not None

    def features_to_triples(self, features, attr_mapping, id_attr=None, include_geometry=True):
        """
        Converts QGIS features to a dictionary of raw triple data.
        attr_mapping: Dict { 'qgis_attr': 'rdf_predicate_uri' }
        """
        data = {}
        for feature in features:
            try:
                # Sanitiza o subject_id
                raw_id = feature[id_attr] if id_attr and id_attr in feature.fields().names() else None
                subject_id = str(raw_id).replace(" ", "_") if raw_id is not None else str(uuid.uuid4())
                
                feature_data = {}
                if include_geometry and feature.hasGeometry():
                    # Default GeoSPARQL predicate
                    feature_data['http://www.opengis.net/ont/geosparql#asWKT'] = feature.geometry().asWkt()

                for q_attr, p_uri in attr_mapping.items():
                    if q_attr in feature.fields().names():
                        feature_data[p_uri] = feature[q_attr]
                
                data[subject_id] = feature_data
            except Exception as e:
                continue # Pula feições problemáticas
        return data

    def build_graph(self, triple_data, base_namespace_uri, rdf_type_uri=None, prefixes=None):
        """Builds an rdflib Graph from triple data."""
        g = Graph()
        # Garante que a URI base termina em / ou #
        if not base_namespace_uri.endswith(("/", "#")):
            base_namespace_uri += "/"
            
        base_ns = Namespace(base_namespace_uri)
        g.bind("base", base_ns)
        
        if prefixes:
            for p, uri in prefixes.items():
                g.bind(p, Namespace(uri))

        for subject_id, attributes in triple_data.items():
            # Constrói o sujeito com segurança
            subject = URIRef(f"{base_namespace_uri}{subject_id}")
            
            if rdf_type_uri:
                g.add((subject, RDF.type, URIRef(rdf_type_uri)))

            for predicate_uri, value in attributes.items():
                if not predicate_uri or not self.is_valid_url(predicate_uri):
                    continue # Predicado inválido
                    
                p = URIRef(predicate_uri)
                # Determine if object is URI or Literal
                if value is not None:
                    if self.is_valid_url(value):
                        o = URIRef(value)
                    else:
                        o = Literal(value)
                    g.add((subject, p, o))
        
        return g

    def serialize(self, graph, format="turtle"):
        """Serializes the graph to a string."""
        return graph.serialize(format=format)
