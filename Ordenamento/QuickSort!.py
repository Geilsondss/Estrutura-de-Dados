#QuickSort!
#É um codigo simples de QuickSort.

def quickSort(alist):
    if len(alist) <=1:
        return alist
    esquerda, pivo, direita = reordena(alist)
    esquerda = quickSort(esquerda)
    direita = quickSort(direita)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist):
    pivo = alist[0]
    esquerda = []
    direita = []
    for i in (alist[1:]):
        if i > pivo:
            direita.append(i)
        elif i <= pivo:
            esquerda.append(i)
    
    return esquerda, pivo, direita
    
#Exemplo de entrada:
    #print(quickSort([3,4,6,1,2,5]))

#Saida:
    #[1, 2, 3, 4, 5, 6]
