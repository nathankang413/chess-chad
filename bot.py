class Bot:

    def __init__(self) -> None:
        pass

    def get_move(self, board: list[list], turn: bool, check: int, legal_moves: list[str]) -> str:
        """
        Given the game state (board, turn, check), choose a legal move
        """
        pass

    def get_eval(self, board: list[list], turn: bool, check: int) -> str:
        """
        Returns a numeric evaluation of the game state
        Positive evaluations mean that white is better, negative means black is better
        """
        pass