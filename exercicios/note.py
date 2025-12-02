
__version__ = "0.1.0"

import sys
import os

cmds = ("read", "new") # Posso ler uma nota ou criar uma novas
path = os.curdir # Diretorio atual
filepath = os.path.join(path, "notes.txt") # Montar o caminho para o arquivo notes

arguments = sys.argv[1:] # Argumentos para rodar no prompt 
if not arguments:
    print("Invalid usage")
    print(f"You must especify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == 'read':
    # Leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower == arguments[1].lower:
            print(f"Title: {title}")
            print(f"Tag: {tag}")
            print(f"Text: {text}")
            print("-" * 30)
            print()

    
if arguments[0] == 'new':
    # Criação das notas
    title = arguments[1] # TODO: Tratar exception
    text = [
        f'{title}',
        input('Tag: ').strip(),
        input('Text:\n').strip(),
    ]    
    with open(filepath, 'a') as file_:
        file_.write("\t".join(text) + '\n')

