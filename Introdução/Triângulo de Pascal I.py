# Triângulo de Pascal I
#Implemente a função triangulo, que recebe um número inteiro n e retorna todas linhas menores e iguais a n do triângulo de Pascal em uma lista.

def triangulo(n):
    triangulo_pascal = [[1]]
    if n == 0:
        return([])
    else:
        for i in range(1, n):
            l_anterior = triangulo_pascal[-1]
            l_nova = [1] 
            
            for j in range(1, i):
                l_nova.append(l_anterior[j - 1] + l_anterior[j]) 
                
            l_nova.append(1)
            triangulo_pascal.append(l_nova) 
            
        return triangulo_pascal

#Exemplo de entrada:
    #print(triangulo(5))

#Saida:
    #[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]