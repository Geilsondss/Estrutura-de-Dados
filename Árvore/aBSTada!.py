#aBSTada!
#Este código inseri elementos em um arvore em pos-ordem,pre-ordem e em-ordem

class Inicializar:
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None

class Abstada:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, dado):
        global RAIZ
        if self.raiz == None:
            self.raiz = Inicializar(dado)
            RAIZ = self.raiz
        else:
            self.ordenar(self.raiz, dado)
            RAIZ = self.raiz
    
    def ordenar(self, n, elemento):
        if elemento < n.elemento:
            if n.esquerda == None:
                n.esquerda = Inicializar(elemento)
            else:
                self.ordenar(n.esquerda, elemento)
        
        elif elemento > n.elemento:
            if n.direita == None:
                n.direita = Inicializar(elemento)
            else:
                self.ordenar(n.direita, elemento)
        
    def infixa(self, no):
        if no != None:
            self.infixa(no.esquerda)
            print(no.elemento, end = ' ')
            self.infixa(no.direita)
    
    def prefixa(self, no):
        if no != None:
            print(no.elemento, end = ' ')
            self.prefixa(no.esquerda)
            self.prefixa(no.direita)
    
    def posfixa(self, no):
        if no != None:
            self.posfixa(no.esquerda)
            self.posfixa(no.direita)
            print(no.elemento, end = ' ')

arvore = Abstada()
cont = 0
while True:
    entrada = input()
    if (entrada == 'in' or entrada == 'pre' or entrada == 'pos') and cont == 0:
        print(' ')
    else:
        if entrada == 'quack':
            break
        if entrada == 'in':
            (arvore.infixa(RAIZ))
            print()
        elif entrada == 'pre':
            (arvore.prefixa(RAIZ))
            print()
        elif entrada == 'pos':
            (arvore.posfixa(RAIZ))
            print()
        else:
            cont = 1
            arvore.inserir(int(entrada))


#Exemplo de entrada:
    #4
    #2
    #1
    #3
    #6
    #7
    #5
    #in
    #pre
    #pos
    #quack
            
#Saida:
    #1 2 3 4 5 6 7
    #4 2 1 3 6 5 7
    #1 3 2 5 7 6 4
    
