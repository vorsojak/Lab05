import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


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
        matricola = self._view._txt_matricola
        if matricola is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona una matricola", color="red")
            )
            self._view.update_page()
            return
        self._model.cerca_matricola(matricola)


def cerca_corsi(self, e):
        pass

    def iscrivi(self, e):
        pass

