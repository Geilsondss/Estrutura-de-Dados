#Inversão de Uma Lista Encadeada
#Este codigo inverte uma lista encadeada

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

#Todo o codigo anterior e dado pela questão.

def inverterLista(L : UnorderedList):
    sem_espaco = (L.__str__().split())
    depois = (sem_espaco[::-1])
    depois = " ".join(depois)
        
    return depois

#Entrada:
    #L = UnorderedList()
    #L.add(1)
    #L.add(2)
    #L.add(3)
    #L.add(4)
    #L.add(5)
    #print(f'Lista antes: {L}')
    #L = inverterLista(L)
    #print(f'Lista depois: {L}')

#Saida:
    #Lista antes: 5 4 3 2 1
    #Lista depois: 1 2 3 4 5

