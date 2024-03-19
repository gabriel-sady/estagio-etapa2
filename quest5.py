'''5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
'''
nome = str(input("Digite uma palavra \n"))
print("Você digitou:\n", nome)
print("O inverso disto é: ")
for l in range(len(nome) -1, -1, -1):
    print(nome[l], end="")