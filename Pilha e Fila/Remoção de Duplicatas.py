#Remoção de Duplicatas
#Dado uma sequencia de equações matematicas(strings) diga se há ou não duplicatas.
#Duplicatas são usos de simbolos matematicos que não fazem diferentes quando repetidos.
#Exemplo: ((1001+110)) é equivalente a 5∗(1001+110)

class Duplicadas:
    def __init__(self):
        self.expressao = []
    
    def inserir(self,item):
        self.expressao.append(item)
        
    def subs(self,mud):
        duplicada = False
        lista = self.expressao
        equacoes = []
        index = 0
        variavel = []
        i = 0
        while i < len(lista):
                if (lista[i] == mud):
                    variavel.append(index)
                    equacoes.append([])
                    index += 1
                for j in variavel:
                    equacoes[j].append(lista[i])
                    
                if mud == '(':
                    inverso = ')'
                elif mud == '[':
                    inverso = ']'
                elif mud == '{':
                    inverso = '}'
                    
                if (lista[i] == inverso):
                    variavel.pop()  
                i+= 1
                
        for subs in equacoes:
                percuso = subs[1:len(subs) - 1]
                if percuso in equacoes:
                    duplicada = True
        
        if duplicada:
            return True
        else:
            return False
                           
    def confere(self):
        lista = self.expressao
        if (lista.count('(') <= 1) and (lista.count('{') <= 1) and (lista.count('[') <= 1):
            duplicadaP = duplicadaC = duplicadaCh = False
        
        else:
            duplicadaP = verificacao.subs('(')
            duplicadaC = verificacao.subs('[')
            duplicadaCh = verificacao.subs('{')        
        if duplicadaP or duplicadaC or duplicadaCh:
            print('A expressão possui duplicata.')
                
        else:
            print('A expressão não possui duplicata.')
            
n = int(input())
verificacao = Duplicadas()
for i in range(n):
    entrada = input()
    for j in entrada:
        verificacao.inserir(j)
    verificacao.confere()
    verificacao.__init__()
    
#Exemplo de entrada:
    #5
    #{[(4-77)*21]}+((3*4)+(4*3))
    #((93*(5)))
    #(43*19)
    #(((7)*(31)))
    #((35/((1))/41))

#Saida:
    #A expressão não possui duplicata.
    #A expressão possui duplicata.
    #A expressão não possui duplicata.
    #A expressão possui duplicata.
    #A expressão possui duplicata.
