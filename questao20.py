#Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente

numeros = []

for i in range(0,5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

numeros_decrescente = sorted(numeros, reverse=True)
print('Os números em ordem crescente são: ', numeros_decrescente)