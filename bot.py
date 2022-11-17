from game_state import GameState

class Bot:

    def __init__(self) -> None:
        pass

    def get_move(self, state: GameState) -> str:
        """
        Chooses a move from state.get_legal_moves()
        """
        pass

    def get_eval(self, state: GameState) -> str:
        """
        Returns a numeric evaluation of the game state
        Positive evaluations mean that white is better, negative means black is better
        """
        pass