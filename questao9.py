#Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista.

menor = 999999

for i in range(1,6):
    numero = int(input('Digite o número: '))
    if numero < menor:
        menor = numero

print('O menor número é: ', menor)