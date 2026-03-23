import flet as ft

class View(object):
    def __init__(self, page):
        # questa riga salva la pagina Flet passata dal main
        self._page = page
        # questa riga imposta il titolo della finestra
        self._page.title = "TdP 2024 - Indovina il Numero"
        # questa riga centra orizzontalmente il contenuto nella pagina
        self._page.horizontal_alignment = 'CENTER'
        # questa riga conterrà il titolo dell'app
        self._titolo = None
        # questa riga conterrà il riferimento al Controller
        self._controller = None

    def caricaInterfaccia(self):
        # questa riga crea il testo del titolo dell'app
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        # questa riga crea il campo di testo che mostra il numero massimo
        self._txtNmax = ft.TextField(
            label="Numero Max",
            value=str(self._controller.getNmax()),
            disabled=True
        )

        # questa riga crea il campo di testo che mostra i tentativi massimi
        self._txtTmax = ft.TextField(
            label="Numero tentativi massimo",
            value=str(self._controller.getTmax()),
            disabled=True
        )

        # questa riga crea il campo di testo che mostra i tentativi rimanenti
        self._txtT = ft.TextField(
            label="Tentativi rimanenti",
            value=str(self._controller.getTmax()),
            disabled=True
        )

        # questa riga crea una riga orizzontale con i tre campi informativi
        self._row1 = ft.Row(controls=[self._txtNmax, self._txtTmax, self._txtT])

        # questa riga crea il campo di testo dove l'utente inserisce il tentativo
        self._txtInTentativo = ft.TextField(label="Valore")

        # questa riga crea il pulsante "Nuova partita" collegato al metodo reset del controller
        self._btnReset = ft.ElevatedButton(
            text="Nuova partita",
            on_click=self._controller.reset
        )

        # questa riga crea il pulsante "Indovina" collegato al metodo play del controller
        self._btnPlay = ft.ElevatedButton(
            text="Indovina",
            on_click=self._controller.play
        )

        # questa riga crea una riga con campo di input + due pulsanti
        self._row2 = ft.Row(controls=[self._txtInTentativo, self._btnReset, self._btnPlay])

        # questa riga crea una ListView che conterrà i messaggi di output
        self._lvOut = ft.ListView(expand=True)

        # questa riga aggiunge tutti i controlli alla pagina
        self._page.add(self._titolo, self._row1, self._row2, self._lvOut)
        # questa riga forza l'aggiornamento della pagina
        self._page.update()

    def setController(self, controller):
        # questa riga collega la View al suo Controller
        self._controller = controller

    def update(self):
        # questa riga aggiorna la pagina Flet dopo modifiche ai controlli
        self._page.update()