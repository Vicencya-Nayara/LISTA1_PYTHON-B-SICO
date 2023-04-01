#Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.

soma = 0
for i in range(1,10):
    numero = int(input('Digite o número: '))

    soma = soma + numero

print('A soma é: ', soma)

