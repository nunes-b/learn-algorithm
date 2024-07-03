caixa_sala = [[], [], []]
caixas_cozinha = [[], [], []]
caixas_quarto = [[], ["chave"], []]

caixas = [caixa_sala, caixas_cozinha, caixas_quarto]


def procure_pela_chave(caixas):
    for indice, pilha in enumerate(caixas):
        for obj, caixa in enumerate(pilha):
            if "chave" in caixa:
                return f"A chave está na pilha {indice}, caixa {obj}"
    return "A chave não foi encontrada"


print(procure_pela_chave(caixas))
