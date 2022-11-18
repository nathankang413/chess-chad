from config import *

class Game:
    """
    A data structure to maintain and update the game state of a chess game
    """

    def __init__(self, board=None, turn: bool=True) -> None:
        """
        Creates a new Game object
        Sets the board to the default starting positions, unless otherwise specified
        Sets the turn to white, unless otehrwise specified
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
        # check if move is legal
        # update board
        # update turn
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
        fen = ""  # Starts by opening an empty string for encoding the board state

        if not self.check_valid_board(self.board):  # checks validity of board state and throws an error code if invalid
            raise ValueError("Invalid board")

        for row in board:
            gap = 0  # Sets gap counter to zero; used in printing gaps between pieces into the FEN string

            for token in row:
                if token == '':  # If the space is empty, adds one count to the gap tracker
                    gap += 1
                else:  # Adds the current token to fen string with the gap count before it (if there is one)
                    fen += f"{gap if gap != 0 else ''}{token}"
                    gap = 0  # Resets gap to zero when a token is found (Yes Nathan, I know it does this everytime)

            if gap != 0:  # At the end of the line, makes sure to add the gap if there is one
                fen += f"{gap}"
            fen += "/"  # Adds the "/" as next-row notation in FEN

        return fen[:-1]  # Returns the FEN encoding but without the "/" that gets attached at the end

    def check_valid_board(self, board: list[list]) -> bool:
        """
        Returns whether the board is valid:
        - 8 x 8
        - all spaces are either empty string or one char representing a piece
        - exactly one of each king on the board
        - no pawns on the first or last rank
        """
        valid_tokens = ['', 'r', 'n', 'b', 'q', 'k', 'p']  # lowercase version of all acceptable tokens on the board

        if not isinstance(board, list) or not all(isinstance(element, list) for element in board):  # Checks to make sure the board is the correct data structure to begin with
            return False

        if len(board) != 8:  # Checks the correct number of rows in the board
            return False

        for row in board:  # Checks the correct number of spaces in each row
            if len(row) != 8:
                return False

        black_king = False
        white_king = False
        for row in board:  # Runs through every position to check only valid tokens are present
            for position in row:
                if type(position) is not str or position.lower() not in valid_tokens:
                    return False
                if position == 'k':
                    if black_king:
                        return False
                    black_king = True
                if position == 'K':
                    if white_king:
                        return False
                    white_king = True

        return True  # If all previous checks for invalidity have passed, returns True
