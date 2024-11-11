import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader():
    def __init__(self, url):
        self._url=url

    def get_player(self):
        response = requests.get(self._url).json()
        print("Players from FIN\n")

        players = []


        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players



class PlayerStats(PlayerReader):
    def __init__(self, reader):
        self.players = reader.get_player()

    def top_scorers_by_nationality(self, nationality):
        finnish_players = [player for player in self.players if player.nationality == "FIN"]
        finnish_players.sort(key=lambda x: x.points, reverse=True)

        return finnish_players



if __name__ == "__main__":
    main()
