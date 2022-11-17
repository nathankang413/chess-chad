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
        """
        pass

    def set_state(self, board, turn: bool) -> None:
        """
        Sets the game state
        Resets the game history
        board - may be string encoding of board (FEN) or a matrix of piece positions
        turn - True if white to play
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

    def get_board(self) -> list[list]:
        """
        Returns a matrix of piece positions
        """
        pass

    def get_history(self) -> list:  # TODO: maybe make a data structure for this? because it might have to remember a different starting position
        """
        Returns the history of the game
        """
        pass