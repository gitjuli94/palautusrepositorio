class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.edellinen = None

    def miinus(self, operandi):
        self.edellinen = self._arvo
        self._arvo = self._arvo - operandi


    def plus(self, operandi):
        self.edellinen = self._arvo
        self._arvo = self._arvo + operandi


    def nollaa(self):
        self.edellinen = self._arvo
        self._arvo = 0


    def aseta_arvo(self, arvo):
        self.edellinen = self._arvo
        self._arvo = arvo


    def arvo(self):
        return self._arvo

    def kumoa(self):
        self._arvo = self.edellinen
