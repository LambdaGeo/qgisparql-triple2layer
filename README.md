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

## A seguir é possivel ver na figura 4 a interface gráfica inicial do plugin “**Triple2Layer**”.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/f1d3c4d2-c02c-495d-b7db-33b48dadc84e" alt="Figura 4: Interface do plugin Triple2layer">
  <p>Figura 4: Interface do plugin Triple2layer <p/>
</div>



## caracteristicas:

Atualmente o plugin é compatível com servidores de banco de dados conectados, denominados em inglês como triple store, independentemente de implementação (ex. Virtuoso e Apache Jena ***Fuseki)***.  Além destes servidores, a atual versão é capaz de carregar dados do portal de dados denominado de [data.world](http://data.world) ([https://docs.data.world/](https://docs.data.world/i)).

Esses portais de dados, possuem uma coleção de triplas que representam dados conectados. Onde cada objeto pode estar relacionado a outros objetos via predicados. Considere os seguintes predicados: 

- `cells:resolution`, poderia ser uado para indicar a resolução espacial de um objeto que é representada por um valor numérico
- `sdmx:refArea` poderia ser usado para trazer alguma informação sobre a localização espacial de um dado objeto. Como o nome ou sigla de um país ou estado.
- `geo:asWkt` pode ser usado para relacionar um objeto com sua representação geometicar e representada como um dado WKT (Well Know Text), que é um formato mantido pelo Open Geospatial Consortium (https://www.ogc.org/).

Considerando estes predicados, um dado conectado poderia ser representado através de um formato de serialização como o Terse Triple Language (https://www.w3.org/TR/turtle/)

### Happy Coding!.


# Acessando o Plugin

Para utilizarmos o **Triple2Layer** basta abrir o **QGIS** na barra de menu e passar o mouse por cima do vetor através do qual será possível ver as ferramentas nos permitindo, assim, manipular camadas vetoriais. Dessa forma será possível acessar em célula QGISPARQL os plugins da **DBCells**. 

Na Figura 3 a seguir, podemos ver a **área dos plugins ativos indicada** com a seta de número 3.  Indo em vetor na barra de menu como mostrado na seta de número 1,podemos então abrir o plugin **Triple2Layer** e selecionar o plugin desejado, no caso o **Triple2Layer** mostrado na seta de número 2.
<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/23c78753-dc02-430a-be49-fa21e59b5fe2" alt="Figura 3: Menu de ferramentas">
  <p> Figura 3: Menu de ferramentas <p/>
<div/>

Na interface gráfica principal do plugin **Triple2Layer** é possível ver na Figura 5 a primeira e a segunda parte. Na primeira contém informações em relação ao arquivo carregado e ao tipo de endpoint. Já na segunda, temos a tabela, onde serão carregados os atributos necessários para a importação. Nessa interface encontramos também o botão “import” que faz a importação do **Layer** para o servidor. Ao seu lado, está o botão “cancelar”, cuja finalidade é fazer o cancelamento de toda execução como também fechar a interface gráfica.
  
<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/90dbcbd7-33f5-4e8d-a07a-ffa84a910c56" alt="Figura 5: Subdivisão do plugin Triple2layer">
  <p> Figura 5: Subdivisão do plugin Triple2layer <p/>
<div/>

# Importando os dados

## Base de dados conectados

Este plugin visa importar os dados de base de dados conectado e convertê-lo para uma camada de dado geográfico no sistema de informação geográfica QGIS (https://qgis.org/).

Atualmente o plugin é compatível com servidores de banco de dados conectados, denominados em inglês como triple store, independentemente de implementação (ex. Virtuoso e Apache Jena ***Fuseki)***.  Além destes servidores, a atual versão é capaz de carregar dados do portal de dados denominado de [data.world](http://data.world) ([https://docs.data.world/](https://docs.data.world/i)).

Esses portais de dados, possuem uma coleção de triplas que representam dados conectados. Onde cada objeto pode estar relacionado a outros objetos via predicados. Considere os seguintes predicados: 

- `cells:resolution`, poderia ser uado para indicar a resolução espacial de um objeto que é representada por um valor numérico
- `sdmx:refArea` poderia ser usado para trazer alguma informação sobre a localização espacial de um dado objeto. Como o nome ou sigla de um país ou estado.
- `geo:asWkt` pode ser usado para relacionar um objeto com sua representação geometicar e representada como um dado WKT (Well Know Text), que é um formato mantido pelo Open Geospatial Consortium (https://www.ogc.org/).

Considerando estes predicados, um dado conectado poderia ser representado através de um formato de serialização como o Terse Triple Language (https://www.w3.org/TR/turtle/) da seguinte maneira:

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

De modo simplificado, uma base de dados conectados pode ser entendido como uma coleção de dados como estes. Para selecionar as informações o plugin tem como entrada um uma consulta SPARQL ([https://www.w3.org/TR/sparql11-query](https://www.w3.org/TR/sparql11-query/)) que contém um conjunto de padrões de triplas que podem possuir algumas variáveis que serão substituídas de modo a realizar um determinado casamento.  Considerando uma base de dados conectada como a descrita, poderíamos usar a seguinte consulta SPARQL para trazer a resolução e as geometrias de um dado objeto.

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

Observe que pelo padrão:

```cpp
?cell sdmx-dimension:refArea "AC".
```

Essa consulta terá como resultado apenas as informações para este estado Brasileiro, no caso o Acre. 

Ao processar essa consulta em uma base de dados conectada, o resultado poderia ser exibido em um formato de tabela com três colunas, representadas pelas variáveis que aparecem na clausula `select`:

```cpp
SELECT ?cell ?resolution ?wkt 
```

![Tabela 1: Tabela de consulta SPARQL](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/d9f0e38a-bd55-4a69-8ac6-2806f520cb29)
Tabela 1: Tabela da consulta SPARQL 

Veremos a seguir que o plugin, precisará de algumas informações do usuários para poder transformar uma tabela de dados, como a descrita na Tabela 1, em uma camada geográfica. 

## Importando

Para importarmos um dado precisamos carregar um “SPARQL file”. Podemos fazer o carregamento do **arquivo RDF** abrindo a caixa de diálogo clicando no botão no lado direito como mostrado na figura 6 a seguir

![Figura 6: Botão de carregamento do SPARQL  file](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/8caac20e-cf6d-4ff5-bc93-052b3335033a)
  
Figura 6: Botão de carregamento do SPARQL  file

Ao clicar no botão vai abrir uma caixa de diálogo no explorador de arquivos do computador, onde podemos selecionar o arquivo que precisaremos como mostrado a Figura 7. Podemos então escolher um arquivo como mostrado na seta de numero 1 e podemos clicar em abrir para fazer o carregamento do dado. 

![Figura 7: Seleção do SPARQL  file](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/5055df8a-338c-48d9-a75d-30936c1383a3)
Figura 7: Seleção do SPARQL  file

Com o arquivo carregado podemos ver que irá aparecer a tabela de atributos como mostrado na figura 8 a seguir. Os atributos do plugin são as informações necessárias para se conectar ao endpoint RDF e executar consultas SPARQL. Esses atributos são usados pelo plugin para enviar consultas SPARQL ao endpoint e retornar os resultados para o usuário.

![Figura 8: Carregamento da tabela após seleção do arquivo](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/308aaa2b-120a-4410-b21d-76c4d632b6c3)

Figura 8: Carregamento da tabela após seleção do arquivo

Ao escolher o arquivo é carregado o código descrito a seguir que realiza uma consulta SPARQL que passa por uma serie de tratamentos de dados usando a linguagem Python

```cpp
['prefix', 'geo:', '<http://www.opengis.net/ont/geosparql#>', 'SELECT', '?cell', '?wkt', '?res', 'WHERE', '{', '?cell', 'geo:asWKT', '?wkt.', '?cell', '<http://purl.org/ontology/dbcells/cells#resolution>', '?res.', '?cell', '<http://purl.org/linked-data/sdmx/2009/dimension#refArea>', '"AC".', '}']
['cell', 'wkt', 'res']
```

A linguagem de consulta usada para recuperar informações de bancos de dados RDF (Resource Description Framework). 

No geral, essa consulta SPARQL busca células com propriedades específicas relacionadas à geolocalização, resolução e área de referência, e retorna as variáveis "?cell", "?wkt" e "?res" como resultados.

Podemos então selecionar o tipo do endpoint “triple Store Endpoint” ou “Data.world Dataset” como mostrado na figura 9 a seguir pela seta de numero 1 e colocar a URL de endpoint na célula que a seta de numero 2 mostra.

![Figura 9: Tipo de Endpoint](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/56299ddd-803d-468f-8894-73d572935825)

Figura 9: Tipo de Endpoint

Logo após, de acordo com a preferencia, colocar ou não um nome no layer.

Na figura 10, por exemplo o nome do layer de exemplo foi “layer_ACRE” por se tratar de um dado do acre.

![Figura 10: Nome do Layer](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/6e9207d2-cbad-49a5-8232-ece75f6c9042)

Figura 10: Nome do Layer

Os atributos do plugin são as informações necessárias para se conectar ao endpoint RDF e executar consultas SPARQL. Isso pode incluir a URL do endpoint, bem como os detalhes da consulta SPARQL, como a consulta em si e quais resultados devem ser retornados. Esses atributos são usados pelo plugin para enviar consultas SPARQL ao endpoint e retornar os resultados para o usuário. 

Podemos então fazer a seleção dos atributos que queremos importar  como mostrado na figura 11 a seguir

![Figura 11: Seleção de atributos](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/3aa36797-0dcb-4cc0-be68-c622e47d601c)

Figura 11: Seleção de atributos

Através desses tratamentos é possivel realizar a seguinte consulta através do plugin 

Irá trazer apenas as informações estão relacionados com este estado Brasileiro,  no caso o Acre.

Ao processar essa consulta, o resultado poderia ser exibido em um formato de tabela com três colunas, representadas pelas variáveis `cell` , `resolution` e `wkt:`

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

Essa consulta carrega o seguinte polígono, como podemos ver no código a seguir:

```cpp
geommmmmm <QgsGeometry: Polygon ((-66.66666696000000059 -9.92973074900001684, -66.58333362999999849 -9.92973074900001684, -66.58333362999999849 -10.01306407900001716, -66.66666696000000059 -10.01306407900001716, -66.66666696000000059 -9.92973074900001684))>
```

Antes de fazer a importação faça um observe se todos esses passos foram seguidos e se todos os dados foram coletados de acordo com a imagem a seguir.

1. arquivo carregado
2. endpoint e fonte do endpoint declarados (“Triple Store Endpoint”)
3. atributos selecionados
4. nome do layer ok como de preferencial

Pronto! Tudo ok, podemos importar o layer.

### Importando para o Data world

A segunda opção de importação é importar para um **Dataset Data World.**  Para importar, basta escolhermos essa opção clicando no botão na parte esquerda como mostrado na figura, nela podemos escolher a segunda maneira de fazer importação. Clicando em “Data.World Dataset” podemos importar um dado RDF para um dataset do data world.

Para importação usando a fonte do Data World a única diferença é que precisamos selecionar a celula do “Data.World Dataset” como mostrado na figura 12 a seguir
  
![Figura 12: Selecionando endpoint para Data world](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/6e2479ad-a8eb-4946-8db0-1cafef0feaf7)

Figura 12: Selecionando endpoint para Data world

Podemos então colocar o caminho do nosso dataset na célula mostrada na figura 13 a seguir a fonte para o qual queremos importar

![Figura 13: Botão de carregamento do SPARQL  file](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/f0a33a1a-747f-4303-b737-cfce4ad7fcf1)

Figura 13: Botão de carregamento do SPARQL  file

O plugin apresenta uma interface de usuário para configurar opções de importação. O botão SPARQL é usado para abrir uma janela de diálogo que permite a entrada de uma consulta SPARQL personalizada. O token de acesso para a plataforma Data.Word pode ser definida usando o “token”.

O próximo passo vai ser colocar o ir em settings no canto superior esquerdo e selecionar “Token Dataworld” como mostrado na figura 14 a seguir.

![Figura 14: Token Data world](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/6b95c68e-7abf-4e66-9a67-f2eaa3443f2a)
 
Figura 14: Token Data world

Depois que a célula for selecionada podemos colocar o token no label de numeração 1 e posteriormente apertar em “ok” na seta 2 como mostrado na figura 15 abaixo.

![Figura 15: Token do Dataset](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/73b00d32-2e21-4f2a-8056-d7ae4226fa4c)

Figura 15: Token do Dataset

A partir desse ponto o restante do processo é idêntico a importação do triplestore

Antes de fazer a importação faça um observe se todos esses passos foram seguidos e se todos os dados foram coletados de acordo com a imagem a seguir.

1. arquivo carregado
2. endpoint e fonte do endpoint declarados( “Data.World Dataset”)
3. atributos selecionados
4. nome do layer ok como de preferencial

não esqueça de checar se tá tudo ok.

## Importando o layer

Por fim, podemos fazer a importação do dado de acordo como mostrado na figura 16 a seguir clicando em “importar”.

![Figura 16: Import from triple store](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/075913f7-5c6a-4b64-88fb-bc8319242509)

Figura 16: Import from triple store

Ao clicarmos, primeiramente veremos a mensagem que o layer está sendo importado e logo após é feito o carregamento do mesmo.

![Figura 17: Carregamento do Layer](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/08101049-a96b-4298-93af-c3f9fac87edf)

Figura 17: Carregamento do Layer

A seguir a imagem do **Layer** 100% carregado 

![Figura 18: Layer carregado](https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/009667ff-08b2-41d8-bee5-4e5956bcedbe)

Figura 18: Layer carregado
