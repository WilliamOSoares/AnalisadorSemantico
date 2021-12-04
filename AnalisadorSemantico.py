#coding: utf-8
import os
import shutil

countArq = 1
countLinha = 1
estado = "Q0"
buffer = ""
linhaCoMF = 1
space = False #Caso pegue o espaço ou Tab 
skip = False #Usado para pular linha
endRead = False #Acaba a leitura de arquivos
pre = ["algoritmo","variaveis","constantes","registro","funcao","retorno","vazio","se","senao","enquanto","para","leia","escreva","inteiro","real","booleano","char","cadeia","verdadeiro","falso"]
erros = []
errosSeman = []
siglaErro = ["SIB","SII","CMF","NMF","CaMF","CoMF","OpMF","SyntaxError", "SemanticoError"]
dados = []
tuplas = []
iterador = 0
linha = "01"
looping = False #Verifica se entrou mais de uma vez, utilizado em expressao
ide = "" 
ideExp = ""
tipo = ""
escopo = ""
regra = ""
regis = ""
retorno = False
retornado = False
tabela = []
paran = []
expressao = False #Se for True é uma expressão lógica ou relacional, se false é aritmetica
fator = True #Se for False é dois fatores em expressão (a||b) e (2+2), se True é um fator (a)
vetorial = False #Se for True é vetor/matriz, se False não é
chamada = "" #Se for Vazio é uma chamada de função, senão é False
atribu = True #Se for True o identificador existe, senão ele não existe
veterror = True #Se for True não há erro na instância do vetor, senão tem
algeb = "" #  "ari"= aritmetico "rel"=relacional "rll"= são os == e != "log"=logicos
ultipo = "" # Ulitmo tipo da ide utilizada na expressão
dentroParen = False # se false não tá dentro do parenteses, se for True, te dentro
verifexpress = True # Se true verifica expressão, se false já tem erro
bufferExpressao = ""
tipoChamada = ""

# Abertura do arquivo
def input():
    global countArq, endRead
    f=""
    try:
        f = open ("input/entrada%d.txt" %countArq, "r")        
    except: 
        endRead = True
        print("Arquivo nao encontrado!")        
    return f

# Escreve uma nova linha no arquivo de saída
def output(linha, code, buffer):
    global countArq, erros, siglaErro, dados, tuplas, errosSeman
    f = open("output/saida%d.txt" %countArq,"a")
    if(code == "ERRO"): 
        if erros:
            for x in erros:
                f.write(x)
                f.write("\n")
        else:
            f.write("SUCESSO!")
    else:
        if(linha<10):
            linhaSaida = "0" + str(linha) + " " + code +" " + buffer
            tuplas.append("0" + str(linha))
            tuplas.append(code)
            tuplas.append(buffer)
        else:
            linhaSaida = str(linha) + " " + code +" " + buffer
            tuplas.append(str(linha))
            tuplas.append(code)
            tuplas.append(buffer)
        flagER = False
        for x in siglaErro:
            if(x==code):
                flagER = True
        if(flagER):
            if("SemanticoError"==code):
                repetido=False
                for z in range(len(errosSeman)):
                    if(errosSeman[z]==linhaSaida):
                        repetido=True
                if(not(repetido)):
                    errosSeman.append(linhaSaida)
                tuplas = []
            else:        
                erros.append(linhaSaida)
                tuplas = []
        else:
            dados.append(tuplas)
            tuplas = []
    f.close()

# Verifica se é uma palavra reservada ou identificador
def PREouIDE(palavra, linha):
    global pre
    flagPRE = False
    for x in pre:
        if(x==palavra):
            flagPRE = True
    if(flagPRE):
        output(linha,"PRE",buffer)
    else:
        output(linha,"IDE",buffer)

########################################## Máquina de Estados Finitas #############################################################################################################################
def maqEstados(caractere,entrada, linha):
    global buffer, estado
    
    if(estado =="Q0"):
        estadoQ0(caractere, entrada, linha)
    elif(estado == "Q1"):
        estadoQ1(caractere, entrada, linha)
    elif(estado == "Q2"):
        estadoQ2(linha)
    elif(estado == "Q3"):
        estadoQ3(caractere, entrada, linha)
    elif(estado == "Q4"):
        estadoQ4(caractere, entrada, linha)
    elif(estado == "Q5"):
        estadoQ5(caractere, entrada, linha)
    elif(estado == "Q6"):
        estadoQ6(caractere, entrada, linha)
    elif(estado == "Q7"):
        estadoQ7(caractere, entrada, linha)
    elif(estado == "Q8"):
        estadoQ8(linha)
    elif(estado == "Q9"):
        estadoQ9(caractere, entrada, linha)
    elif(estado == "Q10"):
        estadoQ10(linha)
    elif(estado == "Q11"):
        estadoQ11(caractere, entrada, linha)
    elif(estado == "Q12"):
        estadoQ12(caractere, entrada, linha)
    elif(estado == "Q13"):
        estadoQ13(caractere, entrada, linha)
    elif(estado == "Q14"):
        estadoQ14(linha)
    elif(estado == "Q15"):
        estadoQ15(linha)
    elif(estado == "Q16"):
        estadoQ16(caractere, entrada, linha)
    elif(estado == "Q17"):
        estadoQ17(linha)
    elif(estado == "Q18"):
        estadoQ18(caractere, entrada, linha)
    elif(estado == "Q19"):
        estadoQ19(linha)   
    elif(estado == "Q20"):
        estadoQ20()   
    elif(estado == "Q21"):
        estadoQ21(caractere, entrada, linha)  
    elif(estado == "Q22"):
        estadoQ22(caractere, entrada)  
    elif(estado == "Q23"):
        estadoQ23(caractere, entrada)  
    elif(estado == "Q24"):
        estadoQ24() 
    elif(estado == "Q25"):
        estadoQ25(caractere, entrada, linha) 
    elif(estado == "Q26"):
        estadoQ26(linha) 
    elif(estado == "Q27"):
        estadoQ27(caractere, entrada, linha)   
    elif(estado == "Q28"):
        estadoQ28(caractere, entrada, linha)   
    elif(estado == "Q29"):
        estadoQ29(linha)   
    elif(estado == "Q30"):
        estadoQ30(caractere, entrada, linha)  
    elif(estado == "Q31"):
        estadoQ31(linha) 
    elif(estado == "Q32"):
        estadoQ32(caractere, entrada, linha)
    elif(estado == "Q33"):
        estadoQ33(caractere, entrada, linha)
    elif(estado == "Q34"):
        estadoQ34(caractere, entrada, linha)   
    elif(estado == "Q35"):
        estadoQ35(linha)   
    elif(estado == "Q36"):
        estadoQ36(caractere, entrada, linha)   
    elif(estado == "Q37"):
        estadoQ37(linha)   
    elif(estado == "Q38"):
        estadoQ38(caractere, entrada, linha) 
    elif(estado == "Q39"):
        estadoQ39(caractere, entrada, linha) 
    else:
        print("Bugou o estado")

############################################### Estados ########################################################################################################################################
'''O estado 0 é reponsavel por analisar o caractere e fazer a transição para o estado responsavel em
classifcar o caractere, verificando o decimal equivalenta na tabela ascii'''
def estadoQ0(caractere,entrada, linha):
    global buffer, estado, space
    buffer=buffer+entrada
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122):
        estado = "Q1" 
    elif(caractere == 44 or caractere == 40 or caractere == 41 or caractere == 46 or caractere == 59 or caractere == 91 or caractere == 93 or caractere == 125):
        estado = "Q2"
    elif(caractere >= 48 and caractere <= 57):
        estado = "Q3"    
    elif(caractere == 124):
        estado = "Q7"
    elif(caractere == 38):
        estado = "Q9"
    elif (caractere >=60 and caractere <= 62 ):
        estado = "Q11"
    elif(caractere == 33):
        estado = "Q13"
    elif(caractere == 47):
        estado = "Q14"    
    elif(caractere == 42):
        estado = "Q15"
    elif(caractere == 45):
        estado = "Q16"
    elif(caractere == 43):
        estado = "Q18"    
    elif(caractere == 37):
        estado = "Q20" 
    elif(caractere == 123):
        estado = "Q21" 
    elif(caractere == 36 or caractere == 92 or caractere == 126 or caractere == 58 or caractere == 63 or caractere == 64 or caractere >=94 and caractere <= 96 or caractere == 35):
        estado = "Q25"
    elif(caractere == 34):
        estado = "Q27" 
    elif(caractere == 39):
        estado = "Q32"    
    else:
        if(not(caractere == 10 or caractere == 194 or caractere == 195 or caractere == 32 or caractere == 3 or caractere ==9 or caractere ==11)):
            estado = "Q26"
        else:
            buffer=""
            space = True

# Estado responsavel por classificar em identificador o caractere
def estadoQ1(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95):
        buffer=buffer+entrada
        estado = "Q1"
    elif(caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 33 or caractere == 34 or caractere == 39):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        estado = "Q0"
        PREouIDE(buffer, linha)
        buffer=""

# Estado responsavel por classificar em delimitador o caractere
def estadoQ2(linha):
    global buffer, estado
    estado = "Q0"
    output(linha, "DEL", buffer)
    buffer=""

# Do estadoQ3 ao estadoQ6 é responsavel por anlisar se é um numero, um numero flutuante ou 
# se há um erro de numero mal formado
def estadoQ3(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q3"
    elif(caractere == 46):
        buffer = buffer + entrada
        estado = "Q4"
    elif(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        estado = "Q0"
        output(linha, "NRO", buffer)
        buffer="" 

def estadoQ4(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q5"
    elif(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 46):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        output(linha, "NMF", buffer)
        estado = "Q0"
        buffer = ""

# Estado responsavel por classificar se é um numero flutante os caracteres ou se é um possivel numero mal formado 
def estadoQ5(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q5"
    elif(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 46):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        estado = "Q0"
        output(linha,"NRO",buffer)
        buffer = ""

# Estado que calssifica que é um numero mal formado os caracteres
def estadoQ6(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere == 46 or caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        estado = "Q0"
        output(linha,"NMF",buffer)
        buffer = ""

# Estado responsavel por analisar se o caractere é um possivel operador logico(||) ou um operador mal formado,
# caso volte para o estadoQ0 e classificado como operador mal formado
def estadoQ7(caractere,entrada, linha):
    global buffer, estado
    if(caractere == 124):
        buffer=buffer+entrada
        estado = "Q8"
    else:
        estado = "Q0"
        output(linha,"OpMF",buffer)
        buffer=""

# Estado que classifica o caractere em operador logico(&&)
def estadoQ8(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"LOG",buffer)
    buffer=""

# Estado responsavel por analisar se o caractere é um possivel operador logico(&&) ou um operador mal formado,
# caso volte para o estadoQ0 e classificado como operador mal formado
def estadoQ9(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 38):
        buffer = buffer+entrada
        estado = "Q10"
    else:
        estado = "Q0"
        output(linha,"OpMF",buffer)
        buffer=""

# Estado que classifica o caractere em operador logico(||)
def estadoQ10(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"LOG",buffer)
    buffer=""

# Estado que analisa se é um operador relacional do tipo > ou < ou = ou se é um possivel 
# operador relacional do tipo ==
def estadoQ11(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 61):
        buffer=buffer+entrada
        estado = "Q12"
    elif (caractere == 60 or caractere == 62):
        buffer=buffer+entrada
        estado = "Q39"
    else:
        estado = "Q0"
        output(linha,"REL",buffer)
        buffer=""

# Estado que classifica em operador relacional (==)
def estadoQ12(caractere, entrada, linha):
    global buffer, estado
    if (caractere >= 60 and caractere <= 62):
        buffer=buffer+entrada
        estado = "Q39"
    else:
        estado = "Q0"
        output(linha,"REL",buffer)
        buffer=""

# Estado que analisa se é um operador logico(!) ou um possivel operador relacional(!=)
def estadoQ13(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 61):
        buffer=buffer+entrada
        estado = "Q12"
    else:
        estado = "Q0"
        output(linha,"LOG",buffer)
        buffer=""

# Estado que classifica em operador artimetico (/)
def estadoQ14(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que classifica em operador artimetico (*)
def estadoQ15(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que anlisa se é um possivel operador artimetico do tipo -- ou de se é um operador aritimetico -
def estadoQ16(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 45):
        buffer=buffer+entrada
        estado = "Q17"
    else:
        estado = "Q0"
        output(linha,"ART",buffer)
        buffer=""

# Estado que classifica em operador artimetico (--)
def estadoQ17(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que anlisa se é um possivel operador artimetico do tipo ++ ou de se é um operador aritimetico +
def estadoQ18(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 43):
        buffer=buffer+entrada
        estado = "Q19"
    else:
        estado = "Q0"
        output(linha,"ART",buffer)
        buffer=""

# Estado que classifica em operador artimetico (++)
def estadoQ19(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que classifica como comentario de linha e ignora da linha e pula para proxima linha
def estadoQ20():
    global buffer, estado, skip
    estado = "Q0"
    buffer=""
    skip = True

# Estado que analisa se é um possivel comentario de bloco ou se é um delimitador ({).
# Do estado Q21 ao Q24 analisa o possivel comentario de bloco
def estadoQ21(caractere, entrada, linha):
    global buffer, estado, linhaCoMF
    if(caractere == 35):
        linhaCoMF = linha
        buffer=buffer+entrada
        estado = "Q22"
    else:
        estado = "Q0"
        output(linha,"DEL",buffer)
        buffer=""

def estadoQ22(caractere, entrada):
    global buffer, estado, linhaCoMF
    if(caractere == 3):
        estado = "Q0"
        output(linhaCoMF,"CoMF",buffer)
        buffer=""
    elif(caractere == 35):
        buffer=buffer+entrada
        estado = "Q23"
    else:
        if(caractere == 10):
            buffer=buffer+" "
            estado = "Q22"
        else:
            buffer=buffer+entrada
            estado = "Q22"

def estadoQ23(caractere, entrada):
    global buffer, estado, linhaCoMF
    if(caractere == 3):
        estado = "Q0"
        output(linhaCoMF,"CoMF",buffer)
        buffer=""
    elif(caractere == 35):
        buffer=buffer+entrada
        estado = "Q23"
    elif(caractere == 125):
        buffer=buffer+entrada
        estado = "Q24"
    else:
        if(caractere == 10):
            buffer=buffer+" "
            estado = "Q22"
        else:
            buffer=buffer+entrada
            estado = "Q22"

# Estado que classifica em comentario de bloco é ignora todos os caracteres que estão dentro desse comentario
# bem formado
def estadoQ24():
    global buffer, estado
    estado = "Q0"
    buffer=""

# Estado que classifica o caracter em simbolo ($ ou ` ou ~ ou ^ ou : ou ? ou @ ou _ ou \ ou #)
def estadoQ25(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 33 or caractere == 34 or caractere == 39):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        estado = "Q0"
        output(linha,"SIB",buffer)
        buffer=""

# Estado que classifica em simbolos invalidos todos os caracteres que não pertencem ao intervalo
# de 32 a 126 da tabela ascii e que não seja final de linha, fim de arquivo, espaço, quebra de texto
# e tabulação
def estadoQ26(linha):
    global buffer, estado
    estado = "Q0"
    output(linha, "SII", buffer)
    buffer=""

# Do estadoQ27 ao estadoQ31 analisa a cadeia de caracteres
def estadoQ27(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q29"
    elif(caractere == 92):
        buffer=buffer+entrada
        estado = "Q28"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39)):
        buffer=buffer+entrada
        estado = "Q27"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""
    elif(caractere == 39):
        buffer=buffer+entrada
        estado = "Q30"
    else:
        buffer=buffer+entrada
        estado = "Q30"

def estadoQ28(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=32 and caractere <= 126):
        buffer=buffer+entrada
        estado = "Q27"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""
    elif(caractere == 39):
        buffer=buffer+entrada
        estado = "Q30"
    else:
        buffer=buffer+entrada
        estado = "Q30"

# Estado que classifica em cadeia de caractere
def estadoQ29(linha):
    global buffer, estado
    output(linha,"CAD",buffer)
    estado = "Q0"
    buffer=""

# Estado que classifica em cadeia mal formada caso não encontre o simbolo que finaliza a cadeia 
# e encontre simbolos invalidos ou apenas não encontre o simbolo que a finaliza
def estadoQ30(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q31"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q30"

# Estado que classifica em cadeia mal formada caso encontre um simbolo invalido mesmo que encontre 
# simbolo que finaliza a cadeia de caracteres
def estadoQ31(linha):
    global buffer, estado
    output(linha,"CMF",buffer)
    estado = "Q0"
    buffer=""

# Do estadoQ32 ao estadoQ37 analisa se eh um caractere simples
def estadoQ32(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 92):
        buffer=buffer+entrada
        estado = "Q34"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39) and not(caractere == 34)):
        buffer=buffer+entrada
        estado = "Q33"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

def estadoQ33(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q35"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

def estadoQ34(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39 or caractere == 34 or caractere == 92):
        buffer=buffer+entrada
        estado = "Q33"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

# Estado que classifica em caractere simples
def estadoQ35(linha):
    global buffer, estado
    output(linha,"CAR",buffer)
    estado = "Q0"
    buffer=""

# Estado que classifica em caractere simples mal formado caso não ache o simbolo que finaliza ou
# encontre um simbolo invalido e tambem não encontre o simbolo que finaliza o caractere simples
def estadoQ36(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q37"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

# Estado que classifica em caractere simples mal formado caso encontre um simbolo invalido e
# encontre o simbolo que finaliza o caractere simples
def estadoQ37(linha):
    global buffer, estado
    output(linha,"CaMF",buffer)
    estado = "Q0"
    buffer=""

##################### NOVOS ESTADOS ATUALIZADOS NA ETAPA DA IMPLEMENTAÇÃO DA SINTATICA ###################

# Estado responsavel por classificar em identificador o caractere
def estadoQ38(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        output(linha,"SIB",buffer)
        estado = "Q0"
        buffer=""
# Estado responsavel por classificar em identificador o caractere
def estadoQ39(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=60 and caractere <= 62):
        buffer=buffer+entrada
        estado = "Q39"
    else:
        output(linha,"OpMF",buffer)
        estado = "Q0"
        buffer=""        

#############################################################################################################

def proxToken():
    global dados, tuplas, iterador
    if(iterador<len(dados)):
        tuplas = [dados[iterador][0], dados[iterador][1],dados[iterador][2]]
        iterador = iterador + 1
    else:
        tuplas = [dados[len(dados)-1][0], "END", "$"]

def mantemToken():
    global dados, tuplas, iterador
    if(iterador<len(dados)):
        tuplas = [dados[iterador-1][0], dados[iterador-1][1],dados[iterador-1][2]]
    else:
        tuplas = [dados[len(dados)-1][0], "END", "$"]

########################################### Analise Sintatica ###############################################

def START():
    global tuplas, buffer, linha, escopo, tipo, ide, tabela, retorno, retornado
    escopo = "global"
    if(tuplas[2] == "algoritmo"):
        buffer = buffer + " " + tuplas[2]
        x = tuplas[0]
        proxToken()
        i = ALGORITMO()
        if(i==1):
            output(int(x), "SyntaxError", "Declaracoes Fora de Escopo: "+buffer)
            mantemToken()
            START()
    elif(tuplas[2] == "funcao"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()        
        i = FUNCAO()
        x=0
        for chave in range(len(tabela)):
            y = "IDE"+str(x)
            if(tabela[chave].get("ESCOPO","não foi")=="funcao"):
                tabela[chave].update({y:'0zero'})
            x=x+1             
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
        buffer = ""
        if(retorno and not(retornado)):
            output(int(linha), "SemanticoError", "Funcao sem retorno")
            mantemToken()
        retorno = False
        retornado = False
        START()
    elif(tuplas[2] == "constantes"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = CONSTANTES()
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
            buffer = ""
            START()
        buffer = ""
        B()
    elif(tuplas[2] == "variaveis"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = VARIAVEIS()
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
            buffer = ""
            START()
        buffer = ""
        A()
    elif(tuplas[2] == "registro"):
        buffer = buffer + " " + tuplas[2]
        tipo = tuplas[2]
        linha = tuplas[0]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            ide = tuplas[2]
            proxToken()
            i = REGISTRO()
            if(i==1):
                output(int(tuplas[0]), "SyntaxError", buffer)
                mantemToken()
            buffer = ""
        START()
    else:    
        errado = False
        if(not(len(buffer)==0)):          
            errado = True
        mantemToken()            
        while(tuplas[2]!="$"):             
            if(tuplas[2] == ";"):
                buffer = buffer + " " + tuplas[2]
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                proxToken()
                return START()
            elif(linha != tuplas[0]):
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                linha = tuplas[0]
                return START()
            else:            
                errado = True
                buffer = buffer + " " + tuplas[2]
                proxToken()  
        if(int(linha)<10):
            aux = "0"+linha
            output(int(aux), "SyntaxError", "Fim do arquivo")
        else:    
            output(int(linha), "SyntaxError", "Fim do arquivo")
        mantemToken()
        return 0

def A():
    global tuplas, buffer, linha, escopo, tipo, ide, retorno, retornado
    escopo = "global"
    if(tuplas[2] == "algoritmo"):
        buffer = buffer + " " + tuplas[2]
        x = tuplas[0]
        proxToken()
        i = ALGORITMO()
        if(i==1):
            output(int(x), "SyntaxError", "Declaracoes Fora de Escopo: "+buffer)
            mantemToken()
            A()
    elif(tuplas[2] == "funcao"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()
        i = FUNCAO()
        x=0
        for chave in range(len(tabela)):
            y = "IDE"+str(x)
            if(tabela[chave].get("ESCOPO","não foi")=="funcao"):
                tabela[chave].update({y:'0zero'})
            x=x+1  
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
        buffer = ""
        if(retorno and not(retornado)):
            output(int(linha), "SemanticoError", "Funcao sem retorno")
            mantemToken()
        retorno = False
        retornado = False
        A()
    elif(tuplas[2] == "constantes"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = CONSTANTES()
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
            buffer = ""
            A()
        buffer = ""
        C()
    elif(tuplas[2] == "registro"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        tipo = tuplas[2]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            ide = tuplas[2]
            proxToken()
            i = REGISTRO()
            if(i==1):
                output(int(tuplas[0]), "SyntaxError", buffer)
                mantemToken()
            buffer = ""
        A()
    else:    
        errado = False
        if(not(len(buffer)==0)):          
            errado = True
        mantemToken()            
        while(tuplas[2]!="$"):
            if(tuplas[2] == ";"):
                buffer = buffer + " " + tuplas[2]
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                proxToken()
                return A()
            elif(linha != tuplas[0]):
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                linha = tuplas[0]
                return A()
            else:            
                errado = True
                buffer = buffer + " " + tuplas[2]
                proxToken()
        if(int(linha)<10):
            aux = "0"+linha
            output(int(aux), "SyntaxError", "Fim do arquivo")
        else:    
            output(int(linha), "SyntaxError", "Fim do arquivo")
        mantemToken()
        return 0
def B():
    global tuplas, buffer, linha, escopo, tipo, ide, retorno, retornado
    escopo = "global"
    if(tuplas[2] == "algoritmo"):
        buffer = buffer + " " + tuplas[2]
        x = tuplas[0]
        proxToken()
        i = ALGORITMO()
        if(i==1):
            output(int(x), "SyntaxError", "Declaracoes Fora de Escopo: "+buffer)
            mantemToken()
            B()
    elif(tuplas[2] == "funcao"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()
        i = FUNCAO()
        x=0
        for chave in range(len(tabela)):
            y = "IDE"+str(x)
            if(tabela[chave].get("ESCOPO","não foi")=="funcao"):
                tabela[chave].update({y:'0zero'})
            x=x+1  
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
        buffer = ""
        if(retorno and not(retornado)):
            output(int(linha), "SemanticoError", "Funcao sem retorno")
            mantemToken()
        retorno = False
        retornado = False
        B()
    elif(tuplas[2] == "variaveis"):
        buffer = buffer + " " + tuplas[2]
        proxToken()        
        i = VARIAVEIS()
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
            buffer = ""
            B()
        buffer = ""
        C()
    elif(tuplas[2] == "registro"):
        buffer = buffer + " " + tuplas[2]
        tipo = tuplas[2]
        linha = tuplas[0]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            ide = tuplas[2]
            proxToken()
            i = REGISTRO()
            if(i==1):
                output(int(tuplas[0]), "SyntaxError", buffer)
                mantemToken()
            buffer = ""
        B()
    else:    
        errado = False
        if(not(len(buffer)==0)):          
            errado = True
        mantemToken()            
        while(tuplas[2]!="$"):
            if(tuplas[2] == ";"):
                buffer = buffer + " " + tuplas[2]
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                proxToken()
                return B()
            elif(linha != tuplas[0]):
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                linha = tuplas[0]
                return B()
            else:            
                errado = True
                buffer = buffer + " " + tuplas[2]
                proxToken()
        if(int(linha)<10):
            aux = "0"+linha
            output(int(aux), "SyntaxError", "Fim do arquivo")
        else:    
            output(int(linha), "SyntaxError", "Fim do arquivo")
        mantemToken()
        return 0
def C():
    global tuplas, buffer, linha, escopo, tipo, ide, retorno, retornado
    escopo = "global"
    if(tuplas[2] == "algoritmo"):
        buffer = buffer + " " + tuplas[2]
        x = tuplas[0]
        proxToken()
        i = ALGORITMO()
        if(i==1):
            output(int(x), "SyntaxError", "Declaracoes Fora de Escopo: "+buffer)
            mantemToken()
            C()
    elif(tuplas[2] == "funcao"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()
        i = FUNCAO()
        x=0
        for chave in range(len(tabela)):
            y = "IDE"+str(x)
            if(tabela[chave].get("ESCOPO","não foi")=="funcao"):
                tabela[chave].update({y:'0zero'})
            x=x+1  
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
        buffer = ""
        if(retorno and not(retornado)):
            output(int(linha), "SemanticoError", "Funcao sem retorno")
            mantemToken()
        retorno = False
        retornado = False
        C()
    elif(tuplas[2] == "registro"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        tipo = tuplas[2]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            ide = tuplas[2]
            proxToken()
            i = REGISTRO()
            if(i==1):
                output(int(tuplas[0]), "SyntaxError", buffer)
                mantemToken()
            buffer = ""
        C()
    else:    
        errado = False
        if(not(len(buffer)==0)):          
            errado = True
        mantemToken()            
        while(tuplas[2]!="$"):
            if(tuplas[2] == ";"):
                buffer = buffer + " " + tuplas[2]
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                proxToken()
                return C()
            elif(linha != tuplas[0]):
                if(errado):
                    output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
                    mantemToken()
                    buffer = ""
                linha = tuplas[0]
                return C()
            else:            
                errado = True
                buffer = buffer + " " + tuplas[2]
                proxToken()
        if(int(linha)<10):
            aux = "0"+linha
            output(int(aux), "SyntaxError", "Fim do arquivo")
        else:    
            output(int(linha), "SyntaxError", "Fim do arquivo")
        mantemToken()
        return 0

def ALGORITMO():
    global tuplas, buffer, escopo, linha
    escopo = "algoritmo"
    if(tuplas[2]=="{"):
        linha = tuplas[0]
        buffer = ""
        proxToken()
        i = CONTEUDO()
        if(i==0):
            buffer=""
            #proxToken()
        linha = tuplas[0]
    else:
        return 1
    foraEscopo = False
    while(tuplas[2]!="$"):
        if(not(foraEscopo)):
            foraEscopo = True
        buffer = buffer + " " + tuplas[2]
        proxToken()
    if(foraEscopo):
        if(int(linha)<10):
            aux = "0"+linha
            output(int(aux), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)
        else:    
            output(int(linha), "SyntaxError", "Declaracoes Fora de Escopo: " + buffer)    
    return 0
        
def CONTEUDO():
    global tuplas, iterador, dados, buffer, linha, tipo, ide, tabela, atribu, chamada, vetorial, fator, expressao, verifexpress, ultipo, algeb, dentroParen, bufferExpressao, tipoChamada
    atribu=True
    vetorial = False 
    expressao = False 
    fator = True 
    algeb = "" 
    ultipo = "" 
    dentroParen = False
    verifexpress = True 
    bufferExpressao = ""
    if(tuplas[2] == "}"):
        buffer = buffer + " " + tuplas[2]
        if(dados[iterador-2][2]=='{'):
            output(int(linha), "SemanticoError", "Conteudo vazio")
            mantemToken()
        proxToken()
        return 0
    elif(tuplas[2] == "escreva"):
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()            
        i = ESCREVA()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken()
            return 0
        else:
            buffer = ""
            return CONTEUDO()
    elif(tuplas[2] == "leia"): 
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()            
        i = LEIA()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken() 
            return 0
        else:
            buffer = ""
            return CONTEUDO()
    elif(tuplas[2] == "constantes"):
        buffer = buffer + " " + tuplas[2]
        proxToken()            
        i = CONSTANTES()
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", tuplas[2])
            mantemToken()
            buffer = ""
        buffer = ""
        linha = tuplas[0]
        return CONTEUDO()
    elif(tuplas[2] == "variaveis"):
        buffer = buffer + " " + tuplas[2]
        proxToken()            
        i = VARIAVEIS()
        if(i==1):
            output(int(tuplas[0]), "SyntaxError", tuplas[2])
            mantemToken()
        buffer = ""
        linha = tuplas[0]
        return CONTEUDO()
    elif(tuplas[2] == "se"): 
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()            
        i = SE()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken() 
            return 0
        else:
            buffer = ""
            return CONTEUDO()
    elif(tuplas[2] == "enquanto"): 
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()            
        i = ENQUANTO()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken() 
            return 0
        else:
            buffer = ""
            return CONTEUDO()
    elif(tuplas[2] == "para"): 
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()            
        i = PARA()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken() 
            return 0
        else:
            buffer = ""
            return CONTEUDO()        
    elif(tuplas[2] == "registro"): 
        buffer = buffer + " " + tuplas[2]
        tipo = tuplas[2]
        linha = tuplas[0]
        proxToken()            
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            ide = tuplas[2]
            proxToken()
            i = REGISTRO()
            if(i == 1):
                output(int(tuplas[0]), "SyntaxError", buffer)
                mantemToken()
            buffer = "" 
            return CONTEUDO() 
        else:
            output(int(tuplas[0]), "SyntaxError", buffer)
            mantemToken()
            buffer = ""
            return CONTEUDO() 
    elif(tuplas[2] == "retorno"): 
        buffer = buffer + " " + tuplas[2]
        linha = tuplas[0]
        proxToken()            
        i = RETORNO()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken() 
            return 0       
        else:
            buffer = ""
            if(tuplas[2] == "}"):
                buffer = ""
                proxToken()
                return 0
            else:
                errado = False
                if(not(len(buffer)==0)):          
                    errado = True
                mantemToken()            
                while(tuplas[2]!="$"):
                    if(tuplas[2]=="}"):
                        if(errado):
                            output(int(linha), "SyntaxError", buffer)
                            mantemToken()
                            buffer = ""
                        proxToken()
                        return 0
                    else:            
                        errado = True
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                if(int(linha)<10):
                    aux = "0"+linha
                    output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
                else:    
                    output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
                mantemToken() 
                return 0           
    elif(tuplas[1] == "IDE"):
        linha = tuplas[0]
        indicador = False
        i = 0
        for chave in range(len(tabela)):
            g = "IDE"+str(i)
            if(tabela[chave].get(g,"não foi")== tuplas[2]):
                indicador = True
                ide = tuplas[2]
                tipo = tabela[chave].get("TIPO","não foi")  
                if(tabela[chave].get("REGRA","não foi")== "CONST"):
                    atribu = False
                    if(not(dados[iterador][2] == '(') and linha == tuplas[0]):
                        output(int(linha), "SemanticoError", "Impossivel mudar valor de constantes: "+ide)
                        mantemToken()                          
            i=i+1
        if(not(indicador)):
            atribu = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        if((dados[iterador][2] == '[' or dados[iterador][2] == '.') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()            
            i = ACESSOVAR()
            if(i==0):
                if(tuplas[2] == '=' and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()                
                    i = EXPATRIBUICAOB()
                    if(i==0): 
                        if(tuplas[2]==";" and linha == tuplas[0]):
                            buffer = ""
                            if(atribu):
                                if(not(vetorial) and chamada==""):
                                    if(fator): #and not(tipo == dados[iterador-2][1])):
                                        aux = dados[iterador-2][1]
                                        erronio= False
                                        if(aux == "CAD"):
                                            if(not(tipo == "cadeia")):
                                                erronio = True
                                        elif(aux == "CAR"):
                                            if(not(tipo == "char")):
                                                erronio = True
                                        elif(aux == "NRO"):
                                            aux = dados[iterador-2][2]
                                            x = aux.find(".")
                                            if(x<0):
                                                if(not(tipo == "inteiro")):
                                                    erronio = True
                                            else:
                                                if(not(tipo == "real")):
                                                    erronio = True
                                        elif(aux == "PRE"):
                                            if(not(tipo == "booleano")):
                                                    erronio = True
                                        else:
                                            aux = dados[iterador-2][2]
                                            indicador = False
                                            i = 0
                                            for chave in range(len(tabela)):
                                                g = "IDE"+str(i)
                                                if(tabela[chave].get(g,"não foi")==aux):
                                                    indicador = True
                                                    if(not(tabela[chave].get("TIPO","não foi")==tipo)):
                                                        output(int(linha), "SemanticoError", "Tipos diferentes")
                                                        mantemToken()                                                   
                                                i=i+1
                                            if(not(indicador) and not(aux=="}")):
                                                output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ aux)
                                                mantemToken()                        
                                        if(erronio):
                                            output(int(linha), "SemanticoError", "Tipos diferentes")
                                            mantemToken()  
                                    else:
                                        if(expressao): #and not(tipo == "booleano")):
                                            if(buffer.find("||")>0 or buffer.find("&&")>0 or buffer.find("==")>0 or buffer.find("!=")>0 or buffer.find(">=")>0 or buffer.find("<=")>0 or buffer.find("<")>0 or buffer.find(">")>0):
                                                if(tipo != "booleano"):
                                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                                    mantemToken()  
                                            else:
                                                if(not(tipo == "inteiro" or tipo == "real")):
                                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                                    mantemToken()
                                elif(not(chamada=="")):
                                    if(tipo!=tipoChamada):
                                        output(int(linha), "SemanticoError", "Tipos diferentes")
                                        mantemToken()
                                chamada=""
                                vetorial = False
                                fator = True
                            proxToken() 
                            return CONTEUDO() 
                        else:
                            output(int(linha), "SyntaxError", buffer)
                            mantemToken()
                            buffer = ""
                            return CONTEUDO() 
                    else:    
                        errado = False
                        if(not(len(buffer)==0)):          
                            errado = True
                        mantemToken()            
                        while(tuplas[2]!="$"):
                            if(tuplas[2]=="}"):
                                if(errado):
                                    output(int(linha), "SyntaxError", buffer)
                                    mantemToken()
                                    buffer = ""
                                proxToken()
                                return 0
                            elif(tuplas[2] == ";"):
                                buffer = buffer + " " + tuplas[2]
                                if(errado):
                                    output(int(linha), "SyntaxError", buffer)
                                    mantemToken()
                                    buffer = ""
                                proxToken()
                                return CONTEUDO()
                            elif(linha != tuplas[0]):
                                if(errado):
                                    output(int(linha), "SyntaxError", buffer)
                                    mantemToken()
                                    buffer = ""
                                linha = tuplas[0]
                                return CONTEUDO()
                            else:            
                                errado = True
                                buffer = buffer + " " + tuplas[2]
                                proxToken()
                        if(int(linha)<10):
                            aux = "0"+linha
                            output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
                        else:    
                            output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
                        mantemToken()
                        return 0
                else:
                    output(int(linha), "SyntaxError", buffer)
                    mantemToken()
                    buffer = ""
                    return CONTEUDO()
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken()
            return 0 
        elif(dados[iterador][2] == '(' and linha == tuplas[0]):
            i = CHAMADAFUNCAO()  
            if(i==0): 
                if(tuplas[2]==";" and linha == tuplas[0]):
                    buffer = ""
                    chamada=""
                    proxToken() 
                    return CONTEUDO() 
                else:
                    output(int(linha), "SyntaxError", buffer)
                    mantemToken()
                    buffer = ""
                    return CONTEUDO() 
            else:    
                errado = False
                if(not(len(buffer)==0)):          
                    errado = True
                mantemToken()            
                while(tuplas[2]!="$"):
                    if(tuplas[2]=="}"):
                        if(errado):
                            output(int(linha), "SyntaxError", buffer)
                            mantemToken()
                            buffer = ""
                        proxToken()
                        return 0
                    elif(tuplas[2] == ";"):
                        buffer = buffer + " " + tuplas[2]
                        if(errado):
                            output(int(linha), "SyntaxError", buffer)
                            mantemToken()
                            buffer = ""
                        proxToken()
                        return CONTEUDO()
                    elif(linha != tuplas[0]):
                        if(errado):
                            output(int(linha), "SyntaxError", buffer)
                            mantemToken()
                            buffer = ""
                        linha = tuplas[0]
                        return CONTEUDO()
                    else:            
                        errado = True
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                if(int(linha)<10):
                    aux = "0"+linha
                    output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
                else:    
                    output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
                mantemToken()
                return 0
        elif(dados[iterador][2] == '=' and linha == tuplas[0]): #Consome IDE
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == '=' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()                
                i = EXPATRIBUICAOB()
                if(i==0): 
                    if(tuplas[2]==";" and linha == tuplas[0]):                        
                        if(atribu):
                            if(not(vetorial) and chamada==""):
                                if(fator): #and not(tipo == dados[iterador-2][1])):
                                    aux = dados[iterador-2][1]
                                    erronio= False
                                    if(aux == "CAD"):
                                        if(not(tipo == "cadeia")):
                                            erronio = True
                                    elif(aux == "CAR"):
                                        if(not(tipo == "char")):
                                            erronio = True
                                    elif(aux == "NRO"):
                                        aux = dados[iterador-2][2]
                                        x = aux.find(".")
                                        if(x<0):
                                            if(not(tipo == "inteiro")):
                                                erronio = True
                                        else:
                                            if(not(tipo == "real")):
                                                erronio = True
                                    elif(aux == "PRE"):
                                        if(not(tipo == "booleano")):
                                                erronio = True
                                    else:
                                        aux = dados[iterador-2][2]
                                        if(aux=="]"):
                                            aux = ide
                                        indicador = False
                                        i = 0
                                        for chave in range(len(tabela)):
                                            g = "IDE"+str(i)
                                            if(tabela[chave].get(g,"não foi")==aux):
                                                indicador = True
                                                if(not(tabela[chave].get("TIPO","não foi")==tipo)):
                                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                                    mantemToken()                                                   
                                            i=i+1
                                        if(not(indicador) and not(aux=="}")):
                                            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ aux)
                                            mantemToken()                        
                                    if(erronio):                                        
                                        output(int(linha), "SemanticoError", "Tipos diferentes")
                                        mantemToken()  
                                else:
                                    if(expressao): #and not(tipo == "booleano")):
                                        if(buffer.find("||")>0 or buffer.find("&&")>0 or buffer.find("==")>0 or buffer.find("!=")>0 or buffer.find(">=")>0 or buffer.find("<=")>0 or buffer.find("<")>0 or buffer.find(">")>0):
                                            if(tipo != "booleano"):
                                                output(int(linha), "SemanticoError", "Tipos diferentes")
                                                mantemToken()  
                                        else:
                                            if(not(tipo == "inteiro" or tipo == "real")):
                                                output(int(linha), "SemanticoError", "Tipos diferentes")
                                                mantemToken()
                                    #else:
                                        #print("É expressão aritmética ou chamada de função")
                            elif(not(chamada=="")):
                                if(tipo!=tipoChamada):
                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                    mantemToken()
                            chamada=""
                            vetorial = False
                            fator = True
                        buffer = ""
                        proxToken() 
                        return CONTEUDO() 
                    else:
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                        return CONTEUDO() 
                else:    
                    errado = False
                    if(not(len(buffer)==0)):          
                        errado = True
                    mantemToken()            
                    while(tuplas[2]!="$"):
                        if(tuplas[2]=="}"):
                            if(errado):
                                output(int(linha), "SyntaxError", buffer)
                                mantemToken()
                                buffer = ""
                            proxToken()
                            return 0
                        elif(tuplas[2] == ";"):
                            buffer = buffer + " " + tuplas[2]
                            if(errado):
                                output(int(linha), "SyntaxError", buffer)
                                mantemToken()
                                buffer = ""
                            proxToken()
                            return CONTEUDO()
                        elif(linha != tuplas[0]):
                            if(errado):
                                output(int(linha), "SyntaxError", buffer)
                                mantemToken()
                                buffer = ""
                            linha = tuplas[0]
                            return CONTEUDO()
                        else:            
                            errado = True
                            buffer = buffer + " " + tuplas[2]
                            proxToken()
                    if(int(linha)<10):
                        aux = "0"+linha
                        output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
                    else:    
                        output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
                    mantemToken()
                    return 0
            else:
                output(int(linha), "SyntaxError", buffer)
                mantemToken()
                buffer = ""
                return CONTEUDO()
        else:    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return CONTEUDO()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    linha = tuplas[0]
                    return CONTEUDO()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken()
            return 0  
    else:    
        errado = False
        if(not(len(buffer)==0)):          
            errado = True
        mantemToken()            
        while(tuplas[2]!="$"):
            if(tuplas[2]=="}"):
                if(errado):
                    output(int(linha), "SyntaxError", buffer)
                    mantemToken()
                    buffer = ""
                proxToken()
                return 0
            elif(tuplas[2] == ";"):
                buffer = buffer + " " + tuplas[2]
                if(errado):
                    output(int(linha), "SyntaxError", buffer)
                    mantemToken()
                    buffer = ""
                proxToken()
                return CONTEUDO()
            elif(linha != tuplas[0]):
                if(errado):
                    output(int(linha), "SyntaxError", buffer)
                    mantemToken()
                    buffer = ""
                #iterador = iterador-1
                linha = tuplas[0]
                return CONTEUDO()
            else:            
                errado = True
                buffer = buffer + " " + tuplas[2]
                proxToken()
        if(int(linha)<10):
            aux = "0"+linha
            output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
        else:    
            output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
        mantemToken()
        return 0
########################################### Escreva ######################################################

def ESCREVA():
    global tuplas, buffer, linha
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ESCONT()
        if(i == 0):
            if(tuplas[2] == ';'and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                return 0
            else:
                return 1
        else:
            return i
    else:
        return 1

def ESCONT():
    global tuplas, buffer, linha
    if(tuplas[1] == "IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ACESSOVAR()
        if(i == 0):
             i = ESFIM()
             return i
        else:
            return i
    if((tuplas[1] == "CAR" or tuplas[1] == "CAD") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ESFIM()
        return i
    else:
        return 1

def ESFIM():
    global tuplas, buffer, linha
    if(tuplas[2] == ")" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2] == "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ESCONT()
        return i
    else:
        return 1    

############################################# Leia ##############################################

def LEIA():
    global tuplas, buffer, linha, expressao, fator, vetorial
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = LEIACONT()
        if(i == 0):
            if(tuplas[2] == ';' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                expressao = False 
                fator = True 
                vetorial = False 
                return 0
            else:
                expressao = False 
                fator = True 
                vetorial = False 
                return 1
        else:
            expressao = False 
            fator = True 
            vetorial = False 
            return i
    else:
        return 1

def LEIACONT():
    global tuplas, buffer, linha
    if(tuplas[1] == "IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ACESSOVAR()
        if(i == 0):
             i = LEIAFIM()
             return i
        else:
            return i
    else:
        return 1

def LEIAFIM():
    global tuplas, buffer, linha
    if(tuplas[2] == ")" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2] == "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = LEIACONT()
        return i
    else:
        return 1

############################################## Se e Senao ######################################
def SE():
    global tuplas, buffer, linha, expressao, fator, vetorial
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = EXPRESSAOB()
        if(i == 0):
            if(tuplas[2] == ')' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tuplas[2] == '{'):
                    buffer = ""
                    proxToken()
                    expressao = False 
                    fator = True 
                    vetorial = False 
                    i = CONTEUDO()
                    if(i == 0):
                        return SENAO()
                    return i
                else:
                    expressao = False 
                    fator = True 
                    vetorial = False 
                    return 1    
            else:
                expressao = False 
                fator = True 
                vetorial = False 
                return 1
        else:
            expressao = False 
            fator = True 
            vetorial = False 
            return i
    else:
        return 1

def SENAO():
    global tuplas, buffer, linha, expressao, fator, vetorial
    if(tuplas[2] == 'senao'):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[2] == '{'):
            buffer = ""
            proxToken()
            expressao = False 
            fator = True 
            vetorial = False 
            return CONTEUDO()
        else:
            expressao = False 
            fator = True 
            vetorial = False 
            return 1    
    else:
        return 0
############################################## Enquanto ######################################
def ENQUANTO():
    global tuplas, buffer, linha, expressao, fator, vetorial
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = EXPRESSAOB()
        if(i == 0):
            if(tuplas[2] == ')' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tuplas[2] == '{'):
                    buffer = ""
                    proxToken()
                    expressao = False 
                    fator = True 
                    vetorial = False 
                    return CONTEUDO()
                else:
                    expressao = False 
                    fator = True 
                    vetorial = False 
                    return 1    
            else:
                expressao = False 
                fator = True 
                vetorial = False 
                return 1
        else:
            expressao = False 
            fator = True 
            vetorial = False 
            return i
    else:
        return 1

############################################## Para ######################################
def PARA():
    global tuplas, buffer, linha
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            i = ACESSOVAR()
            if(i==0):
                if(tuplas[2] == '=' and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    i = EXPATRIBUICAO()
                    if(i==0):
                        if(tuplas[2] == ';' and linha == tuplas[0]):
                            buffer = buffer + " " + tuplas[2]
                            proxToken()
                            return PARACONT()                            
                        else:
                            return 1
                    return i
                else:
                    return 1
            return i
        else:
            return 1
    else:
        return 1

def PARACONT():
    global tuplas, buffer, linha
    i = EXPRESSAOB()
    if(i==0):
        if(tuplas[2] == ';' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            return PARAFIM()        
        else:
            return 1
    else:
        return i

def PARAFIM():
    global tuplas, buffer, linha, expressao, fator, vetorial
    if(tuplas[1] == 'IDE' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ACESSOVAR()        
        if(i==0):
            if(tuplas[2] == '=' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = EXPRESSAOB()   
            else:
                i = EXPATRIBUICAOCONTB() 
            if(i == 0):
                if(tuplas[2] == ')' and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    if(tuplas[2] == '{'):
                        buffer = ""
                        proxToken()
                        expressao = False 
                        fator = True 
                        vetorial = False 
                        return CONTEUDO()
                    else:
                        expressao = False 
                        fator = True 
                        vetorial = False 
                        return 1    
                else:
                    expressao = False 
                    fator = True 
                    vetorial = False 
                    return 1
            else:
                expressao = False 
                fator = True 
                vetorial = False 
                return i
        else:
            return i
    else:
        return 1

############################################## Registro ######################################

def REGISTRO():
    global tuplas, buffer, iterador, linha, ide, tipo, escopo, regra, tabela, regis, dados
    if(tuplas[2]=="{"):
        buffer = buffer + " " + tuplas[2]
        ########## VERIFICA SEMANTICA ###########     
        frase = "IDE"+str(len(tabela))
        aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": "REG"}
        if(len(tabela)==0):
            tabela.append(aux)
        else:
            indicador = False
            i = 0
            for chave in range(len(tabela)):
                g = "IDE"+str(i)
                if(tabela[chave].get(g,"não foi")== aux.get(frase,"Não foi")):
                    indicador = True              
                i=i+1
            if(indicador):
                output(int(linha), "SemanticoError", "Identificador ja instanciado: "+ide)
                mantemToken()
            else:
                tabela.append(aux)
        #verificações
        regis = dados[iterador-2][2]
        proxToken()        
        i = VAR()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):      
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    tuplas[2] = "{"
                    return VARIAVEIS()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    #iterador = iterador-1
                    linha = tuplas[0]
                    tuplas[1] = "DEL"
                    tuplas[2] = "{"                    
                    return VARIAVEIS()
                else:               
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken() 
            return 0
        return i
    return 1

################################################# Acesso Var ######################################

def ACESSOVAR():
    global tuplas, buffer, linha, tabela, dados, iterador, tipo
    if(tuplas[2] == '.' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            i=0
            for chave in range(len(tabela)):
                g = "IDE"+str(i)
                if(tabela[chave].get(g,"não foi")==tuplas[2]):
                    if(not(tabela[chave].get("REGISTRO","não foi")==dados[iterador-3][2])):
                        aux = dados[iterador-3][2]
                        aux = aux+dados[iterador-2][2]
                        aux = aux+tuplas[2]
                        output(int(linha), "SemanticoError", "Erro de acesso: "+ aux)
                        mantemToken()
                    else:
                        tipo = tabela[chave].get("TIPO","não foi")
                i=i+1            
            proxToken()
            if(tuplas[2] == '[' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    if(tuplas[1] == 'IDE'):
                        indicador = False
                        i = 0
                        for chave in range(len(tabela)):
                            g = "IDE"+str(i)
                            if(tabela[chave].get(g,"não foi")== tuplas[2]):
                                indicador = True
                                aux = tabela[chave].get("TIPO","não foi")
                                if(not(aux=="inteiro")):
                                    output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                                    mantemToken()                                         
                            i=i+1
                        if(not(indicador)):                            
                            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                            mantemToken()
                    else:
                        x = tuplas[2].find(".")
                        if(x>=0):
                            output(int(linha), "SemanticoError", "Tipo diferente: real")
                            mantemToken()
                    proxToken()
                    if(tuplas[2] == ']' and linha == tuplas[0]):
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                        i = ACESSOVARCONT()
                        return i
                    else:
                        return 1
                else:
                    return 1
            return 0
        else:
            return 1
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(tuplas[1] == 'IDE'):
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== tuplas[2]):
                        indicador = True
                        aux = tabela[chave].get("TIPO","não foi")
                        if(not(aux=="inteiro")):
                            output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                            mantemToken()                                         
                    i=i+1
                if(not(indicador)):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                    mantemToken()
            else:
                x = tuplas[2].find(".")
                if(x>=0):
                    output(int(linha), "SemanticoError", "Tipo diferente: real")
                    mantemToken()
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = ACESSOVARCONT()
                return i
            else:
                return 1
        else:
            return 1
    return 0

def ACESSOVARCONT():
    global tuplas, buffer, linha, tabela
    if(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(tuplas[1] == 'IDE'):
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== tuplas[2]):
                        indicador = True
                        aux = tabela[chave].get("TIPO","não foi")
                        if(not(aux=="inteiro")):
                            output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                            mantemToken()                                         
                    i=i+1
                if(not(indicador)):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                    mantemToken()
            else:
                x = tuplas[2].find(".")
                if(x>=0):
                    output(int(linha), "SemanticoError", "Tipo diferente: real")
                    mantemToken()
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = ACESSOVARCONTB()
                return i
            else:
                return 1
        else:
            return 1
    return 0

def ACESSOVARCONTB():
    global tuplas, buffer, linha
    if(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(tuplas[1] == 'IDE'):
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== tuplas[2]):
                        indicador = True
                        aux = tabela[chave].get("TIPO","não foi")
                        if(not(aux=="inteiro")):
                            output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                            mantemToken()                                         
                    i=i+1
                if(not(indicador)):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                    mantemToken()
            else:
                x = tuplas[2].find(".")
                if(x>=0):
                    output(int(linha), "SemanticoError", "Tipo diferente: real")
                    mantemToken()
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tipo=="cadeia"):
                    output(int(linha), "SemanticoError", "Impossivel declarar uma matriz 3D do tipo cadeia")
                    mantemToken()
                return 0
            else:
                return 1
        else:
            return 1
    return 0

###################################### Função, Chamada de função e retorno ####################################  

def FUNCAO ():
    global tuplas, buffer, linha, dados, escopo, tipo, ide, tabela, iterador
    if(tuplas[2]=="vazio" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        tipo = tuplas[2]
        proxToken() 
        if(tuplas[1]=="IDE" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            ide = tuplas[2]
            proxToken()  
            return FUNCAOINIT()
    else:
        i = TIPOA()
        if(i==0): 
            tipo = dados[iterador-2][2]
            i = TIPOCONT()
            if(i==0): 
                if(tuplas[1]=="IDE" and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    ide = tuplas[2]
                    proxToken()  
                    return FUNCAOINIT()
                else:
                    return 1                
            return i
        return i

def FUNCAOINIT():
    global tuplas, buffer, linha, escopo, paran, tipo, ide, tabela, escopo, retorno, retornado
    if(tuplas[2]=="(" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()  
        i = PARANINIT()
        if(i==0): 
            if(tuplas[2] == '{'):
                buffer = ""
                # Fazer a adição da função na tabela
                proxToken()
                ########## VERIFICA SEMANTICA ###########  
                frase = "IDE"+str(len(tabela))
                aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": "funcao"}
                if(len(paran)>0):
                    aux.update({"ATRIBUTOS":paran})
                if(len(tabela)==0):
                    tabela.append(aux)
                    x = len(tabela)
                    for chave in range(len(paran)):
                        frase="IDE"+str(x)
                        if(not(chave==0)):
                            if(chave%2>0):
                                entrada=True
                                i=0
                                for y in range(len(tabela)):
                                    g = "IDE"+str(i)
                                    if(tabela[y].get(g,"não foi")==paran[chave]):
                                        entrada = False
                                    i=i+1
                                if(entrada):
                                    aux = {frase: paran[chave], "TIPO":  paran[chave-1], "ESCOPO": "funcao", "LINHA": linha, "REGRA": "VAR"}
                                    tabela.append(aux)
                                    x=x+1
                                else:
                                    output(int(linha), "SemanticoError", "Identificador do parametro ja existe: "+ paran[chave])
                                    mantemToken()
                else:
                    indicador = False
                    i = 0
                    for chave in range(len(tabela)):
                        g = "IDE"+str(i)
                        if(tabela[chave].get(g,"não foi")== aux.get(frase,"Não foi")):
                            if(tabela[chave].get("TIPO","não foi")== aux.get("TIPO","Não foi")):
                                g = tabela[chave].get("ATRIBUTOS","não foi")
                                if(len(g)==len(paran)):
                                    indicadorb = True
                                    for chave in range(len(g)):
                                        if(chave==0):
                                            if(not(g[chave]==paran[chave])):
                                                indicadorb = False
                                        elif(chave%2==0):
                                            if(not(g[chave]==paran[chave])):
                                                indicadorb = False
                                    if(indicadorb):
                                        indicador = True   
                            else:
                                g = tabela[chave].get("ATRIBUTOS","não foi")
                                if(len(g)==len(paran)):
                                    indicadorb = True
                                    for chave in range(len(g)):
                                        if(chave==0):
                                            if(not(g[chave]==paran[chave])):
                                                indicadorb = False
                                        elif(chave%2==0):
                                            if(not(g[chave]==paran[chave])):
                                                indicadorb = False
                                    if(indicadorb):
                                        indicador = True 
                                #indicador = True          
                        i=i+1
                    if(indicador):
                        output(int(linha), "SemanticoError", "Identificador ja instanciado: "+ide)
                        mantemToken()
                    else:
                        tabela.append(aux)
                        x = len(tabela)
                        for chave in range(len(paran)):
                            frase="IDE"+str(x)
                            if(not(chave==0)):
                                if(chave%2>0):
                                    entrada=True
                                    i=0
                                    for y in range(len(tabela)):
                                        g = "IDE"+str(i)
                                        if(tabela[y].get(g,"não foi")== paran[chave]):
                                            entrada = False
                                        i=i+1
                                    if(entrada):
                                        aux = {frase: paran[chave], "TIPO":  paran[chave-1], "ESCOPO": "funcao", "LINHA": linha, "REGRA": "VAR"}
                                        tabela.append(aux)
                                        x=x+1
                                    else:
                                        output(int(linha), "SemanticoError", "Identificador do parametro ja existe: "+ paran[chave])
                                        mantemToken()
                #verificações
                paran = []                
                # Fazer a comparação de função aqui com a tabela
                escopo = "funcao"
                if(not(tipo=="vazio")):
                    retorno = True
                    retornado = False
                else:
                    retorno = False
                    retornado = True
                return CONTEUDO()
            else:
                return 1               
        return i
    else:
        return 1
def TIPOCONT():
    global tuplas, buffer, linha
    if(tuplas[2]=="[" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()  
        if(tuplas[2]=="]" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()  
            return VETORMAIS()
        else:
            return 1
    else:
        return 0

def VETORMAIS():
    global tuplas, buffer, linha
    if(tuplas[2]=="[" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()  
        if(tuplas[2]=="]" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()  
            return VETORMAISUM()
        else:
            return 1
    else:
        return 0

def VETORMAISUM():
    global tuplas, buffer, linha
    if(tuplas[2]=="[" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()  
        if(tuplas[2]=="]" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()  
            return 0
        else:
            return 1
    else:
        return 0

def PARANINIT():
    global tuplas, buffer, linha, dados, paran, iterador
    if(tuplas[2]==")" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:    
        i = TIPOA()
        if(i==0): 
            paran.append(dados[iterador-2][2])
            if(tuplas[1]=="IDE" and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                paran.append(tuplas[2])
                proxToken()  
                if(tuplas[2]=="," and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()  
                    return PARANINIT()
                elif(tuplas[2]==")" and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()  
                    return 0
                else:
                    return 1
            else:
                return 1
        return i

def CHAMADAFUNCAO():
    global tuplas, buffer, linha, ide, chamada
    if(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        ide = tuplas[2]
        chamada=tuplas[2]
        proxToken()    
        if(tuplas[2]=="(" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken() 
            return PARAN()
    else:
        return 1
    
def PARAN():
    global tuplas, buffer, linha, ide, tabela, chamada, paran, tipoChamada
    if(tuplas[2]==")" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        indicador = False
        achouErro = False
        acertou = False
        i = 0
        for chave in range(len(tabela)):
            g = "IDE"+str(i)
            if(tabela[chave].get(g,"não foi")==ide):
                if(tabela[chave].get("REGRA","não foi")=="funcao"):
                    if(not(tabela[chave].get("ATRIBUTOS","m")=="m") and not(acertou)):
                        achouErro = True
                    else:
                        if(not(acertou)):
                            tipoChamada = tabela[chave].get("TIPO","não foi")
                        acertou = True
                        achouErro = False
                    indicador = True                                                  
            i=i+1
        if(achouErro):
            output(int(linha), "SemanticoError", "Quantidade de parametros diferentes")
            mantemToken()
        if(not(indicador)):
            output(int(linha), "SemanticoError", "Funcao nao instanciada: "+ ide)
            mantemToken()
        return 0   
    else:
        return PARANCONT()

def PARANCONT():
    global tuplas, buffer, linha, tabela, ide, chamada, paran, tabela, expressao, fator, vetorial, ideExp, dados, iterador, tipoChamada
    chamadaAux = chamada
    chamada = ""
    i = VALOR()
    if(not(vetorial) and chamada==""):
        if(fator): #and not(tipo == dados[iterador-2][1])):
            aux = dados[iterador-2][1]
            erronio= False
            if(aux == "CAD"):
                paran.append("cadeia")
            elif(aux == "CAR"):
                paran.append("char")
            elif(aux == "NRO"):
                aux = dados[iterador-2][2]
                x = aux.find(".")
                if(x<0):
                    paran.append("inteiro")
                else:
                    paran.append("real")
            elif(aux == "PRE"):
                paran.append("booleano")
            else:
                indicador = False
                y = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(y)
                    if(tabela[chave].get(g,"não foi")==ideExp):
                        indicador = True
                        paran.append(tabela[chave].get("TIPO","não foi"))                                                   
                    y=y+1
                if(not(indicador) and not(aux=="}")):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ ideExp)
                    mantemToken()                        
            if(erronio):
                output(int(linha), "SemanticoError", "Tipos diferentes")
                mantemToken()  
        else:
            if(expressao): #and not(tipo == "booleano")):
                if(buffer.find("||")>0 or buffer.find("&&")>0 or buffer.find("==")>0 or buffer.find("!=")>0 or buffer.find(">=")>0 or buffer.find("<=")>0 or buffer.find("<")>0 or buffer.find(">")>0):
                    paran.append("booleano") 
                else:
                    if(buffer.find(".")>0):
                        paran.append("real")
                    else:
                        paran.append("inteiro")
    elif(not(chamada=="")):
        output(int(linha), "SemanticoError", "Chamada de funcao dentro de chamada de funcao")
        mantemToken()
    vetorial = False
    fator = True
    expressao = False
    chamada = chamadaAux
    if(i==0): 
        if(tuplas[2]=="," and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken() 
            return PARANCONT()   
        elif(tuplas[2]==")" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken() 
            indicador = False
            i = 0
            achouErro = False
            achouMaisUmErro = False
            acertou = False
            for chave in range(len(tabela)):
                g = "IDE"+str(i)
                if(tabela[chave].get(g,"não foi")==ide):
                    if(tabela[chave].get("REGRA","não foi")=="funcao"):
                        if(not(tabela[chave].get("ATRIBUTOS","m")=="m")):
                            aux = tabela[chave].get("ATRIBUTOS","m")
                            if(len(paran)==len(aux)//2):
                                Taerrado = False
                                for x in range(len(paran)):
                                    if(not(paran[x]==aux[x+x]) and not(acertou)):
                                        Taerrado = True
                                if(Taerrado):
                                    achouMaisUmErro = True
                                else:
                                    if(not(acertou)):
                                        tipoChamada = tabela[chave].get("TIPO","não foi")
                                    acertou=True
                                    achouErro=False
                                    achouMaisUmErro = False
                                    indicador = True
                            else:
                                if(not(acertou)):
                                    achouErro = True
                        indicador = True    
                i=i+1
            paran=[]
            if(achouErro):
                output(int(linha), "SemanticoError", "Quantidade de parametros diferentes")
                mantemToken()
            if(achouMaisUmErro):
                output(int(linha), "SemanticoError", "Parametros com tipos diferentes")
                mantemToken()
            if(not(indicador)):
                output(int(linha), "SemanticoError", "Funcao nao instanciada: "+ ide)
                mantemToken()
            return 0  
        else:            
            return 1
    else:
        return 1

def RETORNO():
    global tuplas, buffer, linha, retorno, retornado, expressao, fator, vetorial, chamada, linha, tabela, tipo, dados, iterador, tipoChamada
    i = VALOR()
    if(i==0): 
        if(tuplas[2]==";" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(retorno):
                retornado = True
                i = len(tabela)-1
                primeiro = True
                for chave in reversed(range(len(tabela))):
                    g = "IDE"+str(i)
                    if(tabela[chave].get("REGRA","não foi")=="funcao" and primeiro):
                        primeiro = False
                        testando = tabela[chave].get(g,"não foi")                                               
                        tipo = tabela[chave].get("TIPO","não foi")
                    i=i-1
                Nerrou = True
                #possivel erro
                if(testando == dados[iterador-2][2]):
                    output(int(linha), "SemanticoError", "Impossivel retornar identificador da funcao")
                    mantemToken()  
                    Nerrou = False
                if(not(vetorial) and chamada=="" and Nerrou):
                    if(fator): #and not(tipo == dados[iterador-2][1])):
                        aux = dados[iterador-2][1]
                        erronio= False
                        if(aux == "CAD"):
                            if(not(tipo == "cadeia")):
                                erronio = True
                        elif(aux == "CAR"):
                            if(not(tipo == "char")):
                                erronio = True
                        elif(aux == "NRO"):
                            aux = dados[iterador-2][2]
                            x = aux.find(".")
                            if(x<0):
                                if(not(tipo == "inteiro")):
                                    erronio = True
                            else:
                                if(not(tipo == "real")):
                                    erronio = True
                        elif(aux == "PRE"):
                            if(not(tipo == "booleano")):
                                    erronio = True
                        else:
                            #aux = dados[iterador-2][2]
                            indicador = False
                            i = 0
                            for chave in range(len(tabela)):
                                g = "IDE"+str(i)
                                if(tabela[chave].get(g,"não foi")==ideExp):
                                    indicador = True
                                    if(not(tabela[chave].get("TIPO","não foi")==tipo)):
                                        output(int(linha), "SemanticoError", "Tipos diferentes")
                                        mantemToken()                                                   
                                i=i+1
                            if(not(indicador) and not(aux=="}") and not(aux=="]")):
                                output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ ideExp)
                                mantemToken()                        
                        if(erronio):
                            output(int(linha), "SemanticoError", "Tipos diferentes")
                            mantemToken()  
                    else:
                        if(expressao): #and not(tipo == "booleano")):
                            if(buffer.find("||")>0 or buffer.find("&&")>0 or buffer.find("==")>0 or buffer.find("!=")>0 or buffer.find(">=")>0 or buffer.find("<=")>0 or buffer.find("<")>0 or buffer.find(">")>0):
                                if(tipo != "booleano"):
                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                    mantemToken()  
                            else:
                                if(not(tipo == "inteiro" or tipo == "real")):
                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                    mantemToken() 
                        #else:
                        #   print("É expressão aritmética ou chamada de função")
                elif(not(chamada=="")):
                    if(tipo!=tipoChamada):
                        output(int(linha), "SemanticoError", "Tipos diferentes")
                        mantemToken()
                vetorial = False
                fator = True
                expressao = False
            else:
                output(int(linha), "SemanticoError", "Funcao vazio com retorno")
                mantemToken()
            proxToken() 
            return 0 
        else:
            return 1
    return i

########################################## Constantes e Variaveis #######################################

def CONSTANTES():
    global tuplas, buffer, linha, iterador, regra, chamada, expressao, fator, vetorial
    fator = True
    vetorial = False
    expressao = False
    chamada=""
    regra = "CONST"
    if(tuplas[2]=="{"):
        buffer = buffer + " " + tuplas[2]
        proxToken()    
        i = CONST()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):          
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    tuplas[2] = "{"
                    return CONSTANTES()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    #iterador = iterador-1
                    linha = tuplas[0]
                    tuplas[1] = "DEL"
                    tuplas[2] = "{"
                    return CONSTANTES()
                else:            
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken()
        return i
    return 1

def CONST():
    global tuplas, buffer, linha
    buffer = ""
    linha = tuplas[0]
    i = TIPO()
    if(i==0):
        return CONSTALT()
    else:
        return i

def CONSTCONT(): 
    global tuplas, buffer, chamada, tabela, ide, tipo, escopo, linha, regra
    if(tuplas[2]== "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        ########## VERIFICA SEMANTICA ###########  
        if(chamada==""):
            frase = "IDE"+str(len(tabela))
            aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": regra}
            if(len(tabela)==0):
                tabela.append(aux)
            else:
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== aux.get(frase,"Não foi")):
                        indicador = True             
                    i=i+1
                if(indicador):
                    output(int(linha), "SemanticoError", "Identificador ja instanciado: "+ide)
                    mantemToken()
                else:
                    tabela.append(aux)
        else:
            chamada=""
        #verificações
        return CONSTALT()
    elif(tuplas[2]== ";" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        ########## VERIFICA SEMANTICA ###########  
        if(chamada==""):
            frase = "IDE"+str(len(tabela))
            aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": regra}
            if(len(tabela)==0):
                tabela.append(aux)
            else:
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== aux.get(frase,"Não foi")):
                        indicador = True          
                    i=i+1
                if(indicador):
                    output(int(linha), "SemanticoError", "Identificador ja instanciado: "+ide)
                    mantemToken()
                else:
                    tabela.append(aux)
        else:
            chamada=""
        #verificações
        return CONSTFIM()
    else:
        return 1

def CONSTALT():
    global tuplas, buffer, linha, ide, expressao, fator, tipo, iterador, dados, vetorial, chamada, tabela
    fator = True
    if(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        ide = tuplas[2]
        proxToken()
        i = VARINIT()
        if(i == 0):
            if(not(vetorial) and chamada==""):
                if(fator): #and not(tipo == dados[iterador-2][1])):
                    aux = dados[iterador-2][1]
                    erronio= False
                    if(aux == "CAD"):
                        if(not(tipo == "cadeia")):
                            erronio = True
                    elif(aux == "CAR"):
                        if(not(tipo == "char")):
                            erronio = True
                    elif(aux == "NRO"):
                        aux = dados[iterador-2][2]
                        x = aux.find(".")
                        if(x<0):
                            if(not(tipo == "inteiro")):
                                erronio = True
                        else:
                            if(not(tipo == "real")):
                                erronio = True
                    elif(aux == "PRE"):
                        if(not(tipo == "booleano")):
                                erronio = True
                    else:
                        aux = dados[iterador-2][2]
                        indicador = False
                        i = 0
                        for chave in range(len(tabela)):
                            g = "IDE"+str(i)
                            if(tabela[chave].get(g,"não foi")==aux):
                                indicador = True
                                if(not(tabela[chave].get("TIPO","não foi")==tipo)):
                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                    mantemToken()                                                   
                            i=i+1
                        if(not(indicador) and not(aux=="}") and not(aux=="]")):
                            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ aux)
                            mantemToken()                        
                    if(erronio):
                        output(int(linha), "SemanticoError", "Tipos diferentes")
                        mantemToken()  
                else:
                    output(int(linha), "SemanticoError", "O valor deve ser explicito e com um so fator")
                    mantemToken()
            elif(not(chamada=="")):
                output(int(linha), "SemanticoError", "O valor deve ser explicito e com um so fator")
                mantemToken()
            vetorial = False
            fator = True
            return CONSTCONT()
        else:
            return i
    else:
        return 1 

def CONSTFIM():
    global tuplas, buffer
    if(tuplas[2]=="}"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:
        return CONST()

def VARIAVEIS():
    global tuplas, buffer, iterador, linha, regra, chamada, expressao, fator, vetorial
    fator = True
    vetorial = False
    expressao = False
    chamada=""    
    regra = "VAR"
    if(tuplas[2]=="{"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = VAR()
        if(i == 1):    
            errado = False
            if(not(len(buffer)==0)):      
                errado = True
            mantemToken()            
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    proxToken()
                    return 0
                elif(tuplas[2] == ";"):
                    buffer = buffer + " " + tuplas[2]
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    tuplas[2] = "{"
                    return VARIAVEIS()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "SyntaxError", buffer)
                        mantemToken()
                        buffer = ""
                    #iterador = iterador-1
                    linha = tuplas[0]
                    tuplas[1] = "DEL"
                    tuplas[2] = "{"                    
                    return VARIAVEIS()
                else:               
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
            if(int(linha)<10):
                aux = "0"+linha
                output(int(aux), "SyntaxError", "Fim do arquivo / falta o '}'")
            else:    
                output(int(linha), "SyntaxError", "Fim do arquivo / falta o '}'")
            mantemToken()
        return i
    return 1

def VAR():
    global tuplas, buffer, linha
    buffer = ""
    linha = tuplas[0]
    i = TIPO()
    if(i==0):
        return VARALT()
    else:
        return i

def VARALT():
    global tuplas, buffer, linha, ide
    if(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        ide = tuplas[2]
        proxToken()
        i = VARCONT()
        return i
    else:
        return 1 

def VARCONT():
    global tuplas, buffer, expressao, fator, vetorial, chamada,linha, ultipo, tipoChamada, errosSeman
    fator = True
    if(tuplas[2]== "," or tuplas[2]== ";"): #Conjunto first
        return VARFINAL()        
    else:
        i = VARINIT()        
        if(i == 0):
            if(not(vetorial) and chamada==""):
                if(fator): #and not(tipo == dados[iterador-2][1])):
                    aux = dados[iterador-2][1]
                    erronio= False
                    if(aux == "CAD"):
                        if(not(tipo == "cadeia")):
                            erronio = True
                    elif(aux == "CAR"):
                        if(not(tipo == "char")):
                            erronio = True
                    elif(aux == "NRO"):
                        aux = dados[iterador-2][2]
                        x = aux.find(".")
                        if(x<0):
                            if(not(tipo == "inteiro")):
                                erronio = True
                        else:
                            if(not(tipo == "real")):
                                erronio = True
                    elif(aux == "PRE"):
                        if(not(tipo == "booleano")):
                                erronio = True
                    else:
                        aux = dados[iterador-2][2]
                        indicador = False
                        i = 0
                        for chave in range(len(tabela)):
                            g = "IDE"+str(i)
                            if(tabela[chave].get(g,"não foi")==aux):
                                indicador = True
                                if(not(tabela[chave].get("TIPO","não foi")==tipo)):
                                    output(int(linha), "SemanticoError", "Tipos diferentes")
                                    mantemToken()                                                   
                            i=i+1
                        if(not(indicador) and not(aux=="}") and not(aux=="]")):
                            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ aux)
                            mantemToken()             
                    if(erronio):
                        output(int(linha), "SemanticoError", "Tipos diferentes")
                        mantemToken()  
                else:
                    if(expressao): #and not(tipo == "booleano")):
                        if(buffer.find("||")>0 or buffer.find("&&")>0 or buffer.find("==")>0 or buffer.find("!=")>0 or buffer.find(">=")>0 or buffer.find("<=")>0 or buffer.find("<")>0 or buffer.find(">")>0):
                            if(tipo != "booleano"):
                                output(int(linha), "SemanticoError", "Tipos diferentes")
                                mantemToken()  
                        else:
                            if(not(tipo == "inteiro" or tipo == "real")):
                                output(int(linha), "SemanticoError", "Tipos diferentes")
                                mantemToken()                    
            elif(not(chamada=="")):
                if(tipo!=tipoChamada):
                    output(int(linha), "SemanticoError", "Tipos diferentes")
                    mantemToken()
            vetorial = False
            fator = True
            expressao = False
            return VARFINAL()
        else:
            return i
        
def VARFINAL():
    global tuplas, buffer, linha, ide, tipo, escopo, regra, tabela, chamada, regis
    if(tuplas[2]== "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        ########## VERIFICA SEMANTICA ###########  
        if(chamada==""):
            frase = "IDE"+str(len(tabela))
            if(regis==""):
                aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": regra}
            else:
                aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": regra, "REGISTRO": regis}
            if(len(tabela)==0):
                tabela.append(aux)
            else:
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== aux.get(frase,"Não foi")):
                        indicador = True            
                    i=i+1
                if(indicador):
                    output(int(linha), "SemanticoError", "Identificador ja instanciado: "+ide)
                    mantemToken()
                else:
                    tabela.append(aux)
        else:
            chamada=""
        #verificações
        return VARALT()
    elif(tuplas[2]== ";" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        ########## VERIFICA SEMANTICA ###########    
        if(chamada==""):
            frase = "IDE"+str(len(tabela))
            if(regis==""):
                aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": regra}
            else:
                aux = {frase: ide, "TIPO": tipo, "ESCOPO": escopo, "LINHA": linha, "REGRA": regra, "REGISTRO": regis}
            if(len(tabela)==0):
                tabela.append(aux)
            else:
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== aux.get(frase,"Não foi")):
                        indicador = True            
                    i=i+1
                if(indicador):
                    output(int(linha), "SemanticoError", "Identificador ja instanciado: "+ide)
                    mantemToken()
                else:
                    tabela.append(aux)
        else:
            chamada=""
        #verificações
        return VARFIM()
    else:
        return 1

def VARFIM():
    global tuplas, buffer
    if(tuplas[2]=="}"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:
        return VAR()

def TIPO():
    global tuplas, buffer, linha, tipo
    if((tuplas[2]== "inteiro" or tuplas[2]=="real" or tuplas[2]=="booleano" or tuplas[2]=="cadeia" or tuplas[2]=="char") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        tipo = tuplas[2]
        proxToken()
        return 0
    else:    
        return 1

def TIPOA():
    global tuplas, buffer, linha
    if((tuplas[2]== "inteiro" or tuplas[2]=="real" or tuplas[2]=="booleano" or tuplas[2]=="cadeia" or tuplas[2]=="char" or tuplas[2]=="registro") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:    
        return 1

def VARINIT():
    global tuplas, buffer, linha, tabela, veterror
    if(tuplas[2] == '=' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return VALOR()
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(tuplas[1] == 'IDE'):
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== tuplas[2]):
                        indicador = True
                        aux = tabela[chave].get("TIPO","não foi")
                        if(not(aux=="inteiro")):
                            output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                            mantemToken()                                         
                    i=i+1
                if(not(indicador)):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                    mantemToken()
            else:
                x = tuplas[2].find(".")
                if(x>=0):
                    output(int(linha), "SemanticoError", "Tipo diferente: real")
                    mantemToken()   
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = VARINITCONT()
                veterror = True
                return i
            else:
                return 1
        else:
            return 1
    return 0

def VARINITCONT():
    global tuplas, buffer, linha, tabela, veterror
    if(tuplas[2] == '=' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[2] == '{' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            return VETOR()
        else:
            return 1 
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(tuplas[1] == 'IDE'):
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== tuplas[2]):
                        indicador = True
                        aux = tabela[chave].get("TIPO","não foi")
                        if(not(aux=="inteiro")):
                            output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                            mantemToken()                                         
                    i=i+1
                if(not(indicador)):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                    mantemToken()
            else:
                x = tuplas[2].find(".")
                if(x>=0):
                    output(int(linha), "SemanticoError", "Tipo diferente: real")
                    mantemToken()  
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = VARINITCONTMATR()
                veterror = True
                return i
            else:
                return 1
        else:
            return 1
    return 0

def VARINITCONTMATR():
    global tuplas, buffer, linha, tabela, tipo, veterror
    if(tuplas[2] == '=' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[2] == '{' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            i = VETOR()
            veterror = True
            if(tuplas[2] == ',' and i ==0 and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tuplas[2] == '{'):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    return VETOR()
                else:
                    return 1 
            else:
                return 1 
        else:
            return 1 
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if((tuplas[1] == 'NRO' or tuplas[1] == 'IDE') and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(tuplas[1] == 'IDE'):
                indicador = False
                i = 0
                for chave in range(len(tabela)):
                    g = "IDE"+str(i)
                    if(tabela[chave].get(g,"não foi")== tuplas[2]):
                        indicador = True
                        aux = tabela[chave].get("TIPO","não foi")
                        if(not(aux=="inteiro")):
                            output(int(linha), "SemanticoError", "Tipo diferente: "+aux)
                            mantemToken()                                         
                    i=i+1
                if(not(indicador)):
                    output(int(linha), "SemanticoError", "Identificador nao instanciado: "+tuplas[2])
                    mantemToken()
            else:
                x = tuplas[2].find(".")
                if(x>=0):
                    output(int(linha), "SemanticoError", "Tipo diferente: real")
                    mantemToken()  
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tipo=="cadeia"):
                    output(int(linha), "SemanticoError", "Impossivel declarar uma matriz 3D do tipo cadeia")
                    mantemToken()
                if(tuplas[2] == '=' and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    if(tuplas[2] == '{' and linha == tuplas[0]):
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                        i = VETOR()
                        veterror = True
                        if(tuplas[2] == ',' and i ==0 and linha == tuplas[0]):
                            buffer = buffer + " " + tuplas[2]
                            proxToken()
                            if(tuplas[2] == '{' and linha == tuplas[0]):
                                buffer = buffer + " " + tuplas[2]
                                proxToken()
                                i = VETOR()
                                veterror = True
                                if(tuplas[2] == ',' and i ==0 and linha == tuplas[0]):
                                    buffer = buffer + " " + tuplas[2]
                                    proxToken()
                                    if(tuplas[2] == '{' and linha == tuplas[0]):
                                        buffer = buffer + " " + tuplas[2]
                                        proxToken()
                                        return VETOR()
                                    else:
                                        return 1 
                                else:
                                    return 1 
                            else:
                                return 1 
                        else:
                            return 1 
                    else:
                        return 1 
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    return 0
def VETOR():
    global tuplas, buffer, expressao, fator, vetorial, tipo, chamada,linha, veterror
    vetorial = True
    fator = True
    i = VALOR()
    if(i == 0):
        #print(tuplas)
        if(not(tuplas[2]=="}") and veterror):
            if(fator and chamada==""): #and not(tipo == dados[iterador-2][1])):
                aux = dados[iterador-2][1]
                erronio= False
                if(aux == "CAD"):
                    if(not(tipo == "cadeia")):
                        erronio = True
                elif(aux == "CAR"):
                    if(not(tipo == "char")):
                        erronio = True
                elif(aux == "NRO"):
                    aux = dados[iterador-2][2]
                    x = aux.find(".")
                    if(x<0):
                        if(not(tipo == "inteiro")):
                            erronio = True
                    else:
                        if(not(tipo == "real")):
                            erronio = True
                elif(aux == "PRE"):
                    if(not(tipo == "booleano")):
                            erronio = True
                else:
                    aux = dados[iterador-2][2]
                    indicador = False
                    i = 0
                    for chave in range(len(tabela)):
                        g = "IDE"+str(i)
                        if(tabela[chave].get(g,"não foi")==aux):
                            indicador = True
                            if(not(tabela[chave].get("TIPO","não foi")==tipo)):
                                output(int(linha), "SemanticoError", "Tipos diferentes, lexema: " + aux)
                                mantemToken()                                                   
                        i=i+1
                    if(not(indicador)):
                        output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ aux)
                        mantemToken()                        
                if(erronio):
                    output(int(linha), "SemanticoError", "Tipos diferentes, lexema: " + aux)
                    mantemToken()  
            elif(not(chamada=="")):
                output(int(linha), "SemanticoError", "O valor deve ser explicito e com um so fator")
                mantemToken()
            veterror = False
        chamada=""
        vetorial = False
        fator = True
        return VETORCONT()
    return 1

def VETORCONT():
    global tuplas, buffer, linha, veterror
    if(tuplas[2]=="}" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        veterror = True
        return 0
    elif(tuplas[2]=="," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return VETOR()
    else:
        return 1
    
def VALOR():
    global tuplas, buffer, linha, iterador, dados,chamada
    #if(tuplas[1]== "NRO" or tuplas[1]=="IDE" or tuplas[1]=="CAR" or tuplas[1]=="CAD" or tuplas[2]=="verdadeiro" or tuplas[2]=="falso" and linha == tuplas[0]):
    if((tuplas[1]=="CAR" or tuplas[1]=="CAD") and linha == tuplas[0]):
        #buffer = buffer + " " + tuplas[2]
        #proxToken()
        return EXPRESSAOB()#0
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        if(dados[iterador][2] == "("):
            chamada = tuplas[2]
            return CHAMADAFUNCAO()
        else:
            return EXPRESSAOB()
    elif((tuplas[1]== "NRO" or tuplas[2]=="verdadeiro" or tuplas[2]=="falso" or tuplas[2]=="(" or tuplas[2]=="-" or tuplas[2]=="!") and linha == tuplas[0]):
        return EXPRESSAOB()
    return 1

def NEGATIVO():
    global tuplas, buffer, linha, ultipo, verifexpress, fator, algeb
    if(tuplas[1]== "NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo=="real")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        proxToken()
        return 0
    elif(tuplas[1]== "IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                if(tabela[chave].get("TIPO","não foi")=="inteiro" or tabela[chave].get("TIPO","não foi")=="real"):
                    sup = tabela[chave].get("TIPO","não foi")
                    if(not(fator) and verifexpress):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo=="real") and (sup=="inteiro"or sup=="real")):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    ultipo = tabela[chave].get("TIPO","não foi")
                else:
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Tipo diferente de inteiro ou real")
                    mantemToken() 
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken() 
        proxToken()
        return ACESSOVAR()
    return 1

############################################ EXPRESSOES ####################################################
def EXPREXC():
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, dentroParen, bufferExpressao, expressao, fator
    if((tuplas[2]=="verdadeiro" or tuplas[2]=="falso") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        ultipo = "booleano"
        proxToken()
        return EXPRESSAOCONTB()
    elif(tuplas[2]=="(" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        # Guardar flags e "zerar" elas
        ultipoAux = ultipo
        expressaoAux = expressao 
        fatorAux = fator
        algebAux = algeb        
        expressao = False 
        fator = True 
        algeb = "" 
        ultipo = "" 
        dentroParen = True
        bufferExpressao = ""
        i = EXPRESSAOB()
        k = bufferExpressao.find("+-*/")
        if(bufferExpressao.find("||")>0 or bufferExpressao.find("&&")>0 or bufferExpressao.find("==")>0 or bufferExpressao.find("!=")>0 or bufferExpressao.find(">=")>0 or bufferExpressao.find("<=")>0 or bufferExpressao.find("<")>0 or bufferExpressao.find(">")>0):
            ultipo = "booleano"
        dentroParen = False
        bufferExpressao = ""
        if(i==0):
            if(tuplas[2]==")" and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                expressao = True #expressaoAux
                #fator = fatorAux
                algeb = algebAux  
                # Volta flags guardadas
                if(not(algeb=="")):
                    if((dados[iterador-1][2]==")" or dados[iterador-1][2]==";") and verifexpress):
                        if((algeb=="rel" or algeb=="ari") and ultipo!="booleano"): #and ultipo=="inteiro" or ultipo == "real" and ultipoAux=="inteiro" or ultipoAux=="real"):
                            verifexpress = True
                        elif(algeb=="rll" and ultipo==ultipoAux):
                            verifexpress = True
                        elif(algeb=="rll" and (ultipo=="inteiro" or ultipo=="real") and (ultipoAux=="real" or ultipoAux=="inteiro")):
                            verifexpress = True
                        elif(algeb=="log" and ultipo=="booleano" and ultipo==ultipoAux):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                return EXPRESSAOCONTB()
            else:
                return 1
        return i
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                if(tabela[chave].get("TIPO","não foi")=="booleano"):
                    ultipo = tabela[chave].get("TIPO","não foi")
                else:
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Tipo diferente de booleano")
                    mantemToken() 
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            return EXPRESSAOCONTB()
        return i
    else:
        return 1

def EXPRESSAOCONTB():
    global tuplas, buffer, linha, fator, expressao, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    if((tuplas[2]=="&&" or tuplas[2]=="||" or tuplas[2]=="==" or tuplas[2]=="!=" or tuplas[2]=="<=" or tuplas[2]==">=" or tuplas[2]=="<" or tuplas[2]==">") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        if(verifexpress):
            if(algeb==""):
                if((tuplas[2]=="&&" or tuplas[2]=="||") and ultipo=="booleano"):
                    verifexpress = True
                elif(tuplas[2]=="==" or tuplas[2]=="!="):
                    verifexpress = True
                elif((tuplas[2]=="<=" or tuplas[2]==">=" or tuplas[2]=="<" or tuplas[2]==">") and (ultipo == "inteiro" or ultipo == "real")):
                    verifexpress = True
                else:
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                    mantemToken()
            else:
                if((tuplas[2]=="&&" or tuplas[2]=="||") and not(algeb=="ari")):
                    ultipo="booleano"
                    verifexpress = True
                elif(tuplas[2]=="==" or tuplas[2]=="!="):
                    if(algeb=="rel" or algeb=="rll"): #or algeb=="log"):
                        ultipo="booleano" 
                    verifexpress = True
                elif((tuplas[2]=="<=" or tuplas[2]==">=" or tuplas[2]=="<" or tuplas[2]==">") and (ultipo == "inteiro" or ultipo == "real") and not(algeb=="ari") and not(algeb=="rel")):
                    verifexpress = True
                else:
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                    mantemToken()
        if(tuplas[2]=="&&" or tuplas[2]=="||"):
            algeb = "log"
        elif(tuplas[2]=="==" or tuplas[2]=="!="):
            algeb = "rll"
        else:
            algeb = "rel"
        proxToken()
        fator = False
        expressao = True
        return EXPRESSAOB()
    else:
        return 0

def EXPRESSAOB():
    global tuplas, buffer, linha, expressao, fator, ideExp, algeb, ultipo, verifexpress, bufferExpressao, dentroParen, bufferExpressao, dados, iterador
    if((tuplas[2]=="verdadeiro" or tuplas[2]=="falso") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        if(not(fator) and verifexpress):
            if(algeb=="log" or algeb=="rll"):
                if((dados[iterador][2]==")" or dados[iterador][2]==";") and ultipo!="booleano"):
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                    mantemToken()
                else:
                    verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        ultipo = "booleano"
        return EXPRESSAOCONTB()
    elif(tuplas[2]=="(" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        # Guardar flags e "zerar" elas
        ultipoAux = ultipo
        expressaoAux = expressao 
        fatorAux = fator
        algebAux = algeb        
        expressao = False 
        fator = True 
        algeb = "" 
        ultipo = "" 
        dentroParen = True
        bufferExpressao = ""
        i = EXPRESSAOB()
        if(bufferExpressao.find("||")>0 or bufferExpressao.find("&&")>0 or bufferExpressao.find("==")>0 or bufferExpressao.find("!=")>0 or bufferExpressao.find(">=")>0 or bufferExpressao.find("<=")>0 or bufferExpressao.find("<")>0 or bufferExpressao.find(">")>0):
            ultipo = "booleano"
        dentroParen = False
        bufferExpressao = ""
        if(i==0):
            if(tuplas[2]==")" and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()           
                expressao = True #expressaoAux
                #fator = fatorAux
                algeb = algebAux            
                #ultipo = ultipoAux   
                # Volta flags guardadas
                if(not(algeb=="")):
                    if((dados[iterador-1][2]==")" or dados[iterador-1][2]==";") and verifexpress):
                        if((algeb=="rel" or algeb=="ari") and ultipo!="booleano"): #and ultipo=="inteiro" or ultipo == "real" and ultipoAux=="inteiro" or ultipoAux=="real"):
                            verifexpress = True
                        elif(algeb=="rll" and ultipo==ultipoAux):
                            verifexpress = True
                        elif(algeb=="rll" and (ultipo=="inteiro" or ultipo=="real") and (ultipoAux=="real" or ultipoAux=="inteiro")):
                            verifexpress = True
                        elif(algeb=="log" and ultipo=="booleano" and ultipo==ultipoAux):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                return EXPRESSAOCONTB()
            else:
                return 1
        return i
    elif(tuplas[2]=="!" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        return EXPREXC()
    elif(tuplas[2]=="-" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        i = NEGATIVO()
        if(i==0):
            if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
                #algeb = "ari"
                fator = False
                i = EXPARITMETICACONT()
                if(i==0):
                    return EXPRESSAOCONTB()
                else:
                    return i
            else:
                return EXPRESSAOCONTB()
        return i        
    elif(tuplas[1]=="NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo=="real") and (chave == "real" or chave=="inteiro")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        proxToken()
        if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
            fator = False
            i = EXPARITMETICACONT()
            if(i==0):
                return EXPRESSAOCONTB()
            else:
                return i
        else:            
            return EXPRESSAOCONTB()
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        ideExp = tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                sup = tabela[chave].get("TIPO","não foi")
                if(not(fator) and verifexpress):
                    if(sup=="inteiro" or sup=="real"):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo=="real")):
                            verifexpress = True 
                        elif(algeb=="log"):
                            if(dados[iterador][2]==")" or dados[iterador][2]==";"):   
                                verifexpress = False
                                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                                mantemToken()
                            else:
                                verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    elif(sup=="booleano"):
                        if(dados[iterador][2]==")" or dados[iterador][2]==";"):
                            if((algeb=="log" or algeb=="rll") and ultipo=="booleano"):
                                verifexpress = True
                            else:
                                verifexpress = False
                                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                                mantemToken()
                        elif(algeb=="log"):
                            verifexpress = True
                        elif(algeb=="rll" and ultipo=="booleano"):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    elif(sup=="cadeia"):
                        if(algeb=="rll" and ultipo=="cadeia"):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    elif(sup=="char"):
                        if(algeb=="rll" and ultipo=="char"):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    else:
                        verifexpress = False
                        output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                        mantemToken()
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken() 
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
                fator = False
                i = EXPARITMETICACONT()
                if(i==0):
                    return EXPRESSAOCONTB()
                else:
                    return i
            else:
                return EXPRESSAOCONTB()
        return i
    elif((tuplas[1]=="CAD" or tuplas[1]=="CAR") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        if(not(fator) and verifexpress):
            if(tuplas[1]=="CAD"):
                if(algeb=="rll" and ultipo=="cadeia"):
                    verifexpress = True
                else:
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                    mantemToken()
            else:
                if(algeb=="rll" and ultipo=="char"):
                    verifexpress = True
                else:
                    verifexpress = False
                    output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                    mantemToken()
        if(tuplas[1]=="CAD"):
            ultipo = "cadeia"
        else:
            ultipo = "char"
        proxToken()
        return EXPRESSAOCONTB()
    else:
        return 1

def EXPARITMETICA():
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, fator, dentroParen, bufferExpressao
    if(tuplas[2]=="(" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        #FAZER A VERIFICAÇÃO QUANDO ENTRA EM PARENTESES NA EXPRESSAO ARITIMETICA
        return EXPARITMETICAPAREN()
    elif(tuplas[2]=="-" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        i = NEGATIVO()
        if(i==0):
            return EXPARITMETICACONT()
        return i        
    elif(tuplas[1]=="NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real") and (chave=="inteiro" or chave=="real")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        proxToken()
        return EXPARITMETICACONT()
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                sup = tabela[chave].get("TIPO","não foi")
                if(not(fator) and verifexpress):
                    if(sup=="inteiro" or sup=="real"):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo=="real")):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    else:
                        verifexpress = False
                        output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                        mantemToken()
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken() 
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            return EXPARITMETICACONT()
        return i
    else:
        return 1

def EXPARITMETICAPAREN():
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, fator, dentroParen, bufferExpressao
    if(tuplas[1]=="NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real") and (chave=="inteiro" or chave=="real")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        proxToken()
        if(tuplas[2]==")" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(dentroParen):
                bufferExpressao = bufferExpressao + tuplas[2]
            proxToken()
            return EXPARITMETICACONTB()
        else:
            i = EXPARITMETICACONT()
            if(i==0):
                if(tuplas[2]==")" and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    return EXPARITMETICACONTB()
                else:
                    return 1
            return i
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                sup = tabela[chave].get("TIPO","não foi")
                if(not(fator) and verifexpress):
                    if(sup=="inteiro" or sup=="real"):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real")):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    else:
                        verifexpress = False
                        output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                        mantemToken()
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            if(tuplas[2]==")" and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                return EXPARITMETICACONTB()
            else:
                i = EXPARITMETICACONT()
                if(i==0):
                    if(tuplas[2]==")" and linha == tuplas[0]):
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                        return EXPARITMETICACONTB()
                    else:
                        return 1
                return i
        return i
    else:
        return 1

def EXPARITMETICACONT():
    global tuplas, buffer, linha, fator, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        if(verifexpress):
            if(ultipo=="inteiro" or ultipo=="real"):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Tipos diferentes")
                mantemToken()
        if(algeb=="log" or algeb=="ari" or algeb==""):
            algeb = "ari"
        fator = False
        proxToken()
        return EXPARITMETICAB()
    else:
        return 1

def EXPARITMETICAB():
    global tuplas, buffer, linha, ideExp, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    if(tuplas[2]=="(" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        return EXPARITMETICABPAREN()
    elif(tuplas[2]=="-" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        i = NEGATIVO()
        if(i==0):
            return EXPARITMETICACONTB()
        return i        
    elif(tuplas[1]=="NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real") and (chave=="inteiro" or chave=="real")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        if(tuplas[2]=="0"):
            verifexpress = False
            output(int(linha), "SemanticoError", "Divisao explicita por ZERO")
            mantemToken()
        proxToken()
        return EXPARITMETICACONTB()
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        ideExp = tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                sup = tabela[chave].get("TIPO","não foi")
                if(not(fator) and verifexpress):
                    if(sup=="inteiro" or sup=="real"):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real")):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    else:
                        verifexpress = False
                        output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                        mantemToken()
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            return EXPARITMETICACONTB()
        return i
    else:
        return 1

def EXPARITMETICABPAREN():
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    if(tuplas[1]=="NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real") and (chave=="inteiro" or chave=="real")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        proxToken()
        if(tuplas[2]==")" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            if(dentroParen):
                bufferExpressao = bufferExpressao + tuplas[2]
            proxToken()
            return EXPARITMETICACONTB()
        else:
            i = EXPARITMETICACONTB()
            if(i==0):
                if(tuplas[2]==")" and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    if(dentroParen):
                        bufferExpressao = bufferExpressao + tuplas[2]
                    proxToken()
                    return EXPARITMETICACONTB()
                else:
                    return 1
            return i
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                sup = tabela[chave].get("TIPO","não foi")
                if(not(fator) and verifexpress):
                    if(sup=="inteiro" or sup=="real"):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real")):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    else:
                        verifexpress = False
                        output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                        mantemToken()
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            if(tuplas[2]==")" and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                if(dentroParen):
                    bufferExpressao = bufferExpressao + tuplas[2]
                proxToken()
                return EXPARITMETICACONTB()
            else:
                i = EXPARITMETICACONTB()
                if(i==0):
                    if(tuplas[2]==")" and linha == tuplas[0]):
                        buffer = buffer + " " + tuplas[2]
                        if(dentroParen):
                            bufferExpressao = bufferExpressao + tuplas[2]
                        proxToken()
                        return EXPARITMETICACONTB()
                    else:
                        return 1
                return i
        return i
    else:
        return 1

def EXPARITMETICACONTB():
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, fator, dentroParen, bufferExpressao
    if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        if(verifexpress):
            if(ultipo=="inteiro" or ultipo=="real"):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Tipos diferentes")
                mantemToken()
        algeb = "ari"
        fator = False
        proxToken()
        return EXPARITMETICAB()
    else:
        return 0

def EXPATRIBUICAO():
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    if(tuplas[2]=="-" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        proxToken()
        i = NEGATIVO()
        if(i==0):
            if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
                return EXPARITMETICACONT()
            else:
                return EXPATRIBUICAOCONT()
        return i        
    elif(tuplas[1]=="NRO" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        y = tuplas[2].find(".")
        if(y<0):
            chave = "inteiro"
        else:
            chave = "real"
        if(not(fator) and verifexpress):
            if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real")):
                verifexpress = True
            else:
                verifexpress = False
                output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                mantemToken()
        x = tuplas[2].find(".")
        if(x<0):
            ultipo = "inteiro"
        else:
            ultipo = "real"
        proxToken()
        if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
            return EXPARITMETICACONT()
        else:
            return EXPATRIBUICAOCONT()
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                sup = tabela[chave].get("TIPO","não foi")
                if(not(fator) and verifexpress):
                    if(sup=="inteiro" or sup=="real"):
                        if((algeb=="ari" or algeb=="rll" or algeb=="rel") and (ultipo=="inteiro" or ultipo == "real")):
                            verifexpress = True
                        else:
                            verifexpress = False
                            output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                            mantemToken()
                    else:
                        verifexpress = False
                        output(int(linha), "SemanticoError", "Erro na expressao. Ponto do erro: "+ buffer)
                        mantemToken()
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
                return EXPARITMETICACONT()
            else:
                return EXPATRIBUICAOCONT()
        return i
    else:
        return 1

def EXPATRIBUICAOB():
    global tuplas, buffer, linha, ide, chamada, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    if(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        if(dentroParen):
            bufferExpressao = bufferExpressao + tuplas[2]
        ide = tuplas[2]
        x=0
        errou = True
        for chave in range(len(tabela)):
            g = "IDE"+str(x)
            if(tabela[chave].get(g,"não foi")==tuplas[2]):
                errou = False
                ultipo = tabela[chave].get("TIPO","não foi")
            x=x+1
        if(errou):
            verifexpress = False
            output(int(linha), "SemanticoError", "Identificador nao instanciado: "+ tuplas[2])
            mantemToken()
        proxToken()
        i = ACESSOVAR()
        if(i==0):
            if((tuplas[2]=="-" or tuplas[2]=="+" or tuplas[2]=="*" or tuplas[2]=="/") and linha == tuplas[0]):
                i = EXPARITMETICACONT()
                if(i==0):
                    return EXPRESSAOCONTB()
                return i
            elif(tuplas[2]=="(" and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                if(dentroParen):
                    bufferExpressao = bufferExpressao + tuplas[2]
                chamada=ide
                proxToken()
                return PARAN() 
            else:
                return EXPRESSAOCONTB()
        return i
    else:
        return EXPRESSAOB()

def EXPATRIBUICAOCONT():    
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    algeb = "" 
    ultipo = "" 
    dentroParen = False
    verifexpress = True 
    if(tuplas[2]=="++" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2]=="--" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:
        return 0

def EXPATRIBUICAOCONTB():    
    global tuplas, buffer, linha, algeb, ultipo, verifexpress, dentroParen, bufferExpressao
    algeb = "" 
    ultipo = "" 
    dentroParen = False
    verifexpress = True 
    if(tuplas[2]=="++" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        verifexpress = True 
        return 0
    elif(tuplas[2]=="--" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:
        return 1

################################################# MAIN ####################################################
# Verifica se a existe a pasta input
flag = True
try:
    shutil.rmtree("output")
    os.mkdir("output")        
except:    
    print("Erro na manipulação da pasta output!")
pastas = os.listdir()
for x in pastas:
	if(x == "input"):
		flag = False
if(flag):
    print("Pasta input nao encontrada")
else:    
    while(not(endRead)):
        entrada = input()
        if(not(entrada=="")):
            flagSintax = True
            while 1:
                linha = entrada.readline()	
                i = 0
                if linha=='':
                    countLinha-=1
                    maqEstados(3, " ", countLinha)
                    break
                while i+1<=len(linha):
                    caractere = ord(linha[i])
                    maqEstados(caractere, linha[i], countLinha)
                    if(not(estado=="Q0") or space):
                        i+=1
                        space = False
                    if(skip):
                        skip = False
                        break
                countLinha+=1
            entrada.close()
        countLinha=1
        buffer=""
        if(flagSintax):
            sucessoA = False
            sucessoB = False
            proxToken()
            linha = tuplas[0]
            START()
            flagSintax = False
            if(not(len(erros)==0)):                
                output(0,"ERRO","")
            else:
                sucessoA = True
            erros.clear()
            buffer=""
            print(tabela)
            erros = errosSeman
            if(not(len(erros)==0)):                
                output(0,"ERRO","")
            else:
                sucessoB = True
            if(sucessoA and sucessoB):
                erros=[]
                output(0,"ERRO","")
        tabela.clear()
        paran.clear()
        countArq+=1
        erros=[]
        dados.clear()
        tuplas.clear()
        iterador=0
        errosSeman.clear()
        iterador = 0
        linha = "01"
        looping = False
        retorno = False
        retornado = False
        ide = "" 
        ideExp = ""
        tipo = ""
        escopo = ""
        regra = ""
        regis = ""
        vetorial = False 
        chamada = "" 
        atribu = True 
        veterror = True 
        expressao = False 
        fator = True 
        algeb = "" 
        ultipo = "" 
        dentroParen = False
        verifexpress = True 
        bufferExpressao = ""
        tipoChamada = ""