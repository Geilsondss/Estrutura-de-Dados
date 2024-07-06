#Açaíduto
#Este codigo calcula o custo para interligar a tubulação de todas as residencias de uma cidade.
#O custo do metro é R$ 3.14
def calcular_custo_total(n, residencias):
    grafo = []
    for i in range(n):
        grafo.append([])
        
    for residencia in residencias:
        indice, A, *vizinhos = residencia
        indice -= 1
        for i in range(A):
            elemento = vizinhos[2 * i]
            posição = vizinhos[2 * i + 1] - 1
            grafo[indice].append((elemento, posição))
            grafo[posição].append((elemento, indice))

    visitado = [False] * n
    modificador = [float('inf')] * n
    modificador[0] = 0
    custo_total = 0

    for _ in range(n):
        menor_peso = float('inf')
        u = -1
        for i in range(n):
            if not visitado[i] and modificador[i] < menor_peso:
                menor_peso = modificador[i]
                u = i
        
        if u == -1:
            break  

        visitado[u] = True
        custo_total += menor_peso

        for d, v in grafo[u]:
            if not visitado[v] and d < modificador[v]:
                modificador[v] = d

    return custo_total * 3.14

n = int(input())
residencias = []
for _ in range(n):
    entrada = map(int,input().split())
    residencias.append(entrada)

custo_total = calcular_custo_total(n, residencias)
print(f'R$ {custo_total:.2f}')

#Exemplo de entrada:
    #3
    #1 2 6 2 7 3
    #2 2 6 1 20 3
    #3 2 7 1 20 2

#Saida: R$ 40.82
