#Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.

numeros = []

for i in range(0,6):
    numero = int(input('Digite um número: '))
    if numero > 10:
        numeros.append(numero)

print('Números maiores do que 10 são:', numeros)
