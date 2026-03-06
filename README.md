

# Triple2Layer

Status badge code:
 [![status](https://joss.theoj.org/papers/6a9a1eff32b69c18a8a6d42e76bd60c8/status.svg)](https://joss.theoj.org/papers/6a9a1eff32b69c18a8a6d42e76bd60c8)
Author instructions

A QGIS plugin to import geographic data from SPARQL endpoints and linked data repositories into QGIS vector layers.

Part of the **QGISParQL** suite — see also [Layer2Triple](https://github.com/LambdaGeo/qgisparql-layer2triple).

---

## Overview

**Triple2Layer** enables GIS users to query linked data sources — such as triple stores (Virtuoso, Apache Jena Fuseki) or [Data.world](https://data.world) — using SPARQL and load the results directly as geographic layers in QGIS.

The plugin bridges the Semantic Web and GIS workflows, allowing data encoded in RDF/WKT format to be visualized and analyzed in a familiar GIS environment.

## Features

* Query any SPARQL 1.1-compliant triple store endpoint.
* Import data from [Data.world](https://data.world) datasets (requires API token).
* **Asynchronous Task Management:** Imports run in the background without freezing the QGIS interface.
* **Auto-Geometry Detection:** Automatically identifies point, line, or polygon layers from WKT strings.
* **Dynamic Attribute Mapping:** Configure names and types (String, Int, Double) before import.

## Installation

### 1. Plugin Installation

Download or clone this repository and copy the folder to your QGIS plugins directory:

* **Linux:** `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
* **Windows:** `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`

*Note: Restart QGIS and enable the plugin under **Plugins → Manage and Install Plugins**.*

### 2. Python Dependencies (Crucial)

Because QGIS uses its own Python environment, dependencies must be installed correctly to avoid **version conflicts** (especially with `pandas` in Python 3.12+).

#### **On Linux (Ubuntu/Debian/Fedora)**

Open your terminal and run the commands in this **exact order**:

```bash
# 1. Install core build tools and pandas first
pip install pandas setuptools --break-system-packages

# 2. Install data.world and SPARQLWrapper
pip install datadotworld SPARQLWrapper --break-system-packages

```

#### **On Windows**

1. Search for **OSGeo4W Shell** in your Start Menu and run it as **Administrator**.
2. Run the following command:

```bash
pip install pandas setuptools datadotworld SPARQLWrapper

```

---

## 🔑 Authentication (data.world)

If you plan to use Data.world, you need an API Token. Triple2Layer provides three ways to handle this:

1. **In-Plugin:** Go to the plugin's Settings menu and enter your token. It will be saved securely in QGIS persistent settings.
2. **Environment Variable:** Set `DW_AUTH_TOKEN` in your system.
3. **CLI Config:** If you have run `dw configure` in your terminal, the plugin will automatically detect the token in `~/.dw/config`.

---

## Usage

1. Go to **Vector → QGISParQL → Triple2Layer**.
2. **Layer Name:** Enter a name for the output layer.
3. **Source:** Select **Triple Store** or **Data.world**.
4. **Endpoint:** Enter the URL or Dataset path (e.g., `user/dataset-name`).
5. **SPARQL:** Load a `.sparql` file. The plugin will parse the variables automatically.
6. **Attributes:** Map your SPARQL variables to QGIS fields and select the **Geometry Column** (must be WKT).
7. **Import:** Click to start the background task. Follow progress in the status bar.

---

## Authors

* **Sérgio Souza Costa** — [@profsergiocosta](https://github.com/profsergiocosta) — sergio.costa@ufma.br
* **Nerval Junior** — [@nervaljunior](https://github.com/nervaljunior)

**LambdaGeo Research Group** — Universidade Federal do Maranhão (UFMA).

## Citation

If you use this plugin in your research, please cite it as:

```bibtex
@software{costa2026triple2layer,
  author  = {Costa, Sérgio Souza and Junior, Nerval},
  title   = {Triple2Layer: A QGIS Plugin for Importing Linked Geographic Data},
  year    = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  url     = {https://github.com/LambdaGeo/qgisparql-triple2layer}
}

```
