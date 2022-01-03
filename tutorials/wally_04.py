###################################
#
#   WALLY by Jonathan K. Millen
#     (reconstruction by CMK)
#
###################################

import sys

VERSION = '1.0'

###################################
#
#          Piece encoding
#
###################################
#
# 0000 => 0    empty sqare
# 0001 => 1    black stone
# 0010 => 2    white stone
# 0100 => 4    stone marker
# 0111 => 7    offboard square
# 1000 => 8    liberty marker
#
# 0101 => 5    black stone marked
# 0110 => 6    white stone marked
#
###################################

# 9x9 GO ban
board_9x9 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 1, 1, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 1, 1, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 1, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 13x13 GO ban
board_13x13 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 19x19 GO ban
board_19x19 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# boards lookup
BOARDS = {
     '9': board_9x9,
    '13': board_13x13,
    '19': board_19x19
}

# stones
EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

# count
liberties = []
block = []

# current board used
board = None

# GO ban size
BOARD_WIDTH = 0
BOARD_RANGE = 0
MARGIN = 2

# file markers
files = '     a b c d e f g h j k l m n o p q r s t'

# ASCII representation of stones
pieces = '.#o  bw +'

def print_board():
    # loop over board rows
    for row in range(BOARD_RANGE):
        # loop over board columns
        for col in range(BOARD_RANGE):
            # init square
            square = row * BOARD_RANGE + col
            
            # init stone
            stone = board[square]
            
            # print rank
            if col == 0 and row > 0 and row < BOARD_RANGE - 1:
                rank = BOARD_RANGE - 1 - row
                print(('  ' if rank < 10 else ' ') + str(rank), end='')
            
            # print board square's content
            print(pieces[stone] + ' ', end='')
            
        # print new line
        print()
    
    # print notation
    print(files[0:BOARD_RANGE*2] + '\n')

# set Go ban size
def set_board_size(command):
    # hook global variables
    global BOARD_WIDTH, BOARD_RANGE, board
    
    # parse the board size
    size = int(command.split()[-1])
    
    # throw error if board size is not supported
    if size not in [9, 13, 19]:
        print('? current board size not supported\n')
        return

    # calculate current board size
    BOARD_WIDTH = size
    BOARD_RANGE = BOARD_WIDTH + MARGIN
    board = BOARDS[str(size)]

# count liberties, save stone group coords
def count(square, color):
    # init piece
    piece = board[square]
    
    # skip offboard squares
    if piece == OFFBOARD: return
    
    # if there's a stone at square
    if piece and piece & color and (piece & MARKER) == 0:
        # save stone's coordinate
        block.append(square)
        
        # mark the stone
        board[square] |= MARKER
        
        # look for neighbours recursively
        count(square - BOARD_RANGE, color) # walk north
        count(square - 1, color)           # walk east
        count(square + BOARD_RANGE, color) # walk south
        count(square + 1, color)           # walk west
    
    # if the square is empty
    elif piece == EMPTY:
        # mark liberty
        board[square] |= LIBERTY
        
        # save liberty
        liberties.append(square)

# remove captured stones
def clear_block():
    for captured in block: board[captured] = EMPTY

# clear groups
def clear_groups():
    # hook global variables
    global block, liberties
    
    # clear block and liberties lists
    block = []
    liberties = []

# restore the board after counting stones
def restore_board():
    # clear groupd
    clear_groups()
    
    # unmark stones
    for square in range(BOARD_RANGE * BOARD_RANGE):
        # restore piece if the square is on board
        if board[square] != OFFBOARD: board[square] &= 3

# clear board
def clear_board():
    # clear groupd
    clear_groups()
    
    for square in range(len(board)):
        if board[square] != OFFBOARD: board[square] = 0

# GTP communcation protocol
def gtp():
    # main GTP loop
    while True:
        # accept GUI command
        command = input()
        
        # handle commands
        if 'name' in command: print('= Wally\n')
        elif 'protocol_version' in command: print('= 1\n');
        elif 'version' in command: print('=', VERSION, '\n')
        elif 'list_commands' in command: print('= protocol_version\n')
        elif 'boardsize' in command: set_board_size(command); print('=\n')
        elif 'clear_board' in command: clear_board(); print('=\n')
        elif 'showboard' in command: print('='); print_board()
        elif 'genmove' in command: print('= E2\n')
        elif 'quit' in command: sys.exit()
        else: print('=\n') # skip currently unsupported commands

# start GTP communication
gtp()















