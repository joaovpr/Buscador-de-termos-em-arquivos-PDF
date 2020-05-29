#coding: utf-8
import pdftotext

# Load your PDF
with open("teste22.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?

print(len(pdf))

# Iterate over all the pages
#for page in pdf:
    #print(page)

# Read some individual pages
#print(pdf[0]).encode('UTF-8')
#print(pdf[14])

# Read all the text into one string
##print("\n\n".join(pdf))


#Funcao que busca no pdf
#print(pdf[15].replace(',','').replace('.','').replace('-','').replace('(','').replace(')','').upper())
def buscar(pagina,palavra):
    pdfOrganizado = pdf[pagina].replace(',','').replace('.','').replace('-','').replace('(','').replace(')','').upper()
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



##buscar(0,'banana')


def buscarListaPalavras(listaDePalavras,num_paginas):
    for palavra in listapalavras:
        for j in range(num_paginas):
            if buscar(j,palavra) == 'CONTEM A PALAVRA':
                print('\033[1;36m'+'CONTEM A PALAVRA ' + '(' +'\033[1;31m' +palavra+'\033[0;0m'+'\033[1;36m'+')' +' PAG -' + str(j))



listapalavras = ['IGUALDADE','GÊNERO','SEXO','MASCULINO','FEMININO','DESCRIMINAÇÃO','PRECONCEITO']

buscarListaPalavras(listapalavras,len(pdf))
