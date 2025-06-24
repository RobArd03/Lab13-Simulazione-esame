from dataclasses import dataclass


@dataclass
class Node:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: str
    nationality: str
    url: str

    def __hash__(self):
        return hash(self.driverId)
    def __eq__(self, other):
        return self.driverId == other.driverId
    def __str__(self):
        return self.surname
    def __repr__(self):
        return self.surname