#Drummondichlorian!
#Dado uma sequencia de entradas com funções variadas
#Imprima se a sequencia de instruções se comporta como uma Pilha, Fila,
#Fila de prioridades, se há mais de uma possibilidade ou se não é nenhuma das ditas anteriormente.

class Drummondichlorian:
    def __init__(self):
        self.items = []
        global pilha
        global fila
        global prioridade
        pilha = True
        fila = True
        prioridade = True
    
    def inserir(self,item):
        self.items.append(item)
        
    def remover(self, item):
        global pilha
        global fila
        global prioridade
        if item not in self.items:
            pilha = False
            fila = False
            prioridade = False
            
        else:
            if item == self.items[-1] and pilha == True:
                pilha = True
            else:
                pilha = False
                
            if item == self.items[0] and fila == True:
                fila = True
            else:
                fila = False
                
            if item == max(self.items) and prioridade == True:
                prioridade = True
            else:
                prioridade = False
                
            self.items.remove(item)	
        
    def printar(self):
        global pilha
        global fila
        global prioridade
        if (prioridade == True and pilha == True) or (prioridade == True and fila == True) or (pilha == True and fila == True):
            print('uai?')
            
        elif prioridade:
            print('AIPO')
            
        elif pilha:
            print('LIFO')
            
        elif fila:
            print('FIFO')
        
        else:
            print('no hay!')
        
mestre = Drummondichlorian()        
for i in range(5):
    n = int(input())
    for j in range(n):
        instrucao, x = input().split()
        x = int(x)
        if instrucao == 'in':
            mestre.inserir(x)
        
        elif instrucao == 'out':
            mestre.remover(x)
    mestre.printar()
    mestre.__init__()
    
#Exemplo de entrada:
    #3
    #in 17
    #in 13
    #out 17
    #5
    #in 1
    #in 2
    #in 3
    #out 1
    #out 2
    #5
    #in 23
    #in 30
    #out 30
    #in 1
    #out 23
    #6
    #in 100
    #in 90
    #in 80
    #out 80
    #out 90
    #out 100
    #5
    #in 1
    #in 2
    #out 1
    #in 1
    #out 1

#Saida:
    #uai?
    #FIFO
    #AIPO
    #LIFO
    #no hay!
