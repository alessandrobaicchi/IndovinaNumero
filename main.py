import flet as ft
from controller import Controller
from view import View

def main(page: ft.Page):
    # questa riga crea l'oggetto View e gli passa la pagina Flet
    v = View(page)
    # questa riga crea il Controller e gli passa la View
    c = Controller(v)
    # questa riga dice alla View qual è il suo Controller
    v.setController(c)
    # questa riga costruisce e carica tutta l'interfaccia grafica
    v.caricaInterfaccia()

# questa riga avvia l'app Flet usando la funzione main come entry point
ft.app(target=main)