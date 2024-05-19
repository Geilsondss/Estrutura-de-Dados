#Altura da Árvore Binária
#Este código imprime a altura de uma arvore

def altura(arvore):
    if type(arvore) == list and len(arvore) != 0:
        altura_esquerda = altura(arvore[1])
        altura_direita = altura(arvore[2])
        
        if altura_esquerda > altura_direita:
            return altura_esquerda + 1
        else:
            return altura_direita + 1
        
    else:
        return 0

#Exemplos de entrada:
    #print(altura([1, [2, []], [3, [], [4, [], []]]]))
#Saida: 3
