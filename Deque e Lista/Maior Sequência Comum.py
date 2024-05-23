#Maior Sequência Comum
#Este algoritmo imprime o maior valor de sequencias em comum entre duas strings

def sequencia(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    
    confere = [[0] * (n + 1) for k in range(m + 1)]
    comprimento = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                confere[i][j] = confere[i - 1][j - 1] + 1
                comprimento = max(comprimento, confere[i][j])

    return comprimento

sarscov2 = input().strip()
influenza = input().strip()
verifica = sequencia(sarscov2, influenza)

print(len(sarscov2))
print(len(influenza))
print(verifica)


#Entradas:
    #TAACAAACCAACCAAC
    #AAAGT

#Saida:
    #16
    #5
    #3
