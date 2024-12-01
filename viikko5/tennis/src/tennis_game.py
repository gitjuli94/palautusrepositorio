class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._tied()
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._advantage_or_win()
        return self._normal()

    def _normal(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.m_score1]}-{score_names[self.m_score2]}"
    def _tied(self):
        score_names = ["Love-All", "Fifteen-All", "Thirty-All"]
        return score_names[self.m_score1] if self.m_score1 < 3 else "Deuce"

    def _advantage_or_win(self):
        minus_result = self.m_score1 - self.m_score2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"



