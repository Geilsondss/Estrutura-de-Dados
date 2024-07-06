#Forévis Alonis
#Este codigo tem o objetivo de dizer qual o numerto minimo de ligações para chegar em uma vertice.
#Se não for possivel sair de uma vertice e chegar a outra imprima "Forevis alonis..."
n = int(input())
matriz = []
vertices = []
for i in range(n):
    entrada = input().split()
    if int(entrada[1]) > 0:
        matriz.append(entrada[0])
        matriz.append(entrada[2:])
        vertices.append(entrada[0])

def conexões(principal):
    visitas = [saida]
    modificador = [[saida,0]]
    while True:
        posição, ligações = modificador.pop(0)
        if posição == chegada:
            return ligações -1 
        
        localização = principal.index(posição)
        for i in (principal[localização+1]):
            if i not in visitas:
                visitas.append(i)
                modificador.append([i,ligações+1])

saida, chegada = input().split()
if saida not in vertices or chegada not in vertices:
    print('Forevis alonis...')

else:
    print(conexões(matriz))

#Exemplo de entrada:
    #4
    #1 1 2
    #2 2 1 3
    #3 2 2 4
    #4 1 3
    #4 1

#Saida: 2
