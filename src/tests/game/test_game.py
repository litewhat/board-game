from unittest import TestCase

from game.core import Game, Player
from game.console import Console
from game.exceptions import GameStoppedException


class GameCreationTestCase(TestCase):
    def test_console_none(self):
        with self.assertRaises(TypeError):
            Game(name="TestGame", console=None, player=Player("TestPlayer"))

    def test_player_none(self):
        with self.assertRaises(TypeError):
            Game(name="TestGame", console=Console(), player=None)

    def test_game_attributes(self):
        console = Console()
        player = Player("TestPlayer")
        game = Game(name="TestGame", console=console, player=player)
        self.assertEqual(game.name, "TestGame")
        self.assertEqual(game.console, console)
        self.assertEqual(game.player, player)
        self.assertEqual(game.exceptions, [])
        self.assertEqual(game.actions, [])
        self.assertEqual(game.running, False)
        self.assertEqual(game.stopped,  False)


class GameStartTestCase(TestCase):
    def test_started(self):
        game = Game(name="TestGame", console=Console(), player=Player("TestPlayer"))
        game.start(running_mode='test')
        self.assertEqual(game.running, True)

    def test_started_after_stopped(self):
        game = Game(name="TestGame", console=Console(), player=Player("TestPlayer"))
        with self.assertRaises(GameStoppedException):
            game.stop()
            game.start(running_mode='test')
