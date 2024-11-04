import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_initialization(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_search(self):
        result = self.stats.search("Semenko")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Semenko")

    def test_team(self):
        players = self.stats.team("PIT")
        self.assertEqual(len(players), 1)

    def test_top(self):
        top = self.stats.top(0)
        self.assertEqual(top[0].name, "Gretzky")

    def test_search_no_name_found(self):
        result = self.stats.search("Julia")
        self.assertIsNone(result)

    def test_search_sorting(self):
        best = self.stats.top(0, SortBy.GOALS)
        self.assertEqual(best[0].name, "Lemieux")

