# Triple2Layer

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![QGIS](https://img.shields.io/badge/QGIS-3.0%2B-brightgreen)](https://qgis.org)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org)

A QGIS plugin to import geographic data from SPARQL endpoints and linked data repositories into QGIS vector layers.

Part of the **QGISParQL** suite — see also [Layer2Triple](https://github.com/LambdaGeo/qgisparql-layer2triple).

---

## Overview

**Triple2Layer** enables GIS users to query linked data sources — such as triple stores (Virtuoso, Apache Jena Fuseki) or [Data.world](https://data.world) — using SPARQL and load the results directly as geographic layers in QGIS.

The plugin bridges the Semantic Web and GIS workflows, allowing data encoded in RDF/WKT format to be visualized and analyzed in a familiar GIS environment.

## Features

- Query any SPARQL 1.1-compliant triple store endpoint
- Import data from [Data.world](https://data.world) datasets (requires API token)
- Load results as QGIS vector layers (points, lines, polygons in WKT format)
- Configure attribute names and types (String, Int, Double) before import
- Define the unique identifier for the resulting layer

## Requirements

- QGIS 3.0 or higher
- Python 3.x (tested on Python 3.10–3.12)
- Internet access to reach SPARQL endpoints
- Python packages: `SPARQLWrapper`, `datadotworld`, `pandas`, `setuptools`

## Installation

### From QGIS Plugin Repository (recommended)

1. Open QGIS and go to **Plugins → Manage and Install Plugins**
2. Search for `Triple2Layer`
3. Click **Install**

### Manual installation

1. Download or clone this repository
2. Copy the folder to your QGIS plugins directory:
   - **Linux:** `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Windows:** `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
3. Restart QGIS and enable the plugin under **Plugins → Manage and Install Plugins**

## Installing Python Dependencies

This plugin requires three external Python packages. Because QGIS uses its own Python environment, the installation steps differ slightly from a standard Python setup.

> **Note for Python 3.12 users:** Python 3.12 is strict about system-level package installation. Use the `--break-system-packages` flag as shown below, or use a virtual environment (`venv`) if you prefer isolation.

### Step 1 — Install Pandas and Setuptools

Install these first to ensure the environment has the modern build tools required by the other packages:

```bash
pip install pandas setuptools --break-system-packages
```

### Step 2 — Install the Data.world SDK

Install the base package without extras to avoid pulling in outdated Pandas versions:

```bash
pip install datadotworld --break-system-packages
```

### Step 3 — Install SPARQLWrapper

Required for communication with triple store endpoints:

```bash
pip install SPARQLWrapper --break-system-packages
```

### Step 4 — Configure Data.world credentials

If you plan to use Data.world as a data source, configure your API token:

```bash
dw configure
```

Paste your API token from your [Data.world settings](https://data.world/settings/advanced) when prompted. Alternatively, you can enter the token directly in the plugin's Settings menu inside QGIS.

> **Tip:** If `~/.dw/config` already exists (from a previous `dw configure` run), the plugin will use it automatically without prompting for the token again.

### requirements.txt

```
pandas
datadotworld
SPARQLWrapper
```

> Do not pin the `pandas` version in `requirements.txt`. Installing `pandas` before `datadotworld` ensures the correct version is used.

## Usage

1. In QGIS, go to **Vector → QGISParQL → Triple2Layer**
2. Enter a name for the output layer
3. Select the endpoint type: **Triple Store** or **Data.world**
4. Enter the endpoint URL (or Data.world dataset name)
5. Load a `.sparql` query file using **Open SPARQL**
6. Configure attributes in the table (name, type, geometry column, identifier)
7. Click **Import**

For a full walkthrough with screenshots, see the [documentation](docs/).

### Example SPARQL query

```sparql
PREFIX geo:  <http://www.opengis.net/ont/geosparql#>
PREFIX dbc:  <https://purl.org/linked-data/dbcells#>
PREFIX sdmx: <http://purl.org/linked-data/sdmx/2009/dimension#>

SELECT ?cell ?resolution ?wkt
WHERE {
  ?cell geo:asWKT ?wkt .
  ?cell dbc:resolution ?resolution .
  ?cell sdmx:refArea "AC" .
}
```

The geometry column (`?wkt`) must contain WKT-encoded geometries compatible with GeoSPARQL (`geo:asWKT`).

## Related Plugin

**[Layer2Triple](https://github.com/LambdaGeo/qgisparql-layer2triple)** — the companion plugin that exports QGIS layers back to RDF/triple stores.

## Authors

- **Sérgio Souza Costa** — [@profsergiocosta](https://github.com/profsergiocosta) — sergio.costa@ufma.br
- **Nerval Junior** — [@nervaljunior](https://github.com/nervaljunior)

Universidade Federal do Maranhão (UFMA) — LambdaGeo Research Group

## Citation

If you use this plugin in your research, please cite:

```bibtex
@software{costa2024triple2layer,
  author  = {Costa, Sérgio Souza and Junior, Nerval},
  title   = {Triple2Layer: A QGIS Plugin for Importing Linked Geographic Data},
  year    = {2024},
  url     = {https://github.com/LambdaGeo/qgisparql-triple2layer}
}
```

## License

This project is licensed under the **GNU General Public License v2.0** — see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an [issue](https://github.com/LambdaGeo/qgisparql-triple2layer/issues) or submit a pull request.