from game.console import Console
from game.core import Game, Player


console = Console()
player = Player("TestPlayer")

game = Game(
    name="TestGame",
    console=console,
    player=player
)
game.start()
