import glob

caminho = input("qual a pasta a ser lida?")
arq = open('clientes.txt' , 'w')

for f in glob.glob(caminho+'*.*'):
    arq.write(f+"\n")

arq.close()
