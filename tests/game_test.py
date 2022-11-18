import unittest
import sys
sys.path.append('../')
from src.game import Game

class TestGameClass(unittest.TestCase):

    def test_00_empty(self):
        pass

    def test_01_FEN_to_board(self):
        pass

    def test_02_board_to_FEN(self):
        pass

    def test_03_check_valid_board(self):
        pass

    def test_11_set_state(self):
        pass

    def test_12_get_check(self):
        pass

    def test_13_get_legal_moves(self):
        pass

    def test_14_make_move(self):
        pass

    def test_15_get_history(self):
        pass

    def _check_state(self, game: Game, board: list[list], turn: bool):
        self.assertEqual(game.get_board(), board)
        self.assertEqual(game.get_turn(), turn)


if __name__ == '__main__':
    unittest.main()