# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection


class studenteDAO:

    @staticmethod
    def get_studenti():
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

    @staticmethod
    def get_corsi_matricola( matricola):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = """select codins
                    FROM iscrizione
                    WHERE matricola = %s"""

        cursor.execute(query, (matricola,))
        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def iscrivi_matricola_a_corso(matricola, codins):
        cnx = get_connection()

        cursor = cnx.cursor()
        query = """insert into iscrizione
                            (matricola, codins) values (%s, %s)"""
        cursor.execute(query, (matricola, codins,))

        cnx.commit()
        cursor.close()
        cnx.close()
        return