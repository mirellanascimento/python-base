
import os
import sys

print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError:
        print(f"[ERROR] {str(e)}")
        print("You need to use '+='")
        print("You passes {arg}")
        print("Try with --key=value")

    key = key.lstrip("-").strip()
    value = value.strip()

    # Validação
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language= current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "it_IT": "Ciao, Mondo!",
}

message = msg.get(current_language, msg["en_US"])

""" Tratamento de erro não é necessário quando usamos um dicionário
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)
"""

print(message * int(arguments["count"]))