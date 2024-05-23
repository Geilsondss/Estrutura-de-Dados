#Editor de Listas I
#Este código tem como objetivo ser um editor de lista dinâmica.
#As funções de alteração da lista são:
    #I insere o valor no início da lista.
    #F insere o valor no final da lista.
    #P remove do final e imprime valor removido.
    #D remove do início e imprime valor removido.
    #X Indica o final das operações e que a lista resultante deve ser impressa.

from collections import deque
lista_ordenada = deque([])
while True:
    posicao = input().split()
    if posicao[0] == 'X':
        break
    if posicao[0] == 'F':
        lista_ordenada.append(posicao[1])
    if posicao[0] == 'I':
        lista_ordenada.appendleft(posicao[1])
    if posicao[0] == 'P':
        print(lista_ordenada[-1])
        lista_ordenada.pop()
    if posicao[0] == 'D':
        print(lista_ordenada[0])
        lista_ordenada.popleft()

for i in lista_ordenada:
    print(i)

#Exemplo de entrada:
    #I 54
    #I 87
    #F 90
    #I 76
    #D
    #I 76
    #P
    #F 90
    #X

#Saida:
    #76
    #90
    #76
    #87
    #54
    #90

    
