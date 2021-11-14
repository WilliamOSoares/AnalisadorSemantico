tabelaSim = {}
tabelaT = {"IDE": "nome"}
lista = {"IDE": "nome"}
#tabelaT[1] = lista
print(tabelaT.get("IDE","não foi encontrado"))
tabelaSim[1] = "teste", "af"
tabelaSim[2] = "teste2", "ad"
print(tabelaSim.get(2, "não foi encontrado"))
tabelaSim[2] = "test3", "adsd"
print(tabelaSim.get(2, "não foi encontrado"))
print(tabelaSim)
print(tabelaSim.get(1, "não foi encontrado"))
print(tabelaSim.get(3, "não foi encontrado"))
a = tabelaSim.keys()
print(a)
for chave in tabelaSim.keys():
    if(chave == 2):
        print(chave) #dizer erro semantico

tabela = []
aux = {"IDE0": "alfabeto", "TIPO": "CAD", "ESCOPO": "algoritmo", "LINHA": "15", "INST": "VAR"}
tabela.append(aux)
aux = {"IDE1": "moab", "TIPO": "CAD", "ESCOPO": "algoritmo", "LINHA": "17", "INST": "VAR"}
tabela.append(aux)
aux = {"IDE2": "puta", "TIPO": "CAD", "ESCOPO": "algoritmo", "LINHA": "18", "INST": "VAR"}
tabela.append(aux)
print(tabela)
print(tabela[1])
print(tabela[1].get("IDE1","Não foi"))
aux = {"IDE4": "as", "TIPO": "CAD", "ESCOPO": "algoritmo", "LINHA": "15", "INST": "VAR"}
y = len(tabela)
i = 0
for chave in range(len(tabela)):
    g = "IDE"+str(i)
    if(tabela[chave].get(g,"não foi")== aux.get("IDE4","Não foi")):
        print("são iguais") #dizer erro semantico
    print(g)
    print(tabela[chave].get(g,"não foi"))
    print(aux.get("IDE4","Não foi"))
    i=i+1
'''
for i in y:
    g = "IDE"+str(i)
    valor = tabela[i].get(g,"não foi")
    if(valor == aux.get("IDE4","Não foi")):
        print(valor)
    #i=i+1
'''