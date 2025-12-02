import sys
import logging

log = logging.Logger("alerta")

info ={
    'temperatura': None,
    'umidade': None
}

while True:

    info_size = len(info.values()) # tamanho do dicionario
    filled_size = [value for value in info.values() if value is not None]

    # tamanho do dict for diferente do que está preenchido
    if all(info_size) != filled_size: 
        break

    keys = info.keys()
    for key in keys:
        if info[key] is not None:
            continue
        try:
            info[key] = float(input(f"Indique a {key} atual: ").strip())
        except ValueError:
            log.error("Temperatura inválida!")
            sys.exit(1)

#temp = info['temperatura']
#umidade = info['umidade']
temp, umidade = info.values()

if temp > 45:
    print("Calor extremo!!!")
elif temp * 3 >= umidade:
    print('Alerta!! Perigo de calor úmido')
elif temp >= 10 and temp <= 30:
    print("Normal!")
elif 0 >= temp and temp <= 10:
    print("Frio")
elif temp < 0:
    print("Alerta frio extremo!")

