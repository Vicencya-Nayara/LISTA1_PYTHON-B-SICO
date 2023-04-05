#Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.

maior = 0

for i in range(1, 6):
    numero = int(input('Digite o número: '))
    if numero > maior:
        maior = numero

print('O maior número da lista é: ', maior)

