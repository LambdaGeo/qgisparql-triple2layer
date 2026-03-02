# Contributing to QGISSPARQL: Triple2Layer

First of all, thank you for taking the time to contribute! 🎉

**Triple2Layer** is an open-source plugin for QGIS that aims to import data from linked data repositories (such as triple stores and Data.world) through SPARQL queries, converting them into geographic vector layers. 

Below are the guidelines for contributing to this project.

## 🐛 Reporting Bugs and Requesting Features

If you find a bug or have an idea for a new feature, please use the **Issues** tab of our GitHub repository:
[https://github.com/LambdaGeo/qgisparql-triple2layer/issues](https://github.com/LambdaGeo/qgisparql-triple2layer/issues)

When reporting a bug, please include:
* The QGIS version you are using (requires QGIS 3.4 or higher).
* Your operating system (Windows, Linux, etc.).
* Detailed steps to reproduce the issue.
* The SPARQL query and endpoint (Triple Store URL or Data.world dataset) that generated the error (if applicable).

## 💻 Setting up the Development Environment and Dependencies

The plugin was developed using the **Python** programming language. To contribute to the code and test locally, you will need to set up your environment.

### 1. System Requirements
* **QGIS**: Install QGIS (preferably via OSGeo4W if you are on Windows, or via your package manager on Linux).
* **Graphical User Interface (GUI)**: The interfaces (`.ui` files) were built using **QtDesigner** with the PyQt library. To change the plugin's visual interface, open the `.ui` files in QtDesigner, make your changes, and recompile them to Python.

### 2. Installing Libraries (Linux Terminal / Python 3.12+)
Since Python 3.12+ is strict about system packages (PEP 668), we recommend using the `--break-system-packages` flag if you are not using a virtual environment (`venv`). Follow the order below to avoid dependency conflicts:

**A. Install core dependencies:**
Install **Pandas** and **Setuptools** separately to ensure the environment has modern tools:
```bash
pip install pandas setuptools --break-system-packages
```

**B. Install the data.world SDK:**
Install the base package **without extras** to prevent the installer from attempting to download obsolete versions of Pandas:
```bash
pip install datadotworld --break-system-packages
```

**C. Install SPARQLWrapper:**
Essential for communication with *Triple Stores* via SPARQL queries:
```bash
pip install SPARQLWrapper --break-system-packages
```

**D. Configure data.world Credentials:**
Now that the `dw` command is available (and in your PATH), configure your access token:
```bash
dw configure
```
*(Paste your data.world API Token when prompted in the terminal)*

## 🔀 Contribution Flow (Pull Requests)

Follow the steps below to submit your changes:

1. **Fork** the repository [https://github.com/LambdaGeo/qgisparql-triple2layer/](https://github.com/LambdaGeo/qgisparql-triple2layer/).
2. Clone the repository locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/qgisparql-triple2layer.git
   ```
3. Create a branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-new-feature
   ```
4. Commit your changes with clear and descriptive messages.
5. Push to your branch:
   ```bash
   git push origin feature/my-new-feature
   ```
6. Open a **Pull Request (PR)** in the original repository describing in detail what was changed.

## 🧑‍💻 Code Guidelines

* Follow the PEP 8 style guide for Python scripts.
* Keep the code modular and well-commented, especially regarding integrations with SPARQL queries and calls to the QGIS API.
* If you add new files to the project (such as standard vocabularies or translation files in the `i18n` folder), remember to update the `Makefile` and the `resources.qrc` / `resources_rc.py` files accordingly.

## 📜 License

By contributing to this repository, you agree that your contributions will be licensed under the same **MIT License** that covers the project.
```