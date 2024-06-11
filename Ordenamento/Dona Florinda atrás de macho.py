#Dona Florinda atrás de macho
#D. Florinda adora dançar e por conta disso definiu que a altura ideal para seu parceiro é de 1,80 m.
#Seu primeiro critério é encontrar alguém que é o mais próximo possível desta altura, não faz diferença ser um pouco mais alto ou mais baixo.
#Dentre os candidatos, ela prefere alguém o mais próximo possível de 75 kg, pois seus pés dançantes não aceitam alguém mais pesado.
#Se houver pretendentes da mesma altura, ela escolhe o mais leve (pisões são inevitáveis!).
#Se dois ou mais candidatos têm as mesmas características físicas, ordene-os pelo sobrenome (e depois pelo primeiro nome se for necessário desempatar).
#Defina um algoritmo que ordene uma lista de pretendentes conforme os critérios definidos.

def quickSort(alist,posição,limite):
    if len(alist) <=1:
        return alist
    esquerda, pivo, direita = reordena(alist,posição,limite)
    esquerda = quickSort(esquerda,posição,limite)
    direita = quickSort(direita,posição,limite)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist,posição,limite):
    if limite == 0 or limite == 180:
        pivo = alist[0][posição]
    else:
        pivo = abs(alist[0][posição] - limite)
    esquerda = []
    direita = []
    for i in range (1,len(alist)):
        passa = True
        if limite == 180:#altura
            if (alist[i][posição]) <= pivo:
                esquerda.append(alist[i])
            else:
                direita.append(alist[i])
        
        elif limite == 75:
            if abs(alist[i][posição]- limite) <= pivo:
                esquerda.append(alist[i])
            else:
                direita.append(alist[i])
        
        else:#nome ou sobrenome
            if alist[i][posição] > pivo:
                direita.append(alist[i])
            elif alist[i][posição] <= pivo:
                esquerda.append(alist[i])     
    pivo = alist[0]
    return esquerda, pivo, direita

def Repetições(n,pre_ordenada,igual):
    verificando_empate = [[]]
    auxiliar = [[]]
    for i in range(n):
        repet = auxiliar
        passagem = True
        for j in range(len(repet)):
            if len(auxiliar[j]) > igual:
                if pre_ordenada[i][igual] == auxiliar[j][igual]: 
                    verificando_empate[j].append(pre_ordenada[i])
                    passagem = False
            
        if passagem:
            auxiliar.append(pre_ordenada[i])
            verificando_empate.append([pre_ordenada[i]])
    verificando_empate = verificando_empate[1:]
    
    return verificando_empate

n = int(input())
lista_pretendentes  = []
peso_maior = []
peso_menor = []

for i in range(n):
    nome, sobrenome, altura, peso = input().split()
    altura = int(altura)
    peso = int(peso)
    absoluto = abs(altura-180)
    pretendentes = [nome, sobrenome, altura, peso,absoluto]
    lista_pretendentes.append(pretendentes)
    
ordenação_altura = quickSort(lista_pretendentes,4,180)

Processo_peso =  Repetições(n,ordenação_altura,4)  
ordenação_TOTAL = []
for i in Processo_peso:
    ordenação_peso = []
    for h in range(len(i)):
        if i[h][3] > 75:
            peso_maior.append(i[h])
        else:
            peso_menor.append(i[h])
    ordenação_peso.extend(quickSort(peso_menor,3,75))
    ordenação_peso.extend(quickSort(peso_maior,3,75))
    Processo_sobrenome = Repetições(len(ordenação_peso),ordenação_peso,3)
    for j in Processo_sobrenome:
        Sobrenome_em_ordem = (quickSort(j,1,0))
        Processo_nome = Repetições(len(Sobrenome_em_ordem),Sobrenome_em_ordem,1)
        for k in Processo_nome:
            ordena_nome = (quickSort(k,0,0))
            for l in ordena_nome:
                if l not in ordenação_TOTAL or (lista_pretendentes.count(l) > 1 and ordenação_TOTAL.count(l) <= lista_pretendentes.count(l)):
                    ordenação_TOTAL.append(l)

for i in ordenação_TOTAL:
    print(f'{i[1]}, {i[0]}')

#Exemplo de entrada:
    #7
    #Guido Batista 195 110
    #Heitor Tostes 180 75
    #Bruno Costa 180 75
    #Joao Kleber 180 65
    #Rafael Rodrigues 165 110
    #Ricardo Neto 170 70
    #Juca Carvalho 180 77

#Saida:
    #Costa, Bruno
    #Tostes, Heitor
    #Kleber, Joao
    #Carvalho, Juca
    #Neto, Ricardo
    #Batista, Guido
    #Rodrigues, Rafael
