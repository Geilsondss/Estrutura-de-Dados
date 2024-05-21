#Pop de Caracteres
#Dado uma sequencia de strings, adicione-as em uma pilha.
#A cada '*' imprima e retire o ultimo elemento que foi colocado.
class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop(0)


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
    
#Saida: alo
    
        