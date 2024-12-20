import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player import Player

def main():
    console = Console()
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = Prompt.ask("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]:").upper()

    console.print(f"\nTop scorers of {nationality} season 2023-24", style="bold cyan")

    players = stats.top_scorers_by_nationality(nationality)
    table = Table(title="")

    #luodaan taulukko
    table.add_column("name", style="cyan", no_wrap=True)
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="yellow")
    table.add_column("points", justify="right", style="bold")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console.print(table)

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
