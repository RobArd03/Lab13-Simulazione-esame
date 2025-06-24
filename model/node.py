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