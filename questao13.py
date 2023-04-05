#Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".

palavras = []

for i in range(5):
    palavra = input('Digite uma palavra: ')
    if palavra.startswith('a'):
        palavras.append(palavra)

print('Palavras que começam com a letra "a":', palavras)

