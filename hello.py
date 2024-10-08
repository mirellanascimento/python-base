
import os
import sys

print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": None
}
for arg in sys.argv[1:]:
    # TODO : Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option {key}")
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "it_IT": "Ciao, Mondo!",
}

print(msg[current_language])