from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from itertools import combinations, permutations
from copy import deepcopy
import sys, io

class MeuGrafo(GrafoListaAdjacencia):

    def ha_ciclo(self):
        '''
        Usando DFS, essa função percorre o grafo procurando por um ciclo.
        :return: uma lista no formato [v1, a1, v2, a2, v3, a3, …, an, v1] 
        (onde vx são vértices e ax são arestas) indicando os vértices e arestas que formam o ciclo.
        Se não existir nenhum ciclo no grafo, ele retorna 'False'.
        '''
        visitado = []
        for V in self.N:
            visitado.append(V)
            arestas_paralelas = []
            if(len(self.arestas_sobre_vertice(V))>1):
                for aresta in self.arestas_sobre_vertice(V):
                    if(self.A[aresta].getV1() == V):
                        arestas_paralelas.append(self.A[aresta].getV2())
                    if(self.A[aresta].getV2() == V):
                        arestas_paralelas.append(self.A[aresta].getV1())
            arestas_paralelas_2 = []
            for i in arestas_paralelas:
                if(len(self.arestas_sobre_vertice(i))>1):
                    arestas_paralelas_2.append(i)
            if(len(arestas_paralelas_2)>1):
             for i in self.A:
                try:
                 if([V,arestas_paralelas_2[0]] == [self.A[i].getV1(),self.A[i].getV2()]):
                    grafo = deepcopy(self)
                    grafo.removeAresta(i)
                    ciclo = grafo.caminho_dois_vertices(self.A[i].getV1(),self.A[i].getV2())
                    ciclo.append(i)
                    ciclo.append(self.A[i].getV1())
                    return ciclo
                 if([V,arestas_paralelas_2[0]] == [self.A[i].getV2(),self.A[i].getV1()]):
                    grafo = deepcopy(self)
                    grafo.removeAresta(i)
                    ciclo = grafo.caminho_dois_vertices(self.A[i].getV2(),self.A[i].getV1())
                    ciclo.append(i)
                    ciclo.append(self.A[i].getV2())
                    return ciclo
                except:
                    pass
        return False

    def caminho_dois_vertices(self, s, d):
        '''
        Função auxiliar que verifica se há um caminho entre 2 vértices.
        '''
        self.visited =[]
        self.path = []
        val = []
        aresta = ''
        self.lista_vertices = []

        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])

        def caminho_dois_vertices_rec(u, d, aresta):

            self.visited.append(u)
            self.path.append(u)
            if(u == d):
                print(self.path)
            else:
                for i in range(len(self.lista_vertices)):
                    if (u in self.lista_vertices[i]):
                        self.aresta = self.lista_vertices[i]
                        aresta2 = [self.aresta[0],self.aresta[1]]
                        for i in aresta2:
                            if i not in self.visited:
                                aresta = self.aresta[2]
                                caminho_dois_vertices_rec(i, d, aresta)

                self.path.remove(u)
        
        sys.stdout = io.StringIO()
        caminho_dois_vertices_rec(s, d, aresta)
        val = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__
        val = eval(val)
        caminho_lista = []
        for i in range(len(val)-1):
            caminho_lista.append(val[i])
            for a in self.A:
                if([self.A[a].getV1(),self.A[a].getV2()] == [val[i],val[i+1]]):
                    caminho_lista.append(a)
                if([self.A[a].getV2(),self.A[a].getV1()] == [val[i],val[i+1]]):
                    caminho_lista.append(a)
        caminho_lista.append(val[-1])
        return caminho_lista

    def caminho(self,n):
        '''
        Percorre o grafo para encontrar um caminho de comprimento n
        :param n: O tamanho do caminho a ser buscado
        :return: Uma lista no formato [v1, a1, v2, a2, v3, a3, ...] onde vx são vértices e ax são arestas
        Se não existir nenhum caminho com o tamanho dado, ele retorna 'None'
        '''
        N = self.N
        lista = [''.join(x) for x in permutations(N, 2)]
        for i in lista:
            path = self.caminho_dois_vertices(i[0],i[1])
            if len(path) == n * 2 + 1:
                return path

    def conexo(self):
        '''
        Função para analisar se o grafo é conexo ou não.
        :return: Um valor booleano que indica se o grafo é conexo.
        '''
        visitados = []
        vertices = self.N
        vertices_percorridos = self.dfs(vertices[0])
        if(len(self.N)==1):
            return True
        for i in vertices_percorridos.A:
            if(vertices_percorridos.A[i].getV1() not in visitados):
                visitados.append(vertices_percorridos.A[i].getV1())
            if(vertices_percorridos.A[i].getV2() not in visitados):
                visitados.append(vertices_percorridos.A[i].getV2())
        if(len(self.N) == len(visitados)):
            return True
        return False    
