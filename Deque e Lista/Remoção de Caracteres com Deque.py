#Remoção de Caracteres com Deque
#Este adiciona numeros no final da lista e letras no começo no demorrer que aparecem
#Ao encontrar um '+' e removido do final da lista, e se encontrar um '*' do começo.

from collections import deque
entrada = input()
string = deque([])
saida = deque([])
resul = ''
for i in entrada:
    if i.isnumeric():
        string.append(i)
    elif i != '*' and i != '+':
        string.appendleft(i)
    if i == '*':
        saida.append(string[0])
        string.popleft()
    if i == '+':
        saida.append(string[-1])
        string.pop()
for i in saida:
    resul += i
print(resul)

#Exemplo de entrada:
    #.nohtyp83 > c**********+*+

#Saida:
    #c > python3.8
