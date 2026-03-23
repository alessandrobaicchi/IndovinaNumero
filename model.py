import random

class Model(object):
    def __init__(self):
        # questa riga imposta il valore massimo del numero segreto
        self._Nmax = 100
        # questa riga imposta il numero massimo di tentativi
        self._Tmax = 6
        # questa riga inizializza i tentativi rimanenti al massimo
        self._T = self._Tmax
        # questa riga conterrà il numero segreto da indovinare
        self._segreto = None

    def reset(self):
        # questa riga sceglie un nuovo numero segreto casuale tra 1 e Nmax
        self._segreto = random.randint(1, self._Nmax)
        # questa riga ripristina i tentativi rimanenti al valore massimo
        self._T = self._Tmax
        # questa riga stampa il segreto in console (utile per debug)
        print(self._segreto)

    def play(self, tentativo):
        # questa riga consuma un tentativo (decrementa il contatore)
        self._T -= 1

        # questa riga controlla se il tentativo è esattamente uguale al segreto
        if tentativo == self._segreto:
            # questa riga indica che l'utente ha indovinato
            return 0

        # questa riga controlla se i tentativi sono finiti
        if self._T == 0:
            # questa riga indica che non ci sono più tentativi disponibili
            return 2

        # questa riga controlla se il tentativo è maggiore del segreto
        if tentativo > self._segreto:
            # questa riga indica che il segreto è più piccolo del tentativo
            return -1
        else:
            # questa riga indica che il segreto è più grande del tentativo
            return 1

    @property
    def Nmax(self):
        # questa riga restituisce il valore massimo del numero segreto
        return self._Nmax

    @property
    def Tmax(self):
        # questa riga restituisce il numero massimo di tentativi
        return self._Tmax

    @property
    def T(self):
        # questa riga restituisce il numero di tentativi rimanenti
        return self._T

    @property
    def segreto(self):
        # questa riga restituisce il numero segreto corrente
        return self._segreto