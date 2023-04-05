#Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente.

numeros = []

for i in range(0,5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

numeros_crescente = sorted(numeros)
print('Os números em ordem crescente são: ', numeros_crescente)