# -*- coding: utf-8 -*-
import json
import os
from SPARQLWrapper import SPARQLWrapper, JSON
import datadotworld as dw

class SparqlClient:
    """Handles connections to SPARQL endpoints and other RDF data sources."""

    def __init__(self):
        self.token = None

    def set_token(self, token):
        self.token = token

    def query_endpoint(self, endpoint_url, query):
        """Executes a SPARQL query with a 30-second timeout."""
        sparql = SPARQLWrapper(endpoint_url)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        # Define timeout para evitar travamento da thread
        sparql.setTimeout(30) 
        
        try:
            results = sparql.query().convert()
            if "results" in results and "bindings" in results["results"]:
                return results["results"]["bindings"]
            else:
                # Caso o endpoint retorne um JSON válido mas fora do padrão SPARQL
                return []
        except Exception as e:
            raise Exception(f"SPARQL Error: {str(e)}")

    def query_data_world(self, dataset_id, query):
        if not self.token:
            raise Exception("data.world token not set.")
        try:
            import datadotworld as dw
            os.environ['DW_AUTH_TOKEN'] = self.token
            
            # Detecta se a query é SPARQL (contém PREFIX ou SELECT com variáveis ?s)
            is_sparql = "PREFIX" in query.upper() or "?" in query
            q_type = 'sparql' if is_sparql else 'sql'
            
            results = dw.query(dataset_id, query, query_type=q_type)
            return results.dataframe.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"data.world Error: {str(e)}")

    def load_local_file(self, file_path):
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"File Error: {str(e)}")
