from config import *
from user_interface import UserInterface
from game import Game

class TerminalUI(UserInterface):
    """
    Implementation of UserInterface using the terminal
    """

    def __init__(self, game: Game = None, players: tuple = None) -> None:
        super().__init__(game, players)

    def run_loop(self) -> None:
        super().run_loop()

        while self.game.get_check not in [CHECK_MATE, STALE_MATE]:
            # display the board
            self.display_board()

            # query a move from player whose turn it is
            move = self.query_move()

            # make the move
            legal_move = self.game.make_move(move)

            if not legal_move:
                print(f'{move} is not a legal move')
        
        # show results of the game


    def display_board(self) -> None:
        """
        Prints the board to the terminal
        """
        print('\n'.join(' '.join(' ' if token == '' else token for token in row) for row in self.game.get_board()))

    def query_move(self) -> str:
        """
        Requests and returns a move from the correct player
        """
        pass