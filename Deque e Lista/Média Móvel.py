#Média Móvel
#A média móvel simples sobre uma sequência P=(p1,…,pm) é a sequência P¯¯¯¯=(p¯¯¯1,…,p¯¯¯m−n+1)
#das médias das subsequências de n elementos consecutivos de P. Ou seja, dada a sequência
#P=(p1,…,pm), o cálculo de um termo qualquer da sequência resultante pela média móvel é dado por:
#p¯¯¯i=1n∑j=0n−1pi+j

def media_movel_simples(m, n, sequencia):
    medias = []
    soma = sum(sequencia[:n])
    medias.append(soma // n)

    for i in range(n, m):
        soma += sequencia[i] - sequencia[i - n]
        medias.append(soma // n)
    return medias

m, n = map(int, input().split())
sequencia = list(map(int, input().split()))

for media in media_movel_simples(m, n, sequencia):
    print(media)

#Exemplo de Entradas:
    #8 5
    #1024 999 898 1047 1560 1300 1420 1000

#Saida:
    #1105
    #1160
    #1245
    #1265
