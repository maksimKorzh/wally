###################################
#
#   WALLY by Jonathan K. Millen
#     (reconstruction by CMK)
#
###################################

import sys
import random

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
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 9x9 coordinates
coords_9x9 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
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

# 13x13 coordinates
coords_13x13 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A13','B13','C13','D13','E13','F13','G13','H13','J13','K13','L13','M13','N13','XX',
    'XX', 'A12','B12','C12','D12','E12','F12','G12','H12','J12','K12','L12','M12','N12','XX',
    'XX', 'A11','B11','C11','D11','E11','F11','G11','H11','J11','K11','L11','M11','N11','XX',
    'XX', 'A10','B10','C10','D10','E10','F10','G10','H10','J10','K10','L10','M10','N10','XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
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

# 19x19 coordinates
coords_19x19 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A19','B19','C19','D19','E19','F19','G19','H19','J19','K19','L19','M19','N19','O19','P19','Q19','R19','S19','T19','XX',
    'XX', 'A18','B18','C18','D18','E18','F18','G18','H18','J18','K18','L18','M18','N18','O18','P18','Q18','R18','S18','T18','XX',
    'XX', 'A17','B17','C17','D17','E17','F17','G17','H17','J17','K17','L17','M17','N17','O17','P17','Q17','R17','S17','T17','XX',
    'XX', 'A16','B16','C16','D16','E16','F16','G16','H16','J16','K16','L16','M16','N16','O16','P16','Q16','R16','S16','T16','XX',
    'XX', 'A15','B15','C15','D15','E15','F15','G15','H15','J15','K15','L15','M15','N15','O15','P15','Q15','R15','S15','T15','XX',
    'XX', 'A14','B14','C14','D14','E14','F14','G14','H14','J14','K14','L14','M14','N14','O14','P14','Q14','R14','S14','T14','XX',
    'XX', 'A13','B13','C13','D13','E13','F13','G13','H13','J13','K13','L13','M13','N13','O13','P13','Q13','R13','S13','T13','XX',
    'XX', 'A12','B12','C12','D12','E12','F12','G12','H12','J12','K12','L12','M12','N12','O12','P12','Q12','R12','S12','T12','XX',
    'XX', 'A11','B11','C11','D11','E11','F11','G11','H11','J11','K11','L11','M11','N11','O11','P11','Q11','R11','S11','T11','XX',
    'XX', 'A10','B10','C10','D10','E10','F10','G10','H10','J10','K10','L10','M10','N10','O10','P10','Q10','R10','S10','T10','XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'O9', 'P9', 'Q9', 'R9', 'S9', 'T9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'O8', 'P8', 'Q8', 'R8', 'S8', 'T8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'O7', 'P7', 'Q7', 'R7', 'S7', 'T7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'O6', 'P6', 'Q6', 'R6', 'S6', 'T6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'O5', 'P5', 'Q5', 'R5', 'S5', 'T5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'O4', 'P4', 'Q4', 'R4', 'S4', 'T4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3', 'P3', 'Q3', 'R3', 'S3', 'T3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'O2', 'P2', 'Q2', 'R2', 'S2', 'T2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

# boards lookup
BOARDS = {
     '9': board_9x9,
    '13': board_13x13,
    '19': board_19x19
}

# coords lookup
COORDS = {
     '9': coords_9x9,
    '13': coords_13x13,
    '19': coords_19x19,
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
coords = None

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
                space = '  ' if len(board) == 121 else '   '
                print((space if rank < 10 else '  ') + str(rank), end='')
            
            # print board square's content
            print(pieces[stone] + ' ', end='')
            
        # print new line
        print()
    
    # print notation
    print(' ' + files[0:BOARD_RANGE*2] + '\n')

# set Go ban size
def set_board_size(command):
    # hook global variables
    global BOARD_WIDTH, BOARD_RANGE, board, coords
    
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
    coords = COORDS[str(size)]

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

# make move on board
def set_stone(square, color):
    # make move on board
    board[square] = color
    
    # handle captures
    captures(3 - color)

# generate random move
def make_random_move(color):
    # find empty random square
    random_square = random.randrange(len(board))
    while board[random_square] != EMPTY:
        random_square = random.randrange(len(board))
    
    # make move
    set_stone(random_square, color)
    
    # count liberties
    count(random_square, color)
    
    # suicide move
    if len(liberties) == 0:
        # restore board
        restore_board()
        
        # take off the stone
        board[random_square] = EMPTY
        
        # search for another move
        try:
            # return non suicide move
            return make_random_move(color)
        except:
            # pass the move
            return '' 
    
    # restore board
    restore_board()
    
    # return the move
    return coords[random_square]

# play command
def play(command):
    # parse color
    color = BLACK if command.split()[1] == 'B' else WHITE
    
    # parse square
    square_str = command.split()[-1]
    col = ord(square_str[0]) - ord('A') + 1 - (1 if ord(square_str[0]) > ord('I') else 0)
    row_count = int(square_str[1:]) if len(square_str[1:]) > 1 else ord(square_str[1:]) - ord('0')
    row = (BOARD_RANGE - 1) - row_count
    square = row * BOARD_RANGE + col
    
    # make GUI move
    set_stone(square, color)

# handle captures
def captures(color):
    # loop over the board squares
    for square in range(len(board)):
        # init piece
        piece = board[square]
        
        # skip offboard squares
        if piece == OFFBOARD: continue
        
        # if stone belongs to the given color
        if piece & color:
            # count liberties
            count(square, color)
            
            # if no liberties left remove the stones
            if len(liberties) == 0: clear_block()
            
            # restore the board
            restore_board()

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
        elif 'showboard' in command: print('= '); print_board()
        elif 'play' in command: play(command); print('=\n')
        elif 'genmove' in command: print('=', make_random_move(BLACK if command.split()[-1] == 'B' else WHITE) + '\n')
        elif 'quit' in command: sys.exit()
        else: print('=\n') # skip currently unsupported commands
        

# start GTP communication
gtp()












