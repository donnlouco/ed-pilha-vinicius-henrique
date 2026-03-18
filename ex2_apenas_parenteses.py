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
    
    def pop(self):
        if self.topo is None:
            return None
        removed = self.topo
        self.topo = self.topo.next
        self.size -= 1
        return removed.value
    
    def balanco(self, value):
        balanceado = True
        
        for caracter in value:
            if caracter == '(':
                self.push('(')
            elif caracter == ')':
                if self.topo is None:
                    balanceado = False
                    break
                else:
                    pointer = self.topo.next
                    self.topo = pointer
            else:
                pass
        if balanceado == True and self.topo == None:
            print('Esta balanceado')
            return True
        else:
            print('Esta desbalanceado')
            return False
        
p = Pilha()
p.balanco('A+B)')