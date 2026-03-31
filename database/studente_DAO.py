# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection


class studenteDAO:

    @classmethod
    def get_studenti(cls):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = """select *
                            FROM studente"""

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res