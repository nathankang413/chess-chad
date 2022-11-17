from game import Game
from bot import Bot
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
        if game is None or type(game) is Game:
            self.game = game
        else:
            raise ValueError(f'{game} is not a Game object')

        if players is None or self.valid_players(players):
            self.players = players
        else:
            raise ValueError('players is not a tuple of players')
    
    def valid_players(self, players) -> bool:
        """
        Helper function, returns True if players is a tuple of 2 valid players
        """
        if type(players) is not tuple or len(players != 2): return False

        return all(player == HUMAN_PLAYER or isinstance(player, Bot) for player in players)

    def set_game(self, game: Game) -> None:
        """
        Changes the game object to the given Game
        """
        if type(game) is Game:
            self.game = game
        else:
            raise ValueError(f'{game} is not a Game object')

    def set_players(self, *players) -> None:
        """
        Changes the players to the given players
        players - one (1) tuple or mutiple players (HUMAN_PLAYER or Bot object)
        """
        if len(players) == 2 and self.valid_players(tuple(players)):
            self.players = tuple(players)
        elif self.valid_players(players[0]):
            self.players = tuple(players)
        else:
            raise ValueError(f'{players} does not contain 2 valid players')

    def run_loop(self) -> None:
        """
        Runs the game loop for a chess game 
        Handles I/O with the user
        Handles interfacing with chess engine
        """
        pass