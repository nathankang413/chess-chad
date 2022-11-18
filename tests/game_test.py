import unittest
from src.game import Game

class TestGameClass(unittest.TestCase):

    default_board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

    def test_00_empty(self):
        '''
        tests that the methods in _check_state work properly
        - get board
        - get turn
        '''
        g = Game()
        self._check_state(g, self.default_board, True)

    def test_01_FEN_to_board(self):
        '''
        no prerequisites
        '''
        g = Game()

        self.assertEqual(g.FEN_to_board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'), self.default_board)

        fen1 = '2B1b3/pr1p1p1p/2p1R1b1/Qq1P1Ppr/p1nP1k1R/1N1pN1P1/PP1K1P1P/2n3B1'
        board1 = [
            ['' , '' , 'B', '' , 'b', '' , '' , '' ],
            ['p', 'r', '' , 'p', '' , 'p', '' , 'p'],
            ['' , '' , 'p', '' , 'R', '' , 'b', '' ],
            ['Q', 'q', '' , 'P', ' ', 'P', 'p', 'r'],
            ['p', '' , 'n', 'P', '' , 'k', '' , 'R'],
            ['' , 'N', '' , 'p', 'N', '' , 'P', '' ],
            ['P', 'P', '' , 'K', '' , 'P', '' , 'P'],
            ['' , '' , 'n', '' , '' , '' , 'B', '' ]
        ]
        self.assertEqual(g.FEN_to_board(fen1), board1)

        fen2 = '8/8/8/8/8/8/8/8'
        board2 = [[''] * 8] * 8
        self.assertEqual(g.FEN_to_board(fen2), board2)

        fen3 = 'KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK'
        board3 = [['K'] * 8] * 8
        self.assertEqual(g.FEN_to_board(fen3), board3)

        # -- Invalid FEN strings -- #
        invalid = [
            '',
            '8/8/8/8/8/8/8/7',  # one row missing a value
            'nnnnnnnn/8/nnnnnnnn/8/NNNNNNNN/8/NNNN/8',  # one row missing values
            'qqqqqqqqq/8/8/8/8/8/8/8',  # one row with too many values
            '8/8/8/8/8/8/8',  # too few rows
            '8/8/8/8/8/8/8/8/8',  # too many rows
            'nkqdqqnb/npqnbpnq/nkqdqqnb/npqnbpnq/nkqdqqnb/npqnbpnq',  # too few rows
            'npqbpnqb/pnqbnpqb/knqbpqnb/pqnbkpnq/bpnqbpnq/bkqbpnqb/pnbqpbnq/pnbqpbnQ/BPNQBPNQ',  # too many rows
            '8/8/8/5i2/8/8/8/8',  # invalid character
        ]
        for fen in invalid:
            self.assertEqual(g.FEN_to_board(fen), None)

    def test_02_check_valid_board(self):
        '''
        no prerequisites

        to test:
        - 8 x 8 board
        - valid characters
        - exactly one of each king on the board
        - no pawns on the first or last rank
        '''

        game = Game()
        
        # -- invalid boards -- #
        board1 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board1), False)

        board2 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
        ]
        self.assertEqual(game.check_valid_board(board2), False)

        board3 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board3), False)

        board4 = [
            ['', '', '', '', '', '', '', ''],
            ['', 'k', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board4), False)

        board5 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'K'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board5), False)

        board6 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'K', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'K'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board6), False)

        board7 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'K', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', 'k', '', '', ''],
            ['', '', 'k', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board7), False)

        board8 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'k', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', ' ', '', '', '', '', '', 'K'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board8), False)

        board9 = [
            ['', '', '', '', '', '', '', 'j'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'k', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'K'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board9), False)

        board10 = [
            ['', 'p', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'k', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'K'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board10), False)

        board11 = [
            ['', '', '', '', '', '', 'P', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'k', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'K'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board11), False)

        board12 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'K', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'k'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'p', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board12), False)


        # -- valid boards -- #
        board101 = [
            ['', '', '', '', '', '', '', ''],
            ['', 'k', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', 'K', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
        self.assertEqual(game.check_valid_board(board101), True)

        self.assertEqual(game.check_valid_board(self.default_board), True)

        board102 = [
            ['r', '', '', 'q', 'n', 'r', 'k', ''],
            ['', '', '', 'n', 'b', 'p', 'p', 'p'],
            ['', '', '', 'p', 'b', '', '', ''],
            ['', '', '', '', '', 'P', 'P', ''],
            ['p', 'p', '', 'N', 'P', '', '', ''],
            ['', '', '', '', 'B', '', '', ''],
            ['P', 'P', 'P', 'Q', '', '', '', 'P'],
            ['', '', 'K', 'R', '', 'B', '', 'R']
        ]
        self.assertEqual(game.check_valid_board(board102), True)

    def test_03_board_to_FEN(self):
        '''
        prerequisite: check_valid_board
        '''
        g = Game()

        self.assertEqual(g.board_to_FEN(self.default_board), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

        fen1 = '2B1b3/pr1p1p1p/2p1R1b1/Qq1P1Ppr/p1nP1k1R/1N1pN1P1/PP1K1P1P/2n3B1'
        board1 = [
            ['' , '' , 'B', '' , 'b', '' , '' , '' ],
            ['p', 'r', '' , 'p', '' , 'p', '' , 'p'],
            ['' , '' , 'p', '' , 'R', '' , 'b', '' ],
            ['Q', 'q', '' , 'P', ' ', 'P', 'p', 'r'],
            ['p', '' , 'n', 'P', '' , 'k', '' , 'R'],
            ['' , 'N', '' , 'p', 'N', '' , 'P', '' ],
            ['P', 'P', '' , 'K', '' , 'P', '' , 'P'],
            ['' , '' , 'n', '' , '' , '' , 'B', '' ]
        ]
        self.assertEqual(g.board_to_FEN(board1), fen1)

        fen2 = '8/8/8/8/8/8/8/8'
        board2 = [[''] * 8] * 8
        self.assertEqual(g.board_to_FEN(board2), fen2)

        fen3 = 'KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK/KKKKKKKK'
        board3 = [['K'] * 8] * 8
        self.assertEqual(g.board_to_FEN(board3), fen3)
    
    def test_10_init(self):
        self.fail()

    def test_11_set_state(self):
        self.fail()

    def test_12_get_check(self):
        self.fail()

    def test_13_get_legal_moves(self):
        self.fail()

    def test_14_make_move(self):
        self.fail()

    def test_15_get_history(self):
        self.fail()

    def _check_state(self, game: Game, board: list[list], turn: bool):
        self.assertEqual(game.get_board(), board)
        self.assertEqual(game.get_turn(), turn)


if __name__ == '__main__':
    unittest.main()