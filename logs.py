import logging
import os

# BOILERPLATE: Código repetitivo
# TODO : Usar função
# TODO : Usar lib externa (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Nossa instancia
log = logging.Logger("logs.py", log_level) # Mais recomendando:  logging.DEBUG
# Nível
ch = logging.StreamHandler() # escreve no destino 
ch.setLevel(log_level)
# Formatação
ftm = logging.Formatter(
    '%(asctime)s, %(name)s, %(levelname)s'
    'l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(ftm)
# Destino
log.addHandler(ch)

"""
logging.debug("Mensagem pro dev, qe, sysasdmin")
logging.info("Mensagem geral para usuários")
logging.warning("Aviso que não causa efeito")
logging.error("Erro que afeta uma única execução")
logging.critical("Erro geral. Exemplo: banco de dados que sumiu")
"""

print("------")

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("[ERRO]: Deu erro %s", str(e))