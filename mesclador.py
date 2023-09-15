#utilizarei a biblioteca PyPDF2 para manipular os PDFs
import PyPDF2 as p2 #importar o pypdf2
import os #importar o OS

#criarei a funcionalidade merge que é mesclagem utilizando o p2 junto da classe PdfMerger
merge = p2.PdfMerger()
#junto a classe listdir() na biblioteca OS para poder mexer nos arquivos
lista_arquivos = os.listdir("arquivos para mesclar")

lista_arquivos.sort() #serve para colocar em ordem os arquivos

print(lista_arquivos)

#verificar se todos os arquivos possuem .pdf para adicionar ao merge
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merge.append(f"arquivos para mesclar/{arquivo}")

merge.write("PDF Final.pdf")