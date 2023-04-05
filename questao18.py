#Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.

numeros = []
produto = 1

for i in range(0,5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

for numero in numeros:
    produto *= numero

print('O produto dos números é: ', produto)
