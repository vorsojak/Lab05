from database.corso_DAO import corsoDAO
from database.studente_DAO import studenteDAO
from model.corso import Corso
from model.studente import Studente


class Model:

    def __init__(self):
        pass

    def get_corsi(self):
        dati = corsoDAO.get_corsi()
        corsi = []
        print(dati)
        for i in dati:
            corsi.append(Corso(i[0],i[1],i[2],i[3]))
        return corsi

    def cerca_iscritti(self, corso):
        lista_matricole = corsoDAO.get_matricole_corso(corso)
        dati = studenteDAO.get_studenti()
        studenti_corso = []
        studenti = []
        for i in dati:
            if i[0] in lista_matricole:
                studenti_corso.append(i)
        for s in studenti_corso:
            studenti.append(Studente(s[0],s[1],s[2],s[3]))
        return studenti

    def cerca_matricola(self, matricola):
        dati = studenteDAO.get_studenti()
        for s in dati:
            if int(matricola) == int(s[0]):
                return Studente(s[0], s[1], s[2], s[3])
        return None

    def cerca_corsi(self, matricola):
        dati = studenteDAO.get_corsi_matricola(matricola)
        print(dati)
        dati_corsi = corsoDAO.get_corsi()
        print(dati_corsi)
        corsi = []
        for i in dati_corsi:
            if i[0] in dati:
                corsi.append(Corso(i[0],i[1],i[2],i[3]))
        return corsi

    def iscrivi(self, matricola, corso):
        studente = self.cerca_matricola(matricola)
        if studente is None:
            return 1
        studenteDAO.iscrivi_matricola_a_corso(matricola, corso)
        return 0










