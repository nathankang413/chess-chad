from game import Game
from config import *

class UserInterface:
    """
    Abstract class for interfacing with the user for the Chess game
    Handles the main game loop and I/O with the user
    """

    def __init__(self, game: Game=None, players: tuple=None) -> None:
        """
        Creates a UserInterface object
        game - a game data structure to maintain and update the state and history of the game
        players - (white_player, black_player) - players may be a HUMAN_PLAYER or a Bot object
        """
        pass

    def set_game(self, game: Game) -> None:
        """
        Changes the game object to the given Game
        """
        pass

    def set_players(self, *players) -> None:
        """
        Changes the players to the given players
        players - one (1) tuple or mutiple players (HUMAN_PLAYER or Bot object)
        """
        pass

    def run_loop(self) -> None:
        """
        Runs the game loop for a chess game 
        Handles I/O with the user
        Handles interfacing with chess engine
        """
        pass