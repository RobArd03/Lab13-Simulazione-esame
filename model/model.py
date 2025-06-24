import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes = []
        self._edges = []
        self._idMap = {}
        self._Path = []
        self._minSconf = 100000

    def setYear(self):
        return DAO.getAllYears()

    def buildGraph(self, year):
        self._graph.clear()
        self.addAllNodes(year)
        self.addAllEdges(year)

    def addAllNodes(self, y):
        self._nodes = DAO.getAllNodes(y)
        self._graph.add_nodes_from(self._nodes)
        for n in self._nodes:
            self._idMap[n.driverId] = n

    def addAllEdges(self, year):
        self._edges = DAO.getAllEdges(year, self._idMap)
        for e in self._edges:
            self._graph.add_edge(e.n1, e.n2, weight=e.peso)

    def getDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getNodes(self):
        return self._nodes

    def getEdges(self):
        return self._edges

    def bestDriver(self):
        nodo = None
        migliore = -1000
        for n in self._nodes:
            intL = self._graph.in_edges(n)
            outL = self._graph.out_edges(n)
            pesoI = 0
            pesoO = 0
            for u, v in intL:
                pesoI += self._graph[u][v]["weight"]
            for u, v in outL:
                pesoO += self._graph[u][v]["weight"]
            out = pesoO
            int = pesoI
            if out-int > migliore:
                migliore = out-int
                nodo = n

        return nodo, migliore

    def dreamTeam(self, k:int):
        parziale = []
        self._minSconf = 100000
        self._path = []
        rimanenti = copy.deepcopy(self._nodes)

        self._ricorsione ( parziale, rimanenti, k)
        print(1)
        return self._path, self._minSconf

    def _ricorsione(self, parziale, rimanenti, k):
        print(2)
        score = self._calcolaScore(parziale)
        if len(parziale) == k and score < self._minSconf:
            self._minSconf = score
            self._path = copy.deepcopy(parziale)
        if len(parziale) < k:
            for n in rimanenti:
                if n not in parziale:
                    parziale.append(n)
                    rimanenti.remove(n)
                    self._ricorsione(parziale, rimanenti, k)
                    parziale.pop()
                    rimanenti.append(n)

    def _calcolaScore(self, nodes):
        if len(nodes) > 0:
            s = 0
            for node in nodes:
                for v, n in self._graph.in_edges(node):
                    if v not in nodes:
                        s += self._graph[v][n]["weight"]
        else:
            s = 1000000
        return s






