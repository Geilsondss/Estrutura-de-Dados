#Prevenção de Erros
#Este codigo insere e retira elementos de uma lista, previnindo possiveis erros
#Como retirar um elemento da lista sem possuir elementos.

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            self.items = self.items 
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            self.items = self.items 
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
#Exemplo de entrada:
    #s = Stack() 
    #s.push(1)
    #s.push(2)
    #s.pop()
    #s.push(3)
    #while not s.isEmpty():
        #print(s.pop())

#Saida:
    #3
    #1