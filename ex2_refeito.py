class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.topo = None
        self.size = 0

    def push(self, value):
        pointer = Node(value)
        pointer.next = self.topo
        self.topo = pointer
        self.size += 1

    def pop(self):
        if self.topo is None:
            return None
        removed = self.topo
        self.topo = self.topo.next
        self.size -= 1
        return removed.value
    
    def balanceamento(self, value):
        stack = []
        mapeamento = {')':'(', ']': '[', '}':'{'}

        for caracter in value:
            if caracter in mapeamento.values():
                stack.append(caracter)
            elif caracter in mapeamento:
                if not stack or stack.pop() != mapeamento[caracter]:
                    print('Esta desbalanceada')
                    return False
        
        if len(stack) == 0:
            print('Esta balanceada')
            return True
        else:
            print('Esta desbalanceada')
            return False
        


x = Stack()
x.balanceamento('((A+B) * C)')
x.balanceamento('((A+B)')