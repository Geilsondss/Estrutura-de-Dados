#Matriz de Adjacência
#Este codigo mostra a representação de grafos por matriz.
#São passados 3 parementos: Dimenção do grafo(matriz); Posições ocupadas; Se o grafo é Direcionado(D) ou Não Ditecionado(N).

dime, N, dire = input().split()
dime = int(dime)
N = int(N)
matriz = []
for i in range(dime):
    matriz.append([])
    for j in range(dime):
        matriz[i].append(0)

for i in range(N):
    linha, coluna, elemento = map(int,input().split())
    if dire == "N":
        matriz[linha-1][coluna-1] =  elemento
        matriz[coluna-1][linha-1] =  elemento
    else:
        matriz[linha-1][coluna-1] =  elemento

for k in matriz:
    for i in range(len(k)):
        espaço = 4 - len(str(k[i]))
        espaço = espaço* ' '
        if i == len(k) -1:
            print(f'{espaço}{k[i]}')
        else:
            print(f'{espaço}{k[i]}', end = '')
    
#Exemplo de entrada:
    #3 5 D
    #2 3 2
    #2 1 3
    #1 2 4
    #3 1 4
    #3 2 1 

#Saida:
 #  0   4   0
 #  3   0   2
 #  4   1   0
