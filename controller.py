from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        # questa riga salva il riferimento alla View
        self._view = view
        # questa riga crea il Model che gestisce la logica del gioco
        self._model = Model()
        # questa riga inizializza lo stato del gioco nel modello
        self._model.reset()
        # ATTENZIONE: qui NON tocco self._view._txtT perché ancora non esiste

    def reset(self, e):
        # questa riga resetta lo stato del gioco nel Model
        self._model.reset()
        # questa riga aggiorna il campo tentativi rimanenti nella View
        self._view._txtT.value = str(self._model.T)
        # questa riga svuota la lista dei messaggi di output
        self._view._lvOut.controls.clear()
        # questa riga aggiunge il messaggio iniziale nella ListView
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina il numero che sto pensando...")
        )
        # questa riga aggiorna la View per mostrare le modifiche
        self._view.update()

    def play(self, e):
        # questa riga legge il contenuto del TextField come stringa
        tentativoStr = self._view._txtInTentativo.value
        try:
            # questa riga converte la stringa in intero
            tentativo = int(tentativoStr)
        except ValueError:
            # questa riga aggiunge un messaggio di errore se l'input non è numerico
            self._view._lvOut.controls.append(
                ft.Text("Errore, devi inserire un valore numerico", color="red")
            )
            # questa riga aggiorna la View per mostrare il messaggio di errore
            self._view.update()
            # questa riga interrompe l'esecuzione del metodo
            return

        # questa riga chiede al Model di valutare il tentativo
        res = self._model.play(tentativo)
        # questa riga aggiorna il campo tentativi rimanenti nella View
        self._view._txtT.value = str(self._model.T)

        # questa riga controlla se l'utente ha indovinato
        if res == 0:
            # questa riga aggiunge un messaggio di vittoria in verde
            self._view._lvOut.controls.append(
                ft.Text(f"Hai vinto! Il valore corretto era: {tentativo}", color="green")
            )
            # questa riga aggiorna la View
            self._view.update()
            return

        # questa riga controlla se i tentativi sono finiti
        elif res == 2:
            # questa riga aggiunge un messaggio di sconfitta in rosso
            self._view._lvOut.controls.append(
                ft.Text(f"Hai perso! Il valore corretto era: {self._model.segreto}",
                        color="red")
            )
            # questa riga aggiorna la View
            self._view.update()
            return

        # questa riga controlla se il segreto è più piccolo del tentativo
        elif res == -1:
            # questa riga aggiunge un messaggio che dice che il segreto è più piccolo
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta! Il segreto è più piccolo di {tentativo}")
            )
            # questa riga aggiorna la View
            self._view.update()
            return

        else:
            # questa riga aggiunge un messaggio che dice che il segreto è più grande
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta! Il segreto è più grande di {tentativo}")
            )
            # questa riga aggiorna la View
            self._view.update()
            return

    def getNmax(self):
        # questa riga restituisce il valore Nmax dal Model
        return self._model.Nmax

    def getTmax(self):
        # questa riga restituisce il valore Tmax dal Model
        return self._model.Tmax