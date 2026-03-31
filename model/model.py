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
        print(corso)
        lista_matricole = corsoDAO.get_matricole_corso(corso)
        print(lista_matricole)
        dati = studenteDAO.get_studenti()
        print(dati)
        studenti_corso = []
        studenti = []
        for i in dati:
            if i[0] in lista_matricole:
                studenti_corso.append(i)
        for s in studenti_corso:
            studenti.append(Studente(s[0],s[1],s[2],s[3]))
        print(studenti)
        return studenti

    def cerca_matricola(self, matricola):
        dati = studenteDAO.get_studenti()
        matricole = []
        for i in dati:
            matricole.append(i[0])
        if matricola in matricole:












