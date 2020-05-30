#coding: utf-8
import pdftotext

# Load your PDF (Aqui voce coloca o nome do arquivo .pdf onde está com 'teste22.pdf' -- lembre das aspas o arquivo PDF tem que estar localizado na pasta do programa)
with open("teste22.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?

print('O PDF TEM - ' + str(len(pdf)) + ' PÁGINAS')

# Iterate over all the pages
#for page in pdf:
    #print(page)

# Read some individual pages
#print(pdf[0]).encode('UTF-8')
#print(pdf[14])

# Read all the text into one string
##print("\n\n".join(pdf))


#Funcao que busca no pdf
##(NAO MEXER)##
def buscar(pagina,palavra):
    pdfOrganizado = pdf[pagina].replace(',','').replace('.','').replace('-','').replace('(','').replace(')','').replace(':','').replace(';','').upper()
    listaP = (pdfOrganizado).split()

    saida = False
    for i in range(len(listaP)):
        word = listaP[i].encode('utf8')
        if word == palavra:
            saida = True
            break

        else:
            saida = False


    if saida == True:
        return('CONTEM A PALAVRA')
    else:
        return('NAO CONTEM A PALAVRA')






def buscarListaPalavras(listaDePalavras,num_paginas):
    for palavra in listapalavras:
        for j in range(num_paginas):
            if buscar(j,palavra) == 'CONTEM A PALAVRA':
                print('\033[1;36m'+'CONTÉM A PALAVRA ' + '(' +'\033[32m' +palavra+'\033[0;0m'+'\033[1;36m'+')' +' PAG -' + str(j))







def buscarListaTermos(listaDeTermos,num_paginas):
    for m in range(num_paginas):
        pdfOrganizado = pdf[m].replace(',','').replace('.','').replace('-','').replace('(','').replace(')','').replace(':','').replace(';','').upper()
        listaP = (pdfOrganizado).split()
        ##print(pdfOrganizado)
        for k in range(len(listaDeTermos)):
            termo_atual = listaDeTermos[k].split()
            if len(termo_atual) == 2:
                for l in range(len(listaP)):
                    if termo_atual[0] == listaP[l].encode('utf8') and termo_atual[1] == listaP[l+1].encode('utf8'):
                        print('\033[1;36mCONTÉM O TERMO (' + '\033[32m' +listaTermos[k] + '\033[1;36m ) PAG- '+str(m))
            if len(termo_atual) == 3:
                for l in range(len(listaP)):
                    if termo_atual[0] == listaP[l].encode('utf8') and termo_atual[1] == listaP[l+1].encode('utf8') and termo_atual[2] == listaP[l+2].encode('utf8'):
                        print('\033[1;36mCONTÉM O TERMO (' + '\033[32m' +listaTermos[k] + '\033[1;36m ) PAG- '+str(m))














###########AREA DO USUARIO#############

##(Listas de Termos que se quer buscar)

listaTermos = ['EFEITOS CONSIDERADOS', 'RESULTADOS AJUSTADOS','GRANDES DESAFIOS','É ESSENCIAL','RAPADURA PRETA','DE IMPACTO POSITIVO']

##(Listas de Palavras que se quer buscar)

listapalavras = ['IGUALDADE','GÊNERO','SEXO','MASCULINO','FEMININO','DESCRIMINAÇÃO','PRECONCEITO']

print('##############################################################################')
buscarListaTermos(listaTermos,len(pdf))
print('\033[0;0m#############################################################################')
buscarListaPalavras(listapalavras,len(pdf))
