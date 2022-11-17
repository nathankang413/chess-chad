class GameState:
    """
    A data structure containing the static state of a chess game
    """

    def __init__(self, board: list[list], turn: bool, check: int) -> None:
        """
        Creates a new GameState
        board - a 2d matrix of piece positions
        turn - True if white to move
        check - see config for check values
        """
        pass

    def get_legal_moves(self) -> list[str]:
        """
        Returns a list with all the legal moves in the position for the correct player
        """
        pass