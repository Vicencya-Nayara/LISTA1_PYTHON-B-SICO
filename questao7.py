#Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa.

#Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa

palavra_longa = ''

for i in range(0,4):
    palavra = str(input('Digite  uma palavra: '))
    if len(palavra) > len(palavra_longa):
        palavra_longa = palavra

print('A palavra mais longa é: ', palavra_longa)
