#Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares.

soma = 0

for i in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero %2!=0:
        soma += numero

print('A soma dos números ímpares é: ', soma)