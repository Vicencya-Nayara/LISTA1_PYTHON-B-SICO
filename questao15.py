#Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.

numeros = []

for i in range(0,6):
    numero = int(input('Digite um número: '))
    if numero < 5:
        numeros.append(numero)

print('Números menores que 5:', numeros)