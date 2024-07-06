"""
Pilhas só tem metodos como push e pop
em uma analogia com uma pilha de post-its de papel 
você só consegue ler o de cima e adicionar um encima, logo você só 
consegue inserir e remover do topo
"""


def tchau(nome):
    print("Tchau, Tchau", nome)


def saudacao2(nome):
    print(nome, "Tudo bem?!")


def saudacao(nome):
    print("Olá", nome)
    saudacao2(nome)
    print("Preparando pra dizer tchau...")
    tchau(nome)


print(saudacao("Rômulo"))
