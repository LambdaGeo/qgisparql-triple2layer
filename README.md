# QGISSPARQL:Triple2Layer

# Visão geral

**Repositório**: https://github.com/LambdaGeo/qgisparql-triple2layer/

**Criadores**: [Sérgio Souza Costa](https://github.com/profsergiocosta) e  [Nerval Junior](https://github.com/nervaljunior)

### Este plugin visa importar os dados de base de dados conectado e convertê-lo para uma camada de dado geográfico no sistema de informação geográfica QGIS (https://qgis.org/).

# Triple2Layer
## An application for importing geographic data

![](https://img.shields.io/badge/Language-Python-blue)![](https://img.shields.io/badge/Compiler-QGIS-brightgreen) ![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) ![](https://img.shields.io/badge/Environment-Windows-red) ![](https://img.shields.io/badge/Environment-Linux-purple) ![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---

## Como utilizar 

<aside>
💡 As capturas de tela para esta documentação foram tiradas no QGIS 3.26.3 em execução no Windows. Dependendo da sua configuração, as telas que você encontra podem parecer um pouco diferentes. No entanto, todos os mesmos botões ainda estarão disponíveis e as instruções funcionarão em qualquer sistema operacional. Você precisará do QGIS 3.4 (a versão mais recente no momento de redação) para usar este curso.

</aside>


💡 Antes de iniciar este exercício, o Plugin **Triple2Layer** deve estar instalado no seu computador.


Vamos começar imediatamente!

Para utilizarmos o **Triple2Layer** basta abrir o **QGIS** na barra de menu e passar o mouse por cima do vetor através do qual será possível ver as ferramentas nos permitindo, assim, manipular camadas vetoriais. Dessa forma será possível acessar em célula QGISPARQL os plugins da **DBCells**. 

Na Figura 1 a seguir, podemos ver a **área dos plugins ativos indicada** com a seta de número 3.  Indo em vetor na barra de menu como mostrado na seta de número 1,podemos então abrir o plugin **Triple2Layer** e selecionar o plugin desejado, no caso o **Triple2Layer** mostrado na seta de número 2.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/bac31c85-387e-49ac-aefb-9795fa5e5b3c" alt="Figura 1: Menu de ferramentas">
  <p> Figura 1: Menu de ferramentas </p>
</div>


A seguir é possivel ver na Figura 2 a interface inicial do plugin “**Triple2Layer**”.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/3984ccb8-02cd-457e-9369-02f25f823dd7" alt="Figura 2: Interface do plugin Triple2layer">
  <p>Figura 2: Interface do plugin Triple2layer </p>
</div>


Na interface gráfica principal do plugin **Triple2Layer** é possível ver na Figura 3 a primeira e a segunda parte. Na primeira contém informações em relação ao arquivo carregado e ao tipo de endpoint. Já na segunda, temos a tabela, onde serão carregados os atributos necessários para a importação. Nessa interface encontramos também o botão “import” que faz a importação do **Layer** para o servidor. Ao seu lado, está o botão “cancelar”, cuja finalidade é fazer o cancelamento de toda execução como também fechar a interface gráfica.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/bf8f5123-2b3b-43cb-b2a5-d514a90888dc" alt="Figura 3: Subdivisão do plugin Triple2layer">
  <p>Figura 3: Subdivisão do plugin Triple2layer </p>
</div>


# Importando os dados

## Passo 1: Definindo o nome da camada geográfica

Este *plugin* visa importar os dados conectados de um repositório e convertê-los para uma camada de dados geográficos dentro do sistema de informação geográfica QGIS ([https://qgis.org/](https://qgis.org/)).

Com o plugin aberto, o primeiro passo é colocar o nome que o *layer* (camada geográfica) terá ao ser criado, como mostrado na Figura 4. Neste exemplo, definiu-se o nome do *layer* de como “ACRE” dado que iremos importar dados sobre este estado.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/435bf5f4-53b0-4911-b55d-ad74a0348704" alt="Figura 4: Nome do Layer">
  <p> Figura 4: Nome do Layer </p>
</div>


## Passo 2: Definindo a fonte dos dados conectados

A versão atual do plugin permite importar dados de duas fontes de dados:

- Servidores de banco de dados conectados, denominados em inglês como triple store, independentemente de implementação (ex. Virtuoso ou Apache Jena ***Fuseki).***
- Portal de dados denominado de [data.world](http://data.world) ([https://docs.data.world/](https://docs.data.world/i)).

Esses portais de dados possuem uma coleção de triplas que representam os dados conectados, onde cada objeto pode estar relacionado a outros objetos via predicados.  

Para a criação de uma camada geográfica (layer), é necessário que estes dados possuam um atributo geométrico, como o predicado `geo:asWKT` no Código 1:

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

No paradigma de dados conectados (veja mais em: [https://ceweb.br/livros/dados-abertos-conectados/](https://ceweb.br/livros/dados-abertos-conectados//)) cada recurso possui uma URI, neste exemplo temos a seguinte URI representando um recurso:

```cpp
<https://purl.org/dbcells/epsg4326#R0_0830Cx-34_7917Cy-6_9714>
```

Este recurso está conectado a outras informações por meio de 3 predicados, neste exemplo o recurso representa um polígono que possui uma resolução espacial (área do polígono), sua forma geométrica no formato WKT e uma informação adicional indicando em que estado brasileiro este polígono se localiza. 

<aside>
💡 De modo simplificado, uma base de dados conectados, como o [Data.World](http://Data.World) ou um servidor triple store, pode ser entendida como uma coleção de triplas, como descrita no Código 1.

</aside>

Podemos então selecionar o tipo do endpoint “triple Store Endpoint” ou “Data.world Dataset” como mostrado na Figura 5 pela seta de número 1 e 2. 

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/6f64e68c-f424-4c67-9570-bd0691c3c57b" alt="Figura 5: Tipo de Endpoint">
  <p> Figura 5: Tipo de Endpoint </p>
</div>

No caso do Triple Store colocaremos a URL do servidor como podemos ver na Figura 6.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/26d6e447-6338-4993-87d3-0ad2d1f97401" alt="Figura 6: Selecionando endpoint para Triple Store">
  <p> Figura 6: Selecionando endpoint para Triple Store </p>
</div>


No caso do Data World utilizaremos o nome do Dataset como podemos ver na Figura 7.
<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/92d9f105-995e-4ba7-842b-bb287a45163c" alt="Figura 7: Selecionando endpoint para Data world">
  <p> Figura 7: Selecionando endpoint para Data world </p>
</div>

Além disso, no caso no Data world, para importação é necessário definir um token de acesso. O token pode ser encontrado nas configurações no portal do Data world, como mostrado na Figura 8

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/dc1897a5-628e-44e1-9f10-583b42bcb9f0" alt="Figura 8: API Token">
  <p> Figura 8: API Token </p>
</div>



Em “Settings” no canto superior esquerdo podemos selecionar a opção “Token Dataworld”, como mostrado na Figura 9. 

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/8abebdf4-7a0c-4bf1-86b2-ffaad6822157" alt="Figura 9: Token Data world">
  <p> Figura 9: Token Data world </p>
</div>


Depois que a caixa de texto for selecionada, com o token usado para leitura e escrita (read/write) copiado anteriormente, podemos colar no label de numeração 1 e posteriormente apertar em “ok” na seta 2 como mostrado na figura 10 abaixo.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/ec71c8d9-27d0-494d-94ce-43cda02e12a4" alt="Figura 10: Token do Dataset">
  <p> Figura 10: Token do Dataset </p>
</div>


## Passo 3: Abrindo um arquivo com uma consulta SPARQL

Uma fonte de dados conectados possui milhares ou milhões de triplas. Então, eles suportam  uma linguagem de consulta denominada de SPARQL ([https://www.w3.org/TR/sparql11-query](https://www.w3.org/TR/sparql11-query/)). Essa linguagem permite definir quais triplas que queremos carregar a partir de casamentos de padrões.  Esse conjunto de padrões de triplas podem possuir algumas variáveis que serão substituídas de modo a realizar um determinado casamento.  Considerando a base de dados descrita em Código 1, poderíamos usar a seguinte consulta SPARQL para trazer a resolução e as geometrias de um dado objeto.

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

Em um repositório de dados conectado, essa consulta terá como resultado apenas as informações para este estado Brasileiro, no caso o Acre.  Ao processar essa consulta em uma base de dados conectada, o resultado poderia ser exibido em um formato de tabela com três colunas, representadas pelas variáveis que aparecem na cláusula `select`:

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/4d0d7fbf-7253-4ead-9ea4-33404491ae7b" alt="Tabela 1: Tabela da consulta SPARQL">
  <p> Tabela 1: Tabela da consulta SPARQL </p>
</div>


Veremos a seguir que o plugin precisará de algumas informações do usuário para poder transformar uma tabela de dados, como a descrita na Tabela 1, em uma camada geográfica. 

Podemos carregar um arquivo SPARQL abrindo a caixa de diálogo, clicando em “Open SPARQL” como podemos ver na Figura 11.

<aside>
💡 Para este exemplo, considere um arquivo SPARQL como o descrito no Código 2

</aside>

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/b6b6040d-e316-4de8-bb64-e6c280706519" alt="Figura 11: Botão de carregamento do SPARQL  file">
  <p> Figura 11: Botão de carregamento do SPARQL  file </p>
</div>


Ao clicar no botão, vai abrir uma caixa de diálogo no explorador de arquivos do computador, onde podemos selecionar o arquivo necessário à consulta, como mostrado na Figura 12. Podemos então escolher um arquivo como mostrado na seta de número 1 clicando em abrir para fazer o carregamento do dado. 

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/716aa8b5-4b43-4e83-b970-7c3e9238b980" alt="Figura 12: Seleção do SPARQL  file">
  <p> Figura 12: Seleção do SPARQL  file </p>
</div>


A seguir veremos a definição de como os atributos serão utilizados para a ciração da camada geográfica no QGIS.

## Passo 4: Definição dos atributos

Com o arquivo carregado irá aparecer a tabela de atributos como mostrado na Figura 13.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/4d9597d3-f466-4494-84bd-25edcffc7773" alt="Figura 13: Carregamento da tabela após seleção do arquivo">
  <p> Figura 13: Carregamento da tabela após seleção do arquivo </p>
</div>


Nessa tabela (2) da  Figura 13, serão definidas algumas informações necessárias para a criação da camada geográfica a partir do resultado da consulta SPARQL. Por exemplo, poderemos definir qual atributo será o identificador e qual será usado para representar a geometria. Podemos definir o nome do atributo, que poderá ser diferente do nome da variável no arquivo SPARQL. Além de definir o tipo de dados do atributo, e quais deles serão importados.

### Selecionando o atributo que possui a geometria

Primeiramente, na seleção de atributos da Figura 14, é feito a escolha que represente a geometria. Até o atual momento, a representação suportada pelo plugin é o WKT(Well Know Text), podendo ter geometrias definidas com pontos, linhas e polígonos. Ao selecionar a geometria como uma variável WKT, mostrado na Figura 14, observaremos que as opções de “Attribute name“ e “Attribute type“ são desabilitadas.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/413f8b89-34ef-4f8d-9fb7-2c51b428132d" alt="Figura 14: Seleção do tipo de geometria">
  <p> Figura 14: Seleção do tipo de geometria </p>
</div>

### Selecionado os atributos que serão importados

Nem todos os atributos que virão da consulta precisam ser importados.  O usuário irá marcar os atributos que ele deseja que seja importado para a camada geográfica.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/ebb391b2-0dc5-48dd-8056-734660ac0bc5" alt="Figura 15: Seleção de atributos para importação">
  <p> Figura 15: Seleção de atributos para importação </p>
</div>


### Definindo o nome e o tipo dos atributos

Na seleção de atributos é possível alterar o nome do atributo e o seu tipo de dados. Para alterar o nome do atributo basta dar dois cliques em cima do atributo selecionado e digitar o novo nome.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/0d0dd35f-1bad-444f-9157-e8968bf17bb7" alt="Figura 16: Attribute name">
  <p> Figura 16: Attribute name </p>
</div>


Com relação aos tipos de dados, por padrão eles serão importados como `String`, que representa um texto. No entanto, podemos alterá-lo para `Int`, que representa um número inteiro, ou `Double`, que representa um número real. Neste exemplo, resolução é um dado numérico com casas decimais, representando a resolução da célula, que é melhor representado como um `Double`. 

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/e37fdfe7-51ce-427c-a929-1ecddd511279" alt="Figura 17: Attribute type">
  <p> Figura 17: Attribute type </p>
</div>



### Selecionando qual dos atributos será o identificador da camada geográfica

Uma camada geográfica, como uma tabela em um banco, requer que cada registro (ou linha) possua um identificador (conhecido como chave primária). Em alguns casos, essa informação virá como resultado da consulta ao repositório, então pode-se indicar qual dos atributos representa esse identificador. Um critério importante é que os valores deste atributo sejam únicos, não podemos ter repetições. Caso não seja selecionado, será definido um ID como auto-incremento, ou seja, valores inteiros de 1 até a quantidade de objetos.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/c6125966-a5f5-4e6e-921d-84fea1a8b0aa" alt="Figura 18: Identificador único">
  <p> Figura 18: Identificador único </p>
</div>


## Passo 5: Executando a importação

Por fim, podemos fazer a importação do dado conforme a figura 19 clicando em “importar”.


<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/1bd2f77d-90e1-48b1-809b-0494f1c6e95d" alt="Figura 19: Import layer">
  <p> Figura 19: Import layer </p>
</div>


Ao clicarmos, primeiramente veremos a mensagem que o layer está sendo importado e logo após é feito o carregamento do mesmo.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/0f63542b-2456-4c6a-9e70-6b55fda1d1f4" alt="Figura 20: Carregamento do Layer">
  <p> Figura 20: Carregamento do Layer </p>
</div>


A seguir a imagem do **Layer** 100% carregado.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/9c512014-cc54-40a4-8a4a-add54a0132ca" alt="Figura 21: Layer carregado">
  <p> Figura 21: Layer carregado </p>
</div>


Ao carregar o layer podemos selecionar a camada carregada como mostrado pela seta e numero 1 na Figura 22.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/0324a30c-250d-4ba6-a2c9-9a136bd1a491" alt="Figura 22: abrindo tabela de atributos do QGIS">
  <p> Figura 22: abrindo tabela de atributos do QGIS </p>
</div>


Clicando na tecla F6 conseguimos abrir a tabela de atributos do layer selecionado como mostrado na Figura 23.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-triple2layer/assets/108685222/e511f8cf-f9cd-49c6-9a07-2f226e902eb0" alt="Figura 23: tabela de atributos do QGIS">
  <p> Figura 23: tabela de atributos do QGIS </p>
</div>
