caminho = input("Qual o caminho do arquivo?")
arquivo = input("Qual o nome do arquivo?")
arq = open(arquivo , 'w')
arq.write(input("O que deseja gravar neste arquivo?"))
arq.close()


print(caminho)
print(arquivo)
print(caminho+arquivo)
arq = open(caminho+arquivo , 'r')
print(arq.read())
arq.close()

