
import os

pasta = input("Qual o diretório a ser lido?")
def encontraArquivosEmPastasRecursivamente(pasta):
    arquivosTXT = []
    caminhoAbsoluto = os.path.abspath(pasta)
    for pastaAutal, subPastas, arquivos in os.walk(caminhoAbsoluto):
        arquivosTXT.extend([os.path.join(pastaAutal, arquivo) for arquivo in arquivos if arquivo.endswith('.txt')])
    return arquivosTXT
print (encontraArquivosEmPastasRecursivamente(pasta))

caminho = input("qual o caminho da pasta?")

def lePasta(caminho):
    caminhoAbsoluto = os.path.abspath(caminho)
    arq = open(clientes.txt, 'w')
    for arquivos in os.walk(caminhoAbsoluto):
        arquivo
        arq.write()
