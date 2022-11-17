from config import *

class Game:
    """
    A data structure to maintain and update the game state of a chess game
    """

    def __init__(self, board=None, turn: bool=True) -> None:
        """
        Creates a new Game object
        Sets the board to the default starting positions
        Sets the turn to white
        Saves the entire history of the game

        board - may be string encoding of board (FEN) or a matrix of piece positions
        turn - True if white to play
        """
        self.set_state(board or DEFAULT_BOARD, turn)

        # TODO: init history?

    def set_state(self, board, turn: bool) -> None:
        """
        Sets the game state
        Resets the game history
        board - may be string encoding of board (FEN) or a matrix of piece positions
        turn - True if white to play
        """
        self.board = self.FEN_to_board(board) or board
        if not self.check_valid_board(self.board):
            raise ValueError("Invalid board")
        self.turn = turn

    def get_board(self) -> list[list]:
        """
        Returns a matrix of piece positions
        """
        return self.board

    def get_turn(self) -> bool:
        """
        Returns whether it is white to move
        """
        return self.turn

    def get_check(self) -> int:
        """
        Returns whether player is in check
        """
        pass

    def get_legal_moves(self) -> list[str]:
        """
        Returns a list with all the legal moves in the position for the correct player
        """
        pass

    def make_move(self, move: str, turn: bool) -> bool:
        """
        Updates the game state and history based on the given move
        move - the move in Universal Chess Interface (UCI) notation
        turn - True if white is moving (used to determine whether the move is legal)

        return bool - True if move was legal and made, False if illegal move
        """
        pass

    def get_history(self) -> list:  # TODO: maybe make a data structure for this? because it might have to remember a different starting position
        """
        Returns the history of the game
        """
        pass

    def FEN_to_board(self, fen: str) -> list[list]:
        """
        Returns a matrix of piece positions from a FEN string encoding
        Returns None if FEN string is invalid
        """
        pass

    def board_to_FEN(self, board: list[list]) -> str:
        """
        Returns the FEN encoding of the given board
        Assumes board is valid  # TODO: maybe not? - probably need to raise an error or return none
        """
        pass

    def check_valid_board(self, board: list[list]) -> bool:
        """
        Returns whether the board is valid:
        - 8 x 8
        - all spaces are either empty string or one char representing a piece
        """
        pass