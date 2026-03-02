---
title: 'Triple2Layer: A QGIS Plugin for Importing Linked Geographic Data'
tags:
  - Python
  - QGIS
  - SPARQL
  - Semantic Web
  - Linked Data
  - GeoSPARQL
authors:
  - name: Sérgio Souza Costa
    orcid: 0000-0002-0232-4549
    affiliation: "1"
  - name: Nerval de Jesus Santos Junior
    affiliation: "1"
affiliations:
  - name: Universidade Federal do Maranhão (UFMA), Brazil
    index: "1"
date: 2 March 2026
bibliography: paper.bib
---

## Summary

Geographic Information Systems (GIS) handle a vast amount of data that can greatly benefit from the Linked Data paradigm, which connects data from various repositories to promote reuse and interoperability [@qgissparql_2023; @isotani2015]. However, researchers often face a bottleneck when trying to consume Resource Description Framework (RDF) data directly within traditional GIS software. Historically, retrieving spatial data from Semantic Web repositories required users to write complex custom scripts [@garcia2019]. 

`Triple2Layer` is an open-source QGIS plugin—part of the QGISSPARQL toolset—designed to bridge this gap. It allows users to execute SPARQL queries and import the results as native QGIS vector layers directly through a graphical interface, eliminating the need for programming skills. The plugin supports standard SPARQL 1.1 endpoints (Triple Stores) and the `data.world` platform, providing a streamlined workflow for visualizing and analyzing linked geographic data [@qgissparql_2023; @silva2023].

## Statement of Need

Despite the growth of standards like OGC-GeoSPARQL [@perry2011] for representing spatial data on the Semantic Web, most GIS tools still lack native and user-friendly support for direct SPARQL querying. Current workflows often require researchers to manually download tabular results and convert them into compatible geographic formats. 

`Triple2Layer` addresses these challenges by offering:
1. **Direct Integration:** Connecting QGIS directly to RDF repositories (e.g., Virtuoso, Apache Jena Fuseki) and the data.world portal via HTTP endpoints [@silva2023; @nerval2023].
2. **Dynamic Attribute Mapping:** Providing an interactive table where users can map SPARQL query variables to GIS attributes. Users can define which variable holds the geometry (using Well-Known Text - WKT format), specify the primary key/identifier, and cast attribute types (String, Integer, Double) before importing [@nerval2023; @silva2023].

This tool is particularly relevant for researchers working with Linked Open Data (LOD) in fields such as environmental monitoring and land use/land cover change models. For instance, `Triple2Layer` is currently being used within the DBCells project [@costa2017] to successfully load and map millions of geographic triples representing Brazilian biomes and land cover variables back into QGIS for spatial analysis [@qgissparql_2023].

## State of the field

While there are existing efforts to bridge GIS and the Semantic Web, many are either standalone libraries or require significant technical expertise. Standard QGIS does not provide a native SPARQL connector. Some experimental plugins have attempted basic RDF support, but often lack the ability to handle complex GeoSPARQL geometries or dynamic attribute casting. 

Compared to manual workflows (e.g., exporting CSVs from a Triple Store and re-importing them into QGIS), `Triple2Layer` automates the entire pipeline. It differs from tools like **GeoTriples**, which focuses on *generating* RDF from GIS data, by focusing on the *consumption* of RDF data, making it a critical tool for end-user spatial analysis of existing Linked Data repositories.

## Software Design

`Triple2Layer` is implemented in Python [@nerval2023] and leverages the following architecture:
- **Core Engine:** Utilizes the `SPARQLWrapper` library for standard endpoint communication and the `datadotworld` SDK for direct integration with the data.world ecosystem.
- **Geometry Parser:** Leverages the QGIS API to transform Well-Known Text (WKT) strings retrieved from SPARQL queries into native QGIS points, lines, or polygons.
- **UI Module:** Built using `PyQt` (QtDesigner), offering an intuitive configuration menu for attribute mapping and credential management [@qgissparql_2023].
- **Data Mapper:** A specialized component that allows the user to cast RDF datatypes to GIS field types (Integer, Double, String) during the import process to ensure data integrity.

## Research impact statement

`Triple2Layer` empowers researchers in the Geosciences to interact with the growing body of Linked Open Data without leaving their primary analytical tool. By lowering the technical barrier to accessing GeoSPARQL data, it facilitates the reuse of massive datasets like those hosted by the **LambdaGeo** group and other international repositories. This plugin has been essential for the DBCells project [@costa2017], enabling the visualization of large-scale environmental datasets that were previously locked in Triple Stores.

## Acknowledgements

The authors acknowledge the support from the LambdaGeo Research Group at the Universidade Federal do Maranhão (UFMA). This study was made possible through financial support provided by scientific and technological initiation scholarships granted by CNPq and FAPEMA [@qgissparql_2023; @react2025].

## AI usage disclosure

This submission used generative AI tools (Claude Sonnet 4.6 and NotebookLM) to assist with structuring documentation and synthesizing prior work. All outputs were reviewed and validated by the human authors.

## References