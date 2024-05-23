#Real Life LightSaber Combat Academy
#Este imprime uma lista de nomes em ordem da direita ou esquerda apartir da posição desejada
#Para manipular a estrutura deque, assuma que os seguintes métodos foram implementados:
#is_empty, add_front, add_rear, remove_front, remove_rear e size .

def exibe_candidatos(deque, pos, ordem):
    tamanho = deque.size()
    lista = []
    if pos > tamanho:
        tamanho = deque.size()
    else:
        for i in range(tamanho):
            lista.append(deque.remove_front())
        if ordem == 'direta':
            for i in lista[pos:]:
                print(i)
        else:
            inverso = lista[::-1]
            for j in inverso[-(pos+1):]:
                print(j)


#Exemplo de entrada:
    '''deque.add_rear('Obi-Wan Kenobi')
    deque.add_rear('Leia Skywalker')
    deque.add_rear('Chewbacca')
    deque.add_rear('Boba Fett')
    deque.add_rear('Yoda')
    deque.add_rear('Anakin Skywalker')
    deque.add_rear('Darth Vader')
    deque.add_rear('Ben Solo')
    deque.add_rear('Kylo Ren')
    deque.add_rear('Luke Skywalker')
    deque.add_rear('Leia Organa')
    deque.add_rear('R2-D2')
    deque.add_rear('C-3PO')
    deque.add_rear('BB-8')
    deque.add_rear('Han Solo')
    deque.add_rear('Padmé Amidala')
    deque.add_rear('Mace Windu')
    deque.add_rear('Qui-Gon Jinn')
    deque.add_rear('Vice Almirante Holdo')
    deque.add_rear('Rose Tico')
    deque.add_rear('Poe Dameron')
    deque.add_rear('Lando Calrissian')
    deque.add_rear('Darth Maul')
    deque.add_rear('Red Boba Fett')
    deque.add_rear('Jabba, the Hutt')
    deque.add_rear('Jango Fett')
    deque.add_rear('Conde Dooku')
    deque.add_rear('Darth Tyranus')
    deque.add_rear('General Grievous')
    deque.add_rear('Sheev Palpatine')
    deque.add_rear('Darth Sidious')
    deque.add_rear('Finn')
    deque.add_rear('Maz Kanata')
    deque.add_rear('Rey Palpatine')
    deque.add_rear('Rey Skywalker')
    deque.add_rear('Ben Solo')
    deque.add_rear('Kylo Ren')
    deque.add_rear('Líder Supremo Snoke')
    exibe_candidatos(deque, 2, 'direta')'''

#Saida: 
    '''Chewbacca
    Boba Fett
    Yoda
    Anakin Skywalker
    Darth Vader
    Ben Solo
    Kylo Ren
    Luke Skywalker
    Leia Organa
    R2-D2
    C-3PO
    BB-8
    Han Solo
    Padmé Amidala
    Mace Windu
    Qui-Gon Jinn
    Vice Almirante Holdo
    Rose Tico
    Poe Dameron
    Lando Calrissian
    Darth Maul
    Red Boba Fett
    Jabba, the Hutt
    Jango Fett
    Conde Dooku
    Darth Tyranus
    General Grievous
    Sheev Palpatine
    Darth Sidious
    Finn
    Maz Kanata
    Rey Palpatine
    Rey Skywalker
    Ben Solo
    Kylo Ren
    Líder Supremo Snoke'''



                
