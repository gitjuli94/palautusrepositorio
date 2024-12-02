KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.koko = 0

    def kuuluu(self, n):
        # kuuluuko luku listaan
        for i in range(0, self.koko):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):

        if not self.kuuluu(n):
            # lukua ei ole vielä joukossa
            self.ljono[self.koko] = n
            self.koko += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.koko % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kasvata_kokoa(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.koko + self.kasvatuskoko)
                self.kasvata_kokoa(taulukko_old, self.ljono)

    def poista(self, n):
        if not self.kuuluu(n):
                    return
        indeksi = self.ljono.index(n)
        self.järjestä(indeksi)
        self.koko -= 1

    def järjestä(self, n):
        for j in range(n, self.koko -1):
            self.ljono[j] = self.ljono[j + 1]
        self.ljono[-1] = 0

    def kasvata_kokoa(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        #poistetaan mahdolliset nollat perästä
        return self.ljono[:self.koko]

    @staticmethod
    def yhdiste(a, b):

        result = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            result.lisaa(luku)
        return result

    @staticmethod
    def leikkaus(a, b):
        result = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    result.lisaa(b_taulu[j])

        return result

    @staticmethod
    def erotus(a, b):
        result = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            result.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            result.poista(b_taulu[i])

        return result

    def __str__(self):
        if self.koko == 0:
            return "{}"
        elif self.koko == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.koko - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.koko - 1])
            tuotos = tuotos + "}"
            return tuotos
