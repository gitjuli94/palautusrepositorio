class Ostoskori:
    def __init__(self):
        self._tuotteet = []

    def lisaa(self, tuote):
        self._tuotteet.append(tuote)

    def poista(self, tuote):
        for i,t in enumerate(self._tuotteet):
            if t.id == tuote.id:
                del self._tuotteet[i]
        """self._tuotteet = list(
            filter(lambda t: t.id != tuote.id, self._tuotteet)
        )"""

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
