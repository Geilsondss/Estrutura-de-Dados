#Caminhos em Grafos
#Esta questão pede que seja impresso todos os caminhos possiveis de um elemento a outro.
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}


    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight


    def getConnections(self):
        return self.connectedTo.keys()


    def getId(self):
        return self.id


    def getWeight(self, nbr):
       return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex


    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]

        else:
            return None


    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)

        if t not in self.vertList:
            nv = self.addVertex(t)
            
        self.vertList[f].addNeighbor(self.vertList[t], weight)


    def getVertices(self):
        return self.vertList.keys()
    
#O codigo era pra usar como ponto de partida,
#para implementar uma função que imprimisse todos os possiveis caminhos para chegar em uma vertice.


def encontrar_caminhos(grafo, saida, chegada):
    grafo = grafo.vertList
    caminhos = []
    
    if saida not in grafo or chegada not in grafo:
        return caminhos
    
    def profundidade(elemento, caminhos, lista, visitou):
        visitou[elemento.getId()] = True
        lista.append(elemento.getId())
        
        if elemento.getId() == chegada:
            caminhos.append(lista[:])
            
        else:
            for Ad in elemento.getConnections():
                if not visitou[Ad.getId()]:
                    profundidade(Ad, caminhos, lista, visitou)
        
        visitou[elemento.getId()] = False
        lista.pop()

    visitou = {}
    for p in grafo:
        visitou[p] = False
    
    lista = []
    profundidade(grafo[saida], caminhos, lista, visitou)
    return caminhos

#Exemplo de entrada:
    #g = Graph()
    #g.addEdge("i","x")
    #g.addEdge("x","j")
    #g.addEdge("i","z")
    #g.addEdge("z","j")
    #print(encontrar_caminhos(g,"i","j"))

#Saida: [['i', 'x', 'j'], ['i', 'z', 'j']]

