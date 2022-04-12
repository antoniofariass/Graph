from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from itertools import combinations, permutations
from copy import deepcopy
import sys, io

class MeuGrafo(GrafoListaAdjacencia):
    
    def vertices_adjacentes(self,v):
        '''
        Provê uma lista de vértices adjacentes a um vértice dado como parametro. A lista terá o seguinte formato: [X,Y,W...]
        Onde X, Z e W são vértices no grafo que tem uma aresta entre o vértice V.
        :return: Uma lista com os pares de vértices adjacentes
        '''
        N = self.N
        lista = []
        for a in self.A:
            if(self.A[a].getV1() == v):
                lista.append(self.A[a].getV2())
            if(self.A[a].getV2() == v):
                lista.append(self.A[a].getV1())           
        return lista    

    def ehEuleriano(self):
        '''
        Verifica se o grafo é euleriano
        :return 0: Se o grafo não tiver nenhuma aresta com grau ímpar
        :return 1: Se o grafo não for euleriano (ter apenas 1 aresta ímpar ou mais de 2)
        :return 2: Se o grafo tiver 2 arestas com grau ímpar
        '''
        if(self.conexo() == False):
            return 1
        else:
            grau = 0
            for i in self.N:
                if(self.grau(i) %2 != 0):
                    grau = grau+1
        if grau == 0:
            return 0
        elif grau == 2:
            return 2
        else:
            return 1

    def __arestaValidaEuler(euler,a):
        '''
        Verifica se uma aresta a pode ser passada como 
        próximo caminho do caminho euleriano
        :return: Um valor booleano que indica se a aresta pode ser o caminho
        '''
        u = euler.A[a].getV1()
        v = euler.A[a].getV2()

        if(euler.vertices_adjacentes(u) == [v]):
            return True
        else:
            contador1 = euler.dfs(u)
            euler.removeAresta(a)
            contador2 = euler.dfs(u)
            euler.adicionaAresta(a,u,v)
            return False if len(contador1.N) > len(contador2.N) else True
                       
    def __exibirEuler(euler,u):
        '''
        Adiciona o caminho euleriano em uma lista, começando do vértice u,
        passado como parametro em exibirCaminho()
        '''
        grafo = []
        for i in euler.A:
            if (u in euler.A[i].getV1() or u in euler.A[i].getV2()):
                grafo = [euler.A[i].getV1(),euler.A[i].getV2()]
                break
        if(grafo == []):
            return 0
        for v in grafo:
            if u!=v:
                if(euler.__arestaValidaEuler(i)):
                    if(len(euler.visitados)>0):
                        euler.visitados.append(i)
                        euler.visitados.append(v)
                    if(len(euler.visitados)==0):
                        euler.visitados.append(u)
                        euler.visitados.append(i)
                        euler.visitados.append(v)
                    euler.removeAresta(i)
                    euler.__exibirEuler(v)
                        
    
    def exibirCaminho(self):
        '''
        A função principal que exibe o caminho euleriano. Ela primeiro verifica
        se o grafo é euleriano. Se ele for, a função chama _exibirEuler() para
        printar o caminho.
        :return: Uma lista com o caminho euleriano
        '''
        
        euler = deepcopy(self)

        euler.visitados = []
        if(euler.ehEuleriano() == 1):
            return 'O grafo não é euleriano.'
        if(euler.ehEuleriano() == 0):
            u = euler.N[0]
        else:
            for i in euler.N:
                if(euler.grau(i) %2 != 0):
                    u = i
                    break
        euler.__exibirEuler(u)
        return euler.visitados          

