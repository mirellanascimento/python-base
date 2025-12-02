
import os
import sys
import logging


log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level) # Mais recomendando:  logging.DEBUG
ch = logging.StreamHandler() # escreve no destino 
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s, %(name)s, %(levelname)s'
    'l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
           "You need to use '=', you passed %s. Try --key=value: %s",
           arg,
           str(e) 
        )

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