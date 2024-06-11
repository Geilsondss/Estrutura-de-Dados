#copy + patch
#Esta questão de para calcular o tempo de transfetencia de um arquivo em bytes
#A ideia é simples, basta estimar o tempo restante assumindo que a taxa de transferência será mantida para os bytes que ainda não foram enviados.
#Implemente um patch para realizar esta tarefa adequadamente.
#a cada 5 entradas ele diz o tempo restante

tamanho_arq = int(input())
cont = 0
lista = []
nada = 0
restante = tamanho_arq
entradas1 = 0 
entradas2 = 0
print(f'Transmitindo {tamanho_arq} bytes...')

while True:
    by = int(input())
    lista.append(by)
    restante -= by
    entradas1 += by
    entradas2 += by
    cont += 1
    if restante <= 0:
        break
    
    if cont % 5 == 0:
        for i in lista:
            nada += i
        if nada == 0:
            print('Tempo restante: pendente...')
        else:
            mud_tempo = (entradas1 / 5)
            tempo =(tamanho_arq - entradas2 ) / mud_tempo
            tempo = round(tempo,4)
            entradas1 = 0
            if tempo > 0 and tempo < 1:
                print(f'Tempo restante: {int(tempo+1)} segundos.')
            else:
                if (tempo / (int(tempo))) > 1:
                    print(f'Tempo restante: {int(tempo+1)} segundos.')
                else:
                    print(f'Tempo restante: {int(tempo)} segundos.')
        nada = 0
        lista = []
    
print(f'Tempo total: {cont} segundos.')

'''
Exemplo de entrada:
    100
    10
    20
    20
    0
    10
    0
    10
    0
    10
    0
    20

Saida:
    Transmitindo 100 bytes...
    Tempo restante: 4 segundos.
    Tempo restante: 5 segundos.
    Tempo total: 11 segundos.
    '''
