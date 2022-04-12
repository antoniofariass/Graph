from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy


class MeuGrafo(GrafoListaAdjacencia):

    def bfs(self,V=''):
        '''
        Busca em largura primeiro, na qual provê um grafo bfs.
        :param V: A raiz do grafo, onde começa a busca.
        :return: Uma lista com um novo grafo.
        '''
        
        if(V not in self.N):
            raise(VerticeInvalidoException)
            
        vertices = deepcopy(self.N)
        bfs = MeuGrafo(vertices)
        visitado = [V]

        self.lista_vertices = []
        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])

        fila = []
        rotulos = []
        fila.append(V)

        for a in self.A:
                rotulos.append(self.A[a].getRotulo())
        
        while fila:
            s = fila.pop(0)

            for i in range(len(self.lista_vertices)):
                if(s in self.lista_vertices[i]):
                    aresta = self.lista_vertices[i]
                    aresta2 = [aresta[0],aresta[1]]

                    for i in aresta2:
                        if i not in visitado:
                            bfs.adicionaAresta(aresta[2], aresta[0], aresta[1])
                            fila.append(i)
                            fila = list(dict.fromkeys(fila))
                            visitado.append(i)
        return bfs
        

"""python -m unittest grafo_test.TestGrafo"""