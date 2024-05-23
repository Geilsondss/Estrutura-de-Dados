#Colisão!
#Faça um programa que, dados o tamanho da tabela e uma sequência de chaves,
#indique como as informações seriam armazenadas.


def inicio(tamanho):
    return [[] for k in range(tamanho)]

def elementos(tabela, chave):
    indice = chave % len(tabela)
    tabela[indice].append(chave)

def saida(tabela):
    for i, lista in enumerate(tabela):
        if lista:
            print(f"{i} - {' -> '.join(map(str, lista))}")
        else:
            print(f"{i} - [x]")

T, N = map(int, input().split())
if N == 0:
    for i in range(T):
        print(f'{i} - [x]')
else:
    entrada = list(map(int, input().split()))
    
    tabela = inicio(T)
    for chave in entrada:
        elementos(tabela, chave)
        
    saida(tabela)

#Entrada:	
    #8 5
    #1 3 8 10 42

#Saida:
    #0 - 8
    #1 - 1
    #2 - 10 -> 42
    #3 - 3
    #4 - [x]
    #5 - [x]
    #6 - [x]
    #7 - [x]

