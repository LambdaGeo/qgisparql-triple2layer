# QGISSPARQL:Triple2Layer

# Overview

**Repository**: [https://github.com/LambdaGeo/qgisparql-triple2layer/](https://github.com/LambdaGeo/qgisparql-triple2layer/)

**Creators**: [Sérgio Souza Costa](https://github.com/profsergiocosta) and [Nerval Junior](https://github.com/nervaljunior)

### Purpose
This plugin aims to import data from a connected database and convert it into a geographic data layer in the QGIS geographic information system (GIS) (https://qgis.org/).

<table align="right">
  <tr>
    <td height="43px">
      <b>
        <a href="README-pt.md">Português 🇧🇷</a>
      </b>
    </td>
  </tr>
  <tr>
    <td height="43px">
      <a href="README.md">English 🇺🇸</a>
    </td>
  </tr>
</table>

# Triple2Layer
## An application for importing geographic data

![](https://img.shields.io/badge/Language-Python-blue)![](https://img.shields.io/badge/Compiler-QGIS-brightgreen) ![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) ![](https://img.shields.io/badge/Environment-Windows-red) ![](https://img.shields.io/badge/Environment-Linux-purple) ![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---

## How to Use

> `💡 The screenshots for this documentation were taken in QGIS 3.26.3 running on Windows. Depending on your setup, the screens you encounter might look a bit different. However, all the same buttons will still be available, and the instructions will work on any operating system. You will need QGIS 3.4 (the latest version at the time of writing) to use this plugin.`

> `💡 Before starting this exercise, the **Triple2Layer** plugin must be installed on your computer.`


Let's start right away!

To use **Triple2Layer**, simply open **QGIS** from the menu bar and hover the mouse over the vector through which you will be able to see the tools allowing you to manipulate vector layers. This way, it will be possible to access the plugins of **DBCells** in the QGISPARQL cell.

In Figure 1 below, we can see the **area of active plugins indicated** with arrow number 3. Going to vector in the menu bar as shown in arrow number 1, we can then open the **Triple2Layer** plugin and select the desired plugin, in this case, **Triple2Layer** shown in arrow number 2.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/bac31c85-387e-49ac-aefb-9795fa5e5b3c" alt="Figura 1: Menu de ferramentas">
  <p> Figura 1: Menu de ferramentas </p>
</div>


Next, you can see in Figure 2 the initial interface of the "**Triple2Layer**" plugin.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/3984ccb8-02cd-457e-9369-02f25f823dd7" alt="Figura 2: Interface do plugin Triple2layer">
  <p>Figura 2: Interface do plugin Triple2layer </p>
</div>


In the main graphical interface of the **Triple2Layer** plugin, you can see in Figure 3 the first and second parts. The first part contains information about the loaded file and the type of endpoint. In the second part, there is a table where the attributes necessary for the import will be loaded. In this interface, you will also find the "Import" button, which performs the import of the layer to the server. Next to it, there is the "Cancel" button, which is used to cancel the entire execution and close the graphical interface.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/bf8f5123-2b3b-43cb-b2a5-d514a90888dc" alt="Figura 3: Subdivisão do plugin Triple2layer">
  <p>Figura 3: Subdivisão do plugin Triple2layer </p>
</div>


# Importing Data

## Step 1: Defining the Geographic Layer Name

This plugin aims to import connected data from a repository and convert it into a geographic data layer within the QGIS geographic information system ([https://qgis.org/](https://qgis.org/)).

With the plugin open, the first step is to enter the name that the layer (geographic layer) will have when created, as shown in Figure 4. In this example, the layer name was set to "ACRE" since we will import data about this state.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/435bf5f4-53b0-4911-b55d-ad74a0348704" alt="Figura 4: Nome do Layer">
  <p> Figura 4: Nome do Layer </p>
</div>


## Step 2: Defining the Source of Connected Data

The current version of the plugin allows importing data from two connected data sources:

- Connected database servers, known as a triple store, regardless of implementation (e.g., Virtuoso or Apache Jena ***Fuseki).***
- A data portal called [data.world](http://data.world) ([https://docs.data.world/](https://docs.data.world/i)).

These data portals have a collection of triples representing connected data, where each object can be related to other objects via predicates.

For the creation of a geographic layer, it is necessary for this data to have a geometric attribute, such as the `geo:asWKT` predicate in Code 1:

```cpp
@prefix cells: <https://purl.org/linked-data/dbcells#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix sdmx: <http://purl.org/linked-data/sdmx/2009/dimension#> .

<https://purl.org/dbcells/epsg4326#R0_0830Cx-34_7917Cy-6_9714> a cells:Cell ;
    cells:resolution 8.3e-02 ;
    geo:asWKT "Polygon ((-34.8333349000000041 -6.92973086900001611, -34.750001570000002 -6.92973086900001611, -34.750001570000002 -7.01306419900001643, -34.8333349000000041 -7.01306419900001643, -34.8333349000000041 -6.92973086900001611))" .
    sdmx:refArea "PB" .
```

## Connected Data Paradigm

In the connected data paradigm (see more at: [https://ceweb.br/livros/dados-abertos-conectados/](https://ceweb.br/livros/dados-abertos-conectados//)), each resource has a URI. In this example, we have the following URI representing a resource:

```cpp
<https://purl.org/dbcells/epsg4326#R0_0830Cx-34_7917Cy-6_9714>
```

This resource is connected to other information through three predicates. In this example, the resource represents a polygon that has spatial resolution (area of the polygon), its geometric shape in WKT format, and additional information indicating in which Brazilian state this polygon is located.

<aside>
💡 In a simplified manner, a connected database, such as [Data.World](http://Data.World) or a triple store server, can be understood as a collection of triples, as described in Code 1.

</aside>

We can then select the type of endpoint, either "Triple Store Endpoint" or "Data.world Dataset," as shown in Figure 5 by arrow numbers 1 and 2.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/6f64e68c-f424-4c67-9570-bd0691c3c57b" alt="Figura 5: Tipo de Endpoint">
  <p>Figure 5: Endpoint Type</p>
</div>

For the Triple Store, we will enter the server's URL, as shown in Figure 6.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/26d6e447-6338-4993-87d3-0ad2d1f97401" alt="Figura 6: Selecionando endpoint para Triple Store">
  <p>Figure 6: Selecting endpoint for Triple Store</p>
</div>

For Data.World, we will use the Dataset name, as shown in Figure 7.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/92d9f105-995e-4ba7-842b-bb287a45163c" alt="Figura 7: Selecionando endpoint para Data world">

  <p>Figure 7: Selecting endpoint for Data.world</p>
</div>

Additionally, in the case of Data.World, for importing, it is necessary to define an access token. The token can be found in the settings on the Data.World portal, as shown in Figure 8.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/dc1897a5-628e-44e1-9f10-583b42bcb9f0" alt="Figura 8: API Token">

  <p>Figure 8: API Token</p>
</div>

In "Settings" in the top left corner, we can select the "Data.world Token" option, as shown in Figure 9.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/8abebdf4-7a0c-4bf1-86b2-ffaad6822157" alt="Figura 9: Token Data world">
  
  <p>Figure 9: Data.world Token</p>
</div>

After the text box is selected, with the token used for read and write copied previously, we can paste it into the labeled number 1 and then click "ok" on the arrow 2 as shown in figure 10 below.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/ec71c8d9-27d0-494d-94ce-43cda02e12a4" alt="Figura 10: Token do Dataset">
  <p>Figure 10: Dataset Token</p>
</div>


## Step 3: Opening a file with a SPARQL query

A connected data source has thousands or millions of triples. So, they support a query language called SPARQL ([https://www.w3.org/TR/sparql11-query](https://www.w3.org/TR/sparql11-query/)). This language allows defining which triples we want to load from pattern matches. This set of triple patterns can have some variables that will be replaced to perform a certain match. Considering the database described in Code 1, we could use the following SPARQL query to bring the resolution and geometries of a given object.


```cpp
prefix geo: <http://www.opengis.net/ont/geosparql#>
prefix sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>
prefix dbc: <https://purl.org/linked-data/dbcells#>

SELECT ?cell ?resolution ?wkt 
WHERE {
  ?cell geo:asWKT ?wkt.
  ?cell dbc:resolution ?resolution.
  ?cell sdmx-dimension:refArea "AC".
}
```

<p>Notice that by the pattern:</p>

```cpp
?cell sdmx-dimension:refArea "AC".

```

In a connected data repository, this query will result in only the information for this Brazilian state, in this case, Acre. When processing this query on a connected database, the result could be displayed in a table format with three columns, represented by the variables that appear in the `select` clause:


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/4d0d7fbf-7253-4ead-9ea4-33404491ae7b" alt="Tabela 1: Tabela da consulta SPARQL">
  <p> Table 1: SPARQL Query Result Table </p>
</div>

Next, we'll see that the plugin will need some information from the user to transform a data table, like the one described in Table 1, into a geographic layer.

We can load a SPARQL file by opening the dialog, clicking on "Open SPARQL" as shown in Figure 11.

<aside>
💡 For this example, consider a SPARQL file like the one described in Code 2
</aside>


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/b6b6040d-e316-4de8-bb64-e6c280706519" alt="Figura 11: Botão de carregamento do SPARQL  file">
  <p> Figure 11: SPARQL File Loading Button </p>
</div>

By clicking on the button, a dialog will open in the computer's file explorer, where we can select the file needed for the query, as shown in Figure 12. We can then choose a file as shown in arrow number 1 by clicking open to load the data.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/716aa8b5-4b43-4e83-b970-7c3e9238b980" alt="Figura 12: Seleção do SPARQL  file">
  <p> Figure 12: Selecting the SPARQL File </p>
</div>

Next, we will see how the attributes will be defined for the creation of the geographic layer in QGIS.

## Step 4: Attribute Definition

With the loaded file, the attribute table will appear as shown in Figure 13.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/4d9597d3-f466-4494-84bd-25edcffc7773" alt="Figura 13: Carregamento da tabela após seleção do arquivo">
  <p> Figure 13: Table Loading after File Selection </p>
</div>

In this table (2) in Figure 13, some information necessary for the creation of the geographic layer from the result of the SPARQL query will be defined. For example, we can define which attribute will be the identifier and which one will be used to represent the geometry. We can define the name of the attribute, which may be different from the name of the variable in the SPARQL file. In addition to defining the data type of the attribute and which ones will be imported.

### Selecting the attribute that has the geometry

Firstly, in the attribute selection of Figure 14, the choice representing the geometry is made. So far, the representation supported by the plugin is WKT (Well Know Text), and it can have geometries defined with points, lines, and polygons. By selecting the geometry as a WKT variable, shown in Figure 14, we will observe that the options "Attribute name" and "Attribute type" are disabled.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/413f8b89-34ef-4f8d-9fb7-2c51b428132d" alt="Figura 14: Seleção do tipo de geometria">
  <p> Figure 14: Geometry Type Selection </p>
</div>

### Selecting the attributes to be imported

Not all attributes that come from the query need to be imported. The user will mark the attributes that he wants to be imported into the geographic layer.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/ebb391b2-0dc5-48dd-8056-734660ac0bc5" alt="Figura 15: Seleção de atributos para importação">
  <p> Figure 15: Attribute Selection for Import </p>
</div>

### Defining the name and type of attributes

In the attribute selection, it is possible to change the name of the attribute and its data type. To change the name of the attribute, simply double-click on the selected attribute and type the new name.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/0d0dd35f-1bad-444f-9157-e8968bf17bb7" alt="Figura 16: Attribute name">
<p> Figure 16: Attribute name </p>
</div>

Regarding data types, by default, they will be imported as `String`, which represents text. However, we can change it to `Int`, which represents an integer, or `Double`, which represents a real number. In this example, the resolution is a numerical data with decimal places, representing the resolution of the cell, which is better represented as a `Double`.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/e37fdfe7-51ce-427c-a929-1ecddd511279" alt="Figura 17: Attribute type">
<p> Figure 17: Attribute type </p>
</div>

### Selecting which attribute will be the identifier of the geographic layer

A geographic layer, like a table in a database, requires that each record (or row) has an identifier (known as the primary key). In some cases, this information will come as a result of querying the repository, so you can indicate which of the attributes represents this identifier. An important criterion is that the values of this attribute must be unique; repetitions are not allowed. If not selected, an ID will be defined as auto-increment, i.e., integer values from 1 to the number of objects.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/c6125966-a5f5-4e6e-921d-84fea1a8b0aa" alt="Figura 18: Identificador único">
<p> Figure 18: Unique identifier </p>
</div>

## Step 5: Executing the import

Finally, we can import the data according to Figure 19 by clicking on "importar."


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/1bd2f77d-90e1-48b1-809b-0494f1c6e95d" alt="Figura 19: Import layer">
<p> Figure 19: Import layer </p>
</div>

By clicking, we will first see the message that the layer is being imported and soon after it is loaded.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/0f63542b-2456-4c6a-9e70-6b55fda1d1f4" alt="Figura 20: Carregamento do Layer">
<p> Figure 20: Layer loading </p>
</div>

Next is the image of the 100% loaded Layer.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/9c512014-cc54-40a4-8a4a-add54a0132ca" alt="Figura 21: Layer carregado">
<p> Figure 21: Loaded Layer </p>
</div>

Upon loading the layer, we can select the loaded layer as shown by the arrow and number 1 in Figure 22.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/0324a30c-250d-4ba6-a2c9-9a136bd1a491" alt="Figura 22: abrindo tabela de atributos do QGIS">
<p> Figure 22: Opening QGIS Attribute Table </p>
</div>

By pressing the F6 key, we can open the attribute table of the selected layer, as shown in Figure 23.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/e511f8cf-f9cd-49c6-9a07-2f226e902eb0" alt="Figura 23: tabela de atributos do QGIS">
  <p> Figura 23: tabela de atributos do QGIS </p>
</div>
