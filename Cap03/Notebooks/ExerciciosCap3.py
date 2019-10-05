# Exercício 10 - Faça um programa que conte quantas vezes a letra \"r\" aparece na frase abaixo. Use um placeholder na \n",
# sua instrução de impressão\n",

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a \n",
# vantagem de existir.” (Machado de Assis)\n",

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
for letra in frase:
    if letra == "r":
        count +=1
print("A letra 'R' aparence %s vezes na frase".%(count))