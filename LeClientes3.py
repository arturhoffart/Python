import glob

caminho = input("qual a pasta a ser lida?")
arq = open('clientes.txt', 'w')
listaCliente = []

for f in glob.glob(caminho+'*.*'):
    cliente = open(f,'r')
    arquivo = cliente.readlines()
    for line in arquivo:
        listaCliente.append(line)
        #arq.write(line+",")
    listaCliente.append("\n\n")
    #arq.write("\n")
    cliente.close()

for f in listaCliente:
    arq.write(f)

arq.close()
