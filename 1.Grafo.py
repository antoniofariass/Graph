from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista = []
        for e in self.N:
            for f in self.N:
                if e != f:
                    if (f+'-'+e) not in lista:
                        lista.append(e+'-'+f)
        for g in self.A:
            z = self.A[g].getV1()+"-"+self.A[g].getV2()
            y = self.A[g].getV2()+"-"+self.A[g].getV1()
            if z in lista:
                lista.remove(z)
            if y in lista:
                lista.remove(y)
        return lista
        

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True
        return False

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        lista1= []
        lista2 = []
        
        for h in self.A:
            lista1= self.A[h].getV1()+"-"+self.A[h].getV2()
            for i in self.A:
                lista2 = self.A[i].getV1()+"-"+self.A[i].getV2()
                if h == i:
                    continue
                if lista1 == lista2:
                    return True
        return False
    
    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        var = 0 
        for a in self.A:
            if V not in self.N:
                raise VerticeInvalidoException('O vértice não existe no grafo.')
            if V == self.A[a].getV1() or V == self.A[a].getV2():
                var +=1
                if self.A[a].getV1() == self.A[a].getV2():
                    var +=1
        return var
    
    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        aresta = []
        for b in self.A:
            if V not in self.N:
                raise VerticeInvalidoException("O vértice não existe no grafo.")
            if V == self.A[b].getV1() or V == self.A[b].getV2():
                aresta.append(self.A[b].getRotulo())
        return aresta
    
    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        vertices = 0 
        arestas = 0 
        
        for d in self.A:
            arestas += 1 
        for c in self.N:
            vertices += 1
        if vertices*(vertices-1)/2 == arestas:
            return True
        else:
            return False
    