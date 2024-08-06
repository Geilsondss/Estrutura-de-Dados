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
            soma = 0
            cont = 0
            for i in range(len(self.items)):
                cont += 1
                soma += peso.conferir()
                print(f'Peso retirado: {peso.conferir()}')
                if peso.conferir() == anilha:
                    break
                else:
                    peso.retirar()
                    
            print(f'Anilhas retiradas: {cont}')
            print(f'Peso total movimentado: {soma}')
        
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
