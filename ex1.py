# 1. Inversão de string usando pilha 
# Escreva um programa que inverta uma palavra usando uma pilha.

# Exemplo:

# Entrada:
# ALGORITMO
# Saída Esperada:
# OMTIROGLA

# Dica:

# Empilhar cada caractere
# Desempilhar até a pilha esvaziar


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Pilha:
    def __init__(self):
        self.topo = None
        self.size = 0