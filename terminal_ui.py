from user_interface import UserInterface
from game import Game

class TerminalUI(UserInterface):
    """
    Implementation of UserInterface using the terminal
    """

    def __init__(self, game: Game = None, players: tuple = None) -> None:
        super().__init__(game, players)

    def set_game(self, game: Game) -> None:
        super().set_game(game)

    def set_players(self, *players) -> None:
        super().set_players(*players)

    def run_loop(self) -> None:
        super().run_loop()