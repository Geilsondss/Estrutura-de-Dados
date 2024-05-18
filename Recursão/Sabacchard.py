#Sabacchard
#Este código é referente a um jogo de escolhas de cartas.
#Ele imprime o maior resultado possivel na soma de n/2 cartas.
def repetição(partidas, cartas):
    if partidas == 0:
        Sabacchard(0, cartas)
    if str(cartas) in dic:
        return dic[str(cartas)]
    descartar_ultimo = Sabacchard(partidas-1, cartas[:-1])
    descartar_primeiro = Sabacchard(partidas-1, cartas[1:])
    if descartar_ultimo > descartar_primeiro:
        dic[str(cartas)] = descartar_ultimo
        return descartar_ultimo
    else:
        dic[str(cartas)] = descartar_primeiro
        return descartar_primeiro
        
def Sabacchard(partidas, baralho):
    if partidas == 0:
        return 0
    ultimo = baralho[-1] + repetição(partidas-1, baralho[:-1])
    primeiro = baralho[0] + repetição(partidas-1, baralho[1:])
    if ultimo > primeiro:
        return ultimo
    else:
        return primeiro

jogadas = int(input())
cartas = list(map(int,input().split()))
dic = {}
print(Sabacchard(jogadas, cartas))

#Exemplos de entrada:
    #6
    #7 8 3 4 5 10
#Saida: 25
