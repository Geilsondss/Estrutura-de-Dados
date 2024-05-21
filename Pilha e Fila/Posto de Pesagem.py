#Posto de Pesagem
#Apos fortes chuvas foi necessario haver um limite de peso passa passar  na passarela.
#Então foi criado um codigo que verifica se os veiculos estao no limite do peso, e caso passe tera que voltar ao final da fila
#Algumas regras foram tomadas, se amostra=1, os fiscais verificam todos os veículos.
#Para amostra=2, os veículos são fiscalizados alternadamente, isto é, se um veículo é fiscalizado, o próximo veículo é liberado para seguir viagem.
#No final é impresso o tempo total que todos os veiculos levaram para atravessar o posto.

from collections import deque
quant_veiculo, amostra, limi_peso = map(int,input().split())
tempo = 0
cont = 0
veiculos = deque([])
entrada = list(map(int,input().split()))
for i in entrada:
    veiculos.append(i)
    
def fiscaliza(n):
    mud = veiculos[n] - 2
    veiculos.popleft()
    veiculos.append(mud)
        
def igual_1(n):
    global tempo
    if veiculos[n] <= limi_peso:
        tempo += 5
        veiculos.popleft()
    else:
        fiscaliza(n)
        tempo += 10

def diferente_1(n): 
    global tempo
    global cont
    if cont % amostra == 0:
        if veiculos[n] <= limi_peso:
            tempo += 5
            cont = 0
            veiculos.popleft()
        else:
            fiscaliza(n)
            tempo += 10
    else:
        tempo += 1
        veiculos.popleft()
    cont += 1

while len(veiculos)!= 0:
    if amostra == 1:
        igual_1(0)
    else:
        diferente_1(0)
print(tempo)

#Exempo de entrada:
    #5 1 7
    #4 2 6 3 9

#Saida: 35
