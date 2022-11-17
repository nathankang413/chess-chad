SQUARE_SIZE = 100  # length of side of a square
BOARD_SIZE = SQUARE_SIZE * 8  # length of side of the board

NO_CHECK = 0
CHECK = 1
CHECK_MATE = 2
STALE_MATE = 3

HUMAN_PLAYER = True

DEFAULT_BOARD = [  # uppercase - white, lowercase - black
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['']*8,
    ['']*8,
    ['']*8,
    ['']*8,
    ['']*8,
    ['']*8,
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]