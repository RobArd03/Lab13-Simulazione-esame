import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year = 0
        self._k = 0

    def fillDDYear(self):
        for y in self._model.setYear():
            self._view._ddAnno.options.append(ft.dropdown.Option(key = y, data = y, on_click=self.handleDDYearSelection))

    def handleDDYearSelection(self, e):
        self._year = int(e.control.data)

    def handleCreaGrafo(self,e):
        self._view.txt_result.controls.clear()

        self._model.buildGraph(self._year)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
        n, e = self._model.getDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {n}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {e}"))

        ne, s = self._model.bestDriver()
        self._view.txt_result.controls.append(ft.Text(f"Best driver: {ne}, con score {s}"))

        self._view.update_page()

    def handleCerca(self, e):
        self._view.txt_result.controls.clear()
        k = self._view._txtIntK.value
        if k == "":
            self._view.txt_result.controls.append(ft.Text("Inserire un valore K nel text field", color = "red"))
            self._view.update_page()
            return
        try:
            self._k = int(k)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un valore intero K", color = "red"))
            self._view.update_page()
            return


        p, s = self._model.dreamTeam(self._k)
        self._view.txt_result.controls.append(ft.Text(f"Perdite totali: {s}, di seguito i piloti"))
        for n in p:
            self._view.txt_result.controls.append(ft.Text(f"{n}"))
        self._view.update_page()

