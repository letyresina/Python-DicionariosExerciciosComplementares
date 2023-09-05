'''
    Exercício 2:
    Escreva um programa que recebe uma frase como entrada e retorna um dicionário onde as
    chaves são as palavras únicas na frase e os valores são o número de vezes que cada
    palavra aparece.
'''

dicionario = {} 

def transformaFrase(frase):
    palavra = frase.split()
    for i in palavra:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    return dicionario

frase = input("Informe uma frase: ")
print(transformaFrase(frase))