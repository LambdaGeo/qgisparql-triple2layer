---
title: 'QGISSPARQL: Bidirectional Integration between Linked Data and Geographic Information Systems'
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
    orcid: 0009-0000-2339-3191
  - name: Felipe Martins Sousa
    affiliation: "1"
    orcid: 0009-0009-0505-4845
  - name: José Magno Pinheiro Alves
    affiliation: "1"
    orcid: 0009-0003-7212-4870
  - name: Denilson da Silva Bezerra
    affiliation: "1"
    orcid: 0000-0002-9567-7828
affiliations:
  - name: Universidade Federal do Maranhão (UFMA), Brazil
    index: "1"
date: 2 March 2026
bibliography: paper.bib
---


## Summary

Geographic Information Systems (GIS) handle a vast amount of spatial data that can benefit from the Linked Data paradigm, which promotes interoperability and reuse across distributed repositories [@qgissparql_2023; @isotani2015]. However, integrating Resource Description Framework (RDF) data with traditional GIS tools remains challenging, often requiring custom scripts and technical expertise [@garcia2019; @nerval2023].

**QGISSPARQL** is an open-source QGIS plugin that enables **bidirectional integration between GIS and Linked Data**. It allows users to both: (i) execute SPARQL queries and import RDF data as native QGIS vector layers, and (ii) export geospatial layers into RDF triples compliant with Semantic Web standards such as GeoSPARQL [@perry2011] and the RDF Data Cube Vocabulary [@silva2023].

By combining these capabilities into a unified environment, QGISSPARQL provides an end-to-end workflow for consuming and publishing linked geographic data directly within QGIS, eliminating the need for intermediate transformations or programming.

## Statement of Need

Despite the increasing adoption of standards such as OGC GeoSPARQL [@perry2011] for representing spatial data on the Semantic Web, most GIS tools still lack native and user-friendly support for SPARQL-based workflows. Existing approaches are typically fragmented, requiring separate tools or manual steps for importing and exporting data.

Current workflows often involve exporting query results as tabular files (e.g., CSV), followed by manual conversion into geographic formats. Conversely, publishing GIS data as RDF frequently requires scripting and prior knowledge of Semantic Web technologies.

QGISSPARQL addresses these limitations by providing:

1. **Direct Integration:** Seamless connection between QGIS and RDF repositories (e.g., Virtuoso, Apache Jena Fuseki, and data.world) through SPARQL endpoints.
2. **Bidirectional Workflow:** Support for both importing RDF data into GIS and exporting GIS layers as RDF triples.
3. **User-Friendly Mapping:** Interactive interfaces for mapping SPARQL query variables to GIS attributes and associating GIS attributes with RDF vocabularies.

This unified approach reduces technical barriers and enables researchers to fully leverage Linked Open Data within spatial analysis workflows.

## State of the Field

Several efforts have attempted to bridge GIS and the Semantic Web. Tools such as GeoTriples [@geotriples] focus on generating RDF from geospatial data, while other approaches provide libraries or scripts for querying SPARQL endpoints. However, these solutions are typically unidirectional or require significant technical expertise.

Standard QGIS installations do not provide native support for SPARQL querying or RDF export. Existing plugins and tools often lack support for GeoSPARQL geometries or dynamic attribute mapping.

QGISSPARQL differs from these approaches by providing a **fully integrated, bidirectional workflow** within a single environment. It enables both the consumption and publication of Linked Data, eliminating the need for external tools or intermediate formats.

## Software Design

QGISSPARQL is implemented in Python and leverages PyQGIS and PyQt for integration with the QGIS environment. Its architecture is organized into modular components that separate user interface and core logic.

The plugin integrates two main functionalities:

### Importing RDF Data (Triple → Layer)

* Executes SPARQL queries against standard endpoints.
* Supports integration with platforms such as data.world.
* Maps query variables to GIS attributes.
* Converts Well-Known Text (WKT) geometries into native QGIS geometries.

### Exporting GIS Data (Layer → Triple)

* Converts vector layers (points, lines, polygons) into RDF triples.
* Supports Turtle serialization.
* Allows loading and use of RDF vocabularies (e.g., GeoSPARQL, SKOS, Data Cube).
* Provides strategies for URI generation (UUID or attribute-based).
* Maps GIS attributes to RDF properties.

### Architecture

* **Core Modules:** Handle SPARQL communication, RDF parsing, and data transformation.
* **UI Modules:** Provide interactive interfaces for configuration and mapping.
* **Data Mapping Layer:** Bridges GIS attributes and RDF vocabularies.

This modular design ensures extensibility and maintainability, allowing future enhancements such as direct publishing to triple stores or additional serialization formats.

## Research Impact Statement

QGISSPARQL enables researchers in Geosciences to interact seamlessly with Linked Open Data ecosystems without leaving their primary analytical environment. By supporting both data consumption and publication, it closes the loop between GIS and Semantic Web technologies.

The plugin has been successfully used within the DBCells project [@costa2017], supporting the publication and visualization of large-scale environmental datasets. More than 2.5 million RDF triples representing land use and environmental variables have been generated and integrated using this approach [@qgissparql_2023; @react2025].

By lowering the technical barrier to Linked Data adoption, QGISSPARQL contributes to reproducibility, interoperability, and data reuse in spatial analysis workflows.

## Acknowledgements

The authors acknowledge the support from the LambdaGeo Research Group at the Universidade Federal do Maranhão (UFMA). This study was made possible through financial support provided by scientific and technological initiation scholarships granted by CNPq and FAPEMA [@qgissparql_2023; @react2025].

## AI usage disclosure

This submission used generative AI tools to assist with structuring and refining the manuscript. All content was reviewed and validated by the authors.

## References
