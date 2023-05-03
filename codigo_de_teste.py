def pegarendpoint():
    
    with open("C:/Users/DELL/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/qgisparql-triple2layer/triplestore.txt", "r") as arquivo:
                
        linhas = arquivo.readlines()
        
        ultima_linha = linhas[-1].strip()
        print(ultima_linha)
        return ultima_linha
    
x=pegarendpoint()
print(x)