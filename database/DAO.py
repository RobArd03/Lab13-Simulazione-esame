from database.DB_connect import DBConnect
from model.edge import Edge
from model.node import Node


class DAO():

    @staticmethod
    def getAllEdges(year: int, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
                select  r1.driverId as d1, r2.driverId as d2, COUNT(*) as peso
                from results r1, results r2, races re
                where r1.raceId = r2.raceId
                and re.raceId = r1.raceId
                and re.`year` = %s
                and r1.`position` is not NULL 
                and r2.`position` is not NULL
                and r1.`position` < r2.`position`
                GROUP BY r1.driverId, r2.driverId
                """
        cursor.execute(query, (year, ))

        for row in cursor:
            result.append(Edge(idMap[row['d1']], idMap[row['d2']], row['peso']))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllNodes(year: int):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ 
                select DISTINCT d.*
                from drivers d, results r, races re
                where d.driverId = r.driverId
                and r.position is not null
                and r.raceId = re.raceId
                and re.`year` = %s
                """
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Node(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ 
                select s.`year`
                from seasons s 
                """
        cursor.execute(query)

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()

        return result
