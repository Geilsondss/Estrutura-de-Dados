#Janela Deslizante
#Dado um limite o codigo verifica e imprimi o numero maximo dentro daquele intervalo
from collections import deque
numero = int(input())
lista = list(map(int,input().split()))
real = deque([])
limit = int(input())

for i in lista:
    real.append(i)

def prog(n):
    maximo = []
    cont = 0
    for i in real:
        maximo.append(i)
        cont += 1 
        if cont == limit:
            print(max(maximo), end= '  ')
            maximo = []
            cont = 0
            break

for i in range(numero +1 - limit):
    prog(i)
    real.popleft()    

#Entrada:
    #9
    #1 2 3 1 4 5 2 3 6
    #3

#Saida:
    #3  3  4  5  5  5  6
