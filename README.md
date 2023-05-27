# Triple2Layer

### Este plugin visa importar os dados de base de dados conectado e convertê-lo para uma camada de dado geográfico no sistema de informação geográfica QGIS (https://qgis.org/).


# autor: Sérgio Souza Costa
profsergiocosta

## contribuidor: Nerval Junior
nervaljunior

# Triple2Layer
## An application for importing geographic data

![](https://img.shields.io/badge/Language-Python-blue)![](https://img.shields.io/badge/Compiler-QGIS-brightgreen) ![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) ![](https://img.shields.io/badge/Environment-Windows-red) ![](https://img.shields.io/badge/Environment-Linux-purple) ![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---
<div class="interface">
A seguir é possivel ver na figura 4 a interface inicial do plugin “**Triple2Layer**”.

![Figura 4: Interface do plugin Triple2layer](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3636411f-1988-443b-908c-a13e858cc92d/Untitled.png)

Figura 4: Interface do plugin Triple2layer
<div/>

## caracteristicas:

Atualmente o plugin é compatível com servidores de banco de dados conectados, denominados em inglês como triple store, independentemente de implementação (ex. Virtuoso e Apache Jena ***Fuseki)***.  Além destes servidores, a atual versão é capaz de carregar dados do portal de dados denominado de [data.world](http://data.world) ([https://docs.data.world/](https://docs.data.world/i)).

Esses portais de dados, possuem uma coleção de triplas que representam dados conectados. Onde cada objeto pode estar relacionado a outros objetos via predicados. Considere os seguintes predicados: 

- `cells:resolution`, poderia ser uado para indicar a resolução espacial de um objeto que é representada por um valor numérico
- `sdmx:refArea` poderia ser usado para trazer alguma informação sobre a localização espacial de um dado objeto. Como o nome ou sigla de um país ou estado.
- `geo:asWkt` pode ser usado para relacionar um objeto com sua representação geometicar e representada como um dado WKT (Well Know Text), que é um formato mantido pelo Open Geospatial Consortium (https://www.ogc.org/).

Considerando estes predicados, um dado conectado poderia ser representado através de um formato de serialização como o Terse Triple Language (https://www.w3.org/TR/turtle/)

### Happy Coding!.
