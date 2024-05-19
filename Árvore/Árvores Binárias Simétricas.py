#Árvores Binárias Simétricas
#Este codigo confere se a árvore é simétrica ou não

class ArvoreBinaria:
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def Simetria(esq, dir):
    if esq == None and dir == None:
        return True
    elif esq == None or dir == None:
        return False
    return (esq.dado == dir.dado) and Simetria(esq.esq, dir.dir) and Simetria(esq.dir, dir.esq)

def verificaSimetria(raiz):
    if raiz == None:
        return True
    return Simetrico(raiz.esq, raiz.dir)

#Exemplo de entrada:
    #raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
    #print(verificaSimetria(raiz))

#Saida: True
