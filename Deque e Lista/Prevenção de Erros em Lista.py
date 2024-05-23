#Prevenção de Erros em Lista
#Este código tem como objetivo remover e adicionar elementos em uma lista.
#Este codigo previni o erro de remover algo que não possui

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp is not None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
        return lstr

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

#Exemplo de entrada:
    #L = UnorderedList()
    #L.add(3)
    #L.add(2)
    #L.add(1)
    #L.remove(2)
    #print(f'Lista: {L}')

#Saida:
    #Lista: 1 3
