import random

class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._T = self._Tmax
        self._segreto = None

    def reset(self):
        """Questo metodo resetta lo stato del gioco. Imposta il segreto a un valore randomico fra 0 e NMax
        e ripristina il numero di tentativi rimanenti."""
        self._segreto = random.randint(0, self._Nmax)
        self._T = self._Tmax
        print(self._segreto)


    def play(self, tentativo):
        """Questo metodo riceve come argomento un valore intero, che sarà il tentativo del giocatore e
        lo confronta con il segreto, se il return è:
        -1 --> il segreto è più piccolo del tentativo
        0  --> il segreto è uguale al tentativo
        1  --> il segreto è più grande del tentativo
        2  --> non ci sono più tentativi per giocare"""

        self._T -= 1

        if tentativo == self._segreto:
            """L'utente ha vinto"""
            return 0

        if self._T == 0:
            """Non ci sono più tentativi, quindi non puoi più giocare"""
            return 2

        if tentativo > self._segreto:
            """Il tentativo dell'utente è più grande del segreto"""
            return -1
        else:
            """Il tentativo dell'utente è più piccolo del segreto"""
            return 1


    @property
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto


if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(70))
    print(m.play(80))
    print(m.play(60))
    print(m.play(50))


