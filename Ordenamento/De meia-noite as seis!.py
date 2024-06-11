#De meia-noite as seis!
#Em uma escola tem ha necessidade de verificar se o conteudo de aula foi ensinado ou não, o professor tem que 3 turnos
#A primira entra corresponde aos dias de aula e a quantidade de conteudo.
#Em seguida é passado os conteudo, podendo ser o conteudo programado ou não.
#Para cada caso de teste imprima a mensagem "Bora ralar: {conteudo}", com os conteúdos que você estudará na madrugada, em ordem alfabética.
#Se não houver conteúdo para estudar, chame o Prof. Zigotto para para um projeto de pesquisa com a mensagem "It's in the box!" (ele entenderá o significado).
#Caso algum professor tenha apresentado conteúdo fora do previsto, avise o Prof. Zigotto com a mensagem "You died!" (ele vai convidá-lo para uma partida de videogame).

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

N = int(input())
for i in range(N):
    letras = []
    conteudo = list(input())
    for i in range(3):
        aulas = list(input().strip())
        letras.extend(aulas)
    
    verificacao = letras[::]
    for i in letras:
        if i in conteudo:
            conteudo.remove(i)
            verificacao.remove(i)
    
    if len(verificacao) > 0:
        print('You died!')
    elif len(conteudo) > 0:
        ordenação = quickSort(conteudo)
        saida = ''
        for i in ordenação:
            if i not in saida:
                saida += i
        print(f'Bora ralar: {saida}')
    else:
        print( "It's in the box!")

'''
Exemplo de entrada:
    3
    ALMAANAGRAMADELAMA
    GRAMA
    ANDA
    LAMAEAMAL
    AUNBQUEMFAZEHAGENTE


    ZUUTQNNMHGFEEEEBAAA
    ALECRIMDOURADO
    WTF
    BATATA
    FTYF

Saida:
    It's in the box!
    It's in the box!
    You died!
    '''
