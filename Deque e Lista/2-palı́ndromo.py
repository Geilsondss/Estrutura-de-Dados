#2-palı́ndromo
#Este código verifica se tem mais de um palindromo de 3 letras dentro de outra palavra
#Um um desses palindromos não pode estar dentro de outro

def palindromo(string):
    return string == string[::-1] and len(string) >= 3 and string not in palindrom

def palindromo_2(word):
    global palindrom
    palindrom = []
    n = len(word)
    
 
    for i in range(n):
        for j in range(i + 2, n):
            substring = word[i:j+1]
            if palindromo(substring):
                palindrom.append(substring)
    for verificacao in palindrom:
        for busca in palindrom:
            if verificacao != busca and verificacao not in busca and busca not in verificacao:
                return True
    return False
            
palavras = input().split()
for word in palavras:
    if word == word[::-1]:
        continue
    else:
        if palindromo_2(word):
            if len(palindrom) >= 2:
                print(word)

#Entrada:
    #NAOSOUPALINDROMO AAAA SOCORRAMESUBINOONIBUSEMMARROCOS MESTREYODA

#Saida:
    #NAOSOUPALINDROMO
     #SOCORRAMESUBINOONIBUSEMMARROCOS

                


