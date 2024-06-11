#Divisores Primos
#Números primos gêmeos são pares de números primos (p1, p2) tais que p2=p1+2.
#Implemente uma função chamada primos_gemeos que recebe um número inteiro n
# e retorna os n primeiros pares de números primos gêmeos, conforme formatação indicada abaixo.

def verifique(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primos_gemeos(n):
    pares = []
    count = 0
    num = 2
    while count < n:
        if verifique(num) and verifique(num + 2):
            pares.append((num, num + 2))
            count += 1
        num += 1
    return pares

#Exemplo de entrada: 10

#Saida: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109)]

