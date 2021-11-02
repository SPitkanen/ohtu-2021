import unittest
from statistics import Statistics
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
class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_find_gretzky(self):
        player = self.statistics.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_wrong_player_retrurns_none(self):
        player = self.statistics.search("nhl")
        self.assertEqual(player, None)

    def test_find_players_of_team(self):
        players = self.statistics.team("EDM")
        self.assertEqual(len(players), 3)

    def test_find_correct_top_scorer(self):
        top = self.statistics.top_scorers(1)
        self.assertEqual(top[0].name, "Gretzky")