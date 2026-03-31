import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def lista_corsi(self):
        lista_corsi = self._model.get_corsi()
        res=[]
        for corso in lista_corsi:
            res.append(
                ft.dropdown.Option(
                    key=corso.codins,
                    text=corso.__str__()
                )
            )
        return res

    def cerca_iscritti(self, e):
        self._view._lvOut.controls.clear()
        corso = self._view._dd_corsi.value
        if corso is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un corso", color="red")
            )
            self._view.update_page()
            return

        studenti = self._model.cerca_iscritti(corso)
        self._view._lvOut.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti al corso: "))
        for studente in studenti:
            print(studente)
            self._view._lvOut.controls.append(
                ft.Text(studente)
            )
            self._view.update_page()



    def cerca_studente(self, e):
        self._view._lvOut.controls.clear()

        matricola = self._view._txt_matricola.value
        if matricola is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona una matricola", color="red")
            )
            self._view.update_page()
            return
        studente = self._model.cerca_matricola(matricola)
        if studente is None:
            self._view._lvOut.controls.append(
                ft.Text(f"Attenzione! Studente con matricola {matricola} non presente.", color="red")
            )
            self._view.update_page()
            return
        self._view._txt_nome.value = studente.nome
        self._view._txt_cognome.value = studente.cognome
        self._view.update_page()
        return


    def cerca_corsi(self, e):
        self._view._lvOut.controls.clear()

        matricola = self._view._txt_matricola.value
        if matricola is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona una matricola", color="red")
            )
            self._view.update_page()
            return
        studente = self._model.cerca_matricola(matricola)
        if studente is None:
            self._view._lvOut.controls.append(
                ft.Text(f"Attenzione! Studente con matricola {matricola} non presente.", color="red")
            )
            self._view.update_page()
            return
        lista_corsi = self._model.cerca_corsi(matricola)
        self._view._lvOut.controls.append(
            ft.Text(f"Lo studente {matricola} è iscritto {len(lista_corsi)} a corsi:")
        )
        for corso in lista_corsi:
            self._view._lvOut.controls.append(
                ft.Text(corso)
            )
        self._view.update_page()
        return

    def iscrivi(self, e):
        self._view._lvOut.controls.clear()

        matricola = self._view._txt_matricola.value
        if matricola is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona una matricola", color="red")
            )
            self._view.update_page()
            return

        corso = self._view._dd_corsi.value
        if corso is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un corso", color="red")
            )
            self._view.update_page()
            return

        res = self._model.iscrivi(matricola, corso)
        if res == 1:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! matricola non presente nel db", color="red")
            )
            self._view.update_page()
            return
        self._view._lvOut.controls.append(
            ft.Text(f"Iscrizione della matricola {matricola} al corso {corso} effettuata correttamente!", color="green")
        )
        self._view.update_page()
        return


