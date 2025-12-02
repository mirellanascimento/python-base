"""
Faça um programa que peça ao usuário que digite uma ou mais palavras e imprima cada
uma das palavras com suas vigais duplicadas.

ex: 'Digite uma palavra (ou enter para sair): Python'
Pythoon

"""

import logging

log = logging.Logger("Alerta!!")

vogais = "aeiouãõâ"
palavras = []

while True:
    palavra = input('Insira uma palavra: ').strip()
    if not palavra:
        break

    aux = ''
    for letra in palavra:
        # TODO : Remover acentuação usando função
        if letra.lower() in vogais:
            aux += aux * 2
        else:
            aux += letra

        # If ternário: mais usado em programação funcional
        #aux += letra * 2 if letra.lower() in vogais else letra

        palavras.append(aux)

# for palavra in palavras:
#     print(palavra)
print(*palavras, sep='\n')
