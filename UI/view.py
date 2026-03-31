import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)


        # List View where the reply is printed
        self._lvOut= ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._dd_corsi = ft.Dropdown(label="Seleziona corso", options=self._controller.lista_corsi(), width=200)
        self._btn_cerca_iscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.cerca_iscritti, width=150)
        row1 = ft.Row([self._dd_corsi, self._btn_cerca_iscritti])

        self._txt_matricola = ft.TextField(label="matricola", width=200)
        self._txt_nome = ft.TextField(label="nome", width=200)
        self._txt_cognome = ft.TextField(label="cognome", width=200)
        row2 = ft.Row([self._txt_matricola, self._txt_nome, self._txt_cognome])

        self._btn_cerca_studente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.cerca_studente, width=150)
        self._btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.cerca_corsi, width=150)
        self._btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.iscrivi, width=150)
        row3 = ft.Row([self._btn_cerca_studente, self._btn_cerca_corsi, self._btn_iscrivi])
        self._page.add(row1, row2, row3, self._lvOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
