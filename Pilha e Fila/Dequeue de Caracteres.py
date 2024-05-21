#Dequeue de Caracteres
#Este código tem como objetivo armazenear uma sequencia de strings em uma fila
#A Cada '*' imprime e retire o primeiro elemento da lista.
class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

entrada = input()
fila = Queue()
saida = ''
for letra in entrada:
  if letra == "*":
    saida += fila.dequeue()
    
  else:
    fila.enqueue(letra)
print(saida)

#Exemplo de entrada: ola*** mundo
#Saida: ola
