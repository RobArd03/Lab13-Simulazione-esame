from dataclasses import dataclass

from model.node import Node


@dataclass
class Edge:
    n1: Node
    n2: Node
    peso: int

    def __hash__(self):
        return hash((self.n1, self.n2))

    def __eq__(self, other):
        return (self.n1, self.n2) == (other.n, other.n2)

    def __str__(self):
        return f"{str(self.n1)}, {str(self.n2)}, {self.peso}"