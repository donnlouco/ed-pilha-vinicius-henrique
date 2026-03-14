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
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
class Pilha:
    def __init__(self):
        self.topo = None
        self.size = 0

    def push(self, value):
        pointer = Node(value)
        pointer.next = self.topo
        self.topo = pointer
        self.size += 1

    def pop(self):
        if self.topo.value is None:
            print("A pilha esta vazia")
            return None
        removed = self.topo
        self.topo = self.topo.next
        self.size -= 1
        return removed.value

    def peek(self):
        if self.topo is None:
            return None
        return self.topo.value
    
    def inversao(self):
        if self.topo is None:
            return None
        pointer = self.topo
        while pointer is not None:
            print(f"{pointer.value}", end="")
            pointer = pointer.next

algoritmo = Pilha()
algoritmo.push("a")
algoritmo.push("l")
algoritmo.push("g")
algoritmo.push("o")
algoritmo.push("r")
algoritmo.push("i")

algoritmo.inversao()
