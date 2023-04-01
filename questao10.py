#Crie um programa que leia uma lista de números do usuário e exiba a média desses números.

media = 0

quantidade_notas = int(input('Quantidade de notas a serem digitadas: '))
for i in range(quantidade_notas):
    nota = float(input('Digite a nota do aluno: '))
    media += nota

media /= quantidade_notas
print('A média é:', media)


