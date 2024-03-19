'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

n1 = 0
n2 = 1

pertence = 0

numInfo = int(input())


i = 0

while i<=numInfo:
    n3 = n1 + n2
    if n3 == numInfo or numInfo == 0:
        print("Este número pertece a sequencia de Fibonacci.")
        pertence = 1
    n1 = n2
    n2 = n3
    i += 1

if pertence == 0:
    print("Este numero não pertence a sequencia de Fibonacci")