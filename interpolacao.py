
import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informa o nome do arquivo de emails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes = []

for line in open(filepath):
    # TODO: Substituir por list comprehesion
    clientes.append(line.split(","))

for name, email in clientes:
    # TODO : Substituis por envio de email
    print(f"Enviando para: {email}")
    print(
        open(templatepath). read() 
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )