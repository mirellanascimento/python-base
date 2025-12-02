import logging
import os
from logging import handlers

# TODO : Usar função
# TODO : Usar lib externa (loguru)

'''
# BOILERPLATE: Código repetitivo para formatar o log

    1. Verifica qual o level que o usuário está passando
    2. Cria a própria instância
    3. Configurações
        - Level
        - Formataçao
        - Objeto de formatação dentro do handler
        - Adicionar o handler ao logging
'''


log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level) # Mais recomendando:  logging.DEBUG
# Nível
#ch = logging.StreamHandler() # Escreve no destino. Padrão: Console/terminal
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6,
    backupCount=10
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s, %(name)s, %(levelname)s'
    'l:%(lineno)d f:%(filename)s %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

log.debug("Mensagem pro dev, qe, sysasdmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa efeito")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral. Exemplo: banco de dados que sumiu")

print("------")

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("[ERRO]: Deu erro %s", str(e))