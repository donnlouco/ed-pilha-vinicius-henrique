# 2. Verificação de parênteses
# Implemente um verificador de parênteses confirmando se os mesmo estão balanceados.

# Exemplo:

# Válido:
# ((A+B) * C)
# Inválido:
# (A+B))

# Teste:

# ((A+B) * C)
# (A+B))
# ((A+B)

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
            return None
        removed = self.topo
        self.topo = self.topo.next
        self.size -= 1
        return removed.value
    
    def balanceamento(self, value):
        lista = []
        mapa = {')': '(', '}': '{', ']': '['}

        for caracter in value:
            if caracter in mapa.values():
                lista.append(caracter)
            elif caracter in mapa.keys():
                if not lista or lista.pop() != mapa[caracter]:
                    print('Esta desbalanceado')
                    return False
        
        if len(lista) == 0:
            print('Esta balanceado')
    

x = Pilha()
x.balanceamento('((A+B) * C)')
