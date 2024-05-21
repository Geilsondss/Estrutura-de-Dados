#Anilhas da Academia
#O programa inseri as anilhas até o numero "0" ser digitado, apos isso é digitado qual anilha necessita.
#Dada uma sequencia de anilhas estão empilhadas, faça um programa que
#Acompanhar a quantidade de anilhas que são retiradas até se pegar a anilha específica da série de exercícios.
#Caso não haja a anilha desejada tire imprima todas.

class Academia:
    def __init__(self):
        self.items = []
        
    def inserir(self, item):
        self.items.insert(0, item)
    
    def retirar(self):
        return self.items.pop(0)
    
    def conferir(self):
        return self.items[0]
    def printar(self):
        if len(self.items) != 0:
            soma = anilha
            cont = 1
            acabou = 0
            for i in range(len(self.items)):
                if peso.conferir() != anilha:
                    soma += peso.conferir()
                    print(f'Peso retirado: {peso.retirar()}')
                    cont += 1
            if anilha in self.items:
                print(f'Peso retirado: {anilha}')
                print(f'Anilhas retiradas: {cont}')
                print(f'Peso total movimentado: {soma}')
            else:
                print(f'Anilhas retiradas: {cont - 1}')
                print(f'Peso total movimentado: {soma - anilha}')
        
peso = Academia() 
while True:
    entrada = int(input())
    if entrada != 0:
        peso.inserir(entrada)
    else:
        break

anilha = int(input())
peso.printar()


#Exemplo de entrada:
    #20
    #5
    #10
    #3
    #50
    #20
    #0
    #10

#Saida:
    #Peso retirado: 20
    #Peso retirado: 50
    #Peso retirado: 3
    #Peso retirado: 10
    #Anilhas retiradas: 4
    #Peso total movimentado: 83
