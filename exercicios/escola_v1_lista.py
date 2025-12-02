"""O programa exibi relatório de crianças por atividade.

Imprmir a lista de crianças agrupadas por sala e 
que frequenta cada uma das atividades.

"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Inglês", aula_ingles), 
              ("Música", aula_musica), 
              ("Dança", aula_danca), 
            ]

for nome_atividade, atividade in atividades:

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"{nome_atividade} da sala 1:", atividade_sala1)
    print(f"{nome_atividade} da sala 2:", atividade_sala2)
    print("-" * 50)
