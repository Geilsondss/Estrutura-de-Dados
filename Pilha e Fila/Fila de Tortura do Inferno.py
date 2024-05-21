#Fila de Tortura do Inferno
#Dado uma lista de nomes após uma eternidade, a primeira pessoa da fila é chamada e torturada
#Quando a pessoa finalmente sai da frente da fila, ela é redirecionada ao fim da fila e chamamos a proxima.
#O seu trabalho é dizer quem será a ultima e a primeira pessoa da fila apos toda a tortura ser realiza.

class Inferno:
    def __init__(self):
        self.eternidade = []
    
    def inserir(self, item):
        self.eternidade.append(item)
                             
    def remover(self):
        self.eternidade.append(self.eternidade[0])
        self.eternidade.pop(0)
    
    def printar(self):
        print(f'Pessoa da frente: {self.eternidade[0]}')
        print(f'Pessoa do fim: {self.eternidade[-1]}')
                
Nomes = Inferno()
entrada = input().split()
n = int(input())
for i in entrada:
    Nomes.inserir(i)

for j in range(n):
    Nomes.remover()
Nomes.printar()

#Exemplo de entrada:
    #Carlos Gabriel Joao Vitor
    #1
#Saida:
    #Pessoa da frente: Gabriel
    #Pessoa do fim: Carlos
