#Árvore Binária de Busca Válida
#Este codigo confere se a árvore é uma arvore de busca ou não

class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
        
def constituiArvoreBinariaDeBusca(raiz):
    valores = []
    em_ordem(raiz, valores)
    for i in range(1, len(valores)):
        if valores[i] <= valores[i - 1]:
            return False
    return True
    
def em_ordem(raiz, valores):
    if raiz != None:
        em_ordem(raiz.esq, valores)
        valores.append(raiz.dado)
        em_ordem(raiz.dir, valores)

#Exemplo de entrada:
    #raiz = ArvoreBinaria(2, ArvoreBinaria(1), ArvoreBinaria(3))
    #print(constituiArvoreBinariaDeBusca(raiz))

#Saida: True
