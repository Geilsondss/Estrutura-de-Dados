#Quarto Bagunçado
#Dado uma sequencia de roupas, arrume-as em seus repectivos lugares
#Considere que é uma pilha de roupa.

class Armario:
    def __init__(self):
        self.tipo = []
        self.cor = []
    
    def inserir_tipo(self, item):
        self.tipo.insert(0, item)
    
    def inserir_cor(self, item):
        self.cor.insert(0, item)
    
    def remover_cor(self):
        return self.cor.pop(0)
    
    def remover_tipo(self):
        return self.tipo.pop(0)
        
    def printar(self):
        for i in range(n):
            print(f'Tipo: {organizar.remover_tipo()}, Cor: {organizar.remover_cor()}')
        print(f'Total de roupas: {n}')
        print(f'Total de tempo: {soma}')
        
   
n = int(input())
organizar = Armario()
soma = 0

for i in range(n):
    tipo, cor, quant = input().split()
    quant = int(quant)
    organizar.inserir_tipo(tipo)
    organizar.inserir_cor(cor)
    soma += quant
organizar.printar()
    

#Exemplo de entrada:
    #5
    #camisa verde 1
    #calca azul 3
    #sobretudo preto 10
    #cueca branca 1
    #cueca azul 2
    
#Saida:
    #Tipo: cueca, Cor: azul
    #Tipo: cueca, Cor: branca
    #Tipo: sobretudo, Cor: preto
    #Tipo: calca, Cor: azul
    #Tipo: camisa, Cor: verde
    #Total de roupas: 5
    #Total de tempo: 17
