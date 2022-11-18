import unittest
import sys
sys.path.append('../')
from src.game import *

class TestGameClass(unittest.TestCase):

    def test_01(self):
        pass

    def _check_state(self, game, board, turn, check):
        self.assertEqual(game.get_board())


if __name__ == '__main__':
    unittest.main()