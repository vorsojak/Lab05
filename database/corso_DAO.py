# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection, DBConnect


class corsoDAO:

    @staticmethod
    def get_corsi():
        cnx = get_connection()
        cursor = cnx.cursor()

        query = """select *
                 FROM corso"""

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @classmethod
    def get_matricole_corso(cls, corso):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = """select matricola
                         FROM iscrizione
                         WHERE codins=%s"""

        cursor.execute(query, (corso,))
        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res