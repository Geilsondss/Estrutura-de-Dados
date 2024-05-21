#Início Topo Mantém
# Dado uma sequencia de instruções realize-as.
#Em seguida imprima todos os elementos existentes na Pilha

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
      
    def pop(self):
       self.items.pop(0)
      
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

#Exemplo de entrada:
    #s = Stack() 
    #s.push(0)
    #s.push(2)
    #s.push(0)
    #s.push(2)
    #s.push('D')
    #s.push('E')
    #for i in s.items:
        #print(i)

#Saida:
    #E
    #D
    #2
    #0
    #2
    #0
        