import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []
        self._idMap = {}
        self._Path = []

    def setYearColor(self):
        return DAO.getAllYears()

    def buildGraph(self, year):
        self._graph.clear()
        self._graph = nx.Graph()
        self.addAllNodes(year)
        self.addAllEdges(year)

    def addAllNodes(self, c):
        self._nodes = DAO.getAllNodes(c)
        self._graph.add_nodes_from(self._nodes)
        for n in self._nodes:
            self._idMap[n.Product_number] = n

    def addAllEdges(self, year, color):
        self._edges = DAO.getAllEdges(year, self._idMap)
        for e in self._edges:
            self._graph.add_edge(e.n1, e.n2, weight=e.peso)

    def getDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()