#Fibonacci III
#Este código imprime quantas vezes uma fibonacci é chamado
lista = []
def fibonacci(n):
    global lista
    lista.append(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n -2)

entrada = int(input())
print(f'fibonacci({entrada}) = {fibonacci(entrada)}.')
for i in range(entrada+1):
    print(f'{lista.count(i)} chamada(s) a fibonacci({i}).')

#Exemplos de entrada: 4
#Saida:
    #fibonacci(4) = 3.
    #2 chamada(s) a fibonacci(0).
    #3 chamada(s) a fibonacci(1).
    #2 chamada(s) a fibonacci(2).
    #1 chamada(s) a fibonacci(3).
    #1 chamada(s) a fibonacci(4).



