#Crie um programa que leia uma lista de números do usuário e exiba somente os números pares.

numeros = []

for i in range(1,10):
    numero = int(input('Digite um número: '))
    if (numero %2==0):
        numeros.append(numero)

print('Os números pares digitados foram: ', numeros)
