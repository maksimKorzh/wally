###################################
#
#          Piece encoding
#
###################################
#
# 0100 => 4    stone marker
# 1000 => 8    liberty marker
#
# 0001 => 1    black stone
# 0101 => 5    black stone marked
# 0010 => 2    white stone
# 0110 => 6    white stone marked
# 0111 => 7    offboard square
# 0000 => 0    empty sqare
#
###################################

import random, sys

BLACK = 1
WHITE = 2

board = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 0, 0, 0, 1, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

pieces = '.#o  bw +'
liberties = []
block = []
best_square = 0

def print_board():
    for i in range(len(board)):
        rank = 11 - int(i / 11)
        print(pieces[board[i]] +
              ' ' if ((i % 11) != 0) else
              ('\n ' + str(rank-1) if rank > 1 and rank < 11 else '') + 
              pieces[board[i]] + ' ', end='')

    print('\n\n    a b c d e f g h i\n')

def count(square, color):
    global liberties
    piece = board[square]
    if piece == 7: return
    if piece and piece & color and (piece & 4) == 0:
        block.append(square)
        board[square] |= 4
        count(square - 11, color)
        count(square -1, color)
        count(square + 11, color)
        count(square + 1, color)
    elif piece == 0:
        board[square] |= 8
        liberties.append(square)

def clear_block():
    for captured in block:
        board[captured] = 0

def restore_board():
    global liberties, block
    liberties = []
    block = []
    
    for square in range(len(board)):
        if board[square] != 7: board[square] &= 3

def weffect():
    global best_square
    for square in range(len(board)):
        piece = board[square]
        if piece == 7: continue
        if piece & BLACK:
            count(square, BLACK)
            if len(liberties) == 0: clear_block()
            elif len(liberties) == 1:
                is_edge = 0
                for d in [1, 11, -1, -11]:
                    if board[liberties[0] + d] == 7:
                        is_edge = 1
                        break
                
                if not is_edge:
                    board[liberties[0]] = BLACK
                    best_square = 1
                    break
            restore_board()
            
def beffect():
    global best_square
    for square in range(len(board)):
        piece = board[square]
        if piece == 7: continue
        if piece & WHITE:
            count(square, WHITE)
            if len(liberties) == 0: clear_block()
            if len(liberties) == 1 and not best_square:
                board[liberties[0]] = BLACK
                clear_block()
                best_square = 1
                break
            restore_board()

def main():
    global best_square
    while True:        
        best_square = 0
        print_board()
        square_str = input('Your move: ')
        if square_str == '': continue
        _file = ord(square_str[0]) - ord('a') + 1
        _rank = 10 - (ord(square_str[1]) - ord('0'))
        square = _rank * 11 + _file
        if board[square] == 0: board[square] = WHITE
        else: continue
        print_board()
        weffect()
        beffect()

        if best_square == 0:
            random_square = random.randrange(len(board))
            while board[random_square] != 0:
                random_square = random.randrange(len(board))
            board[random_square] = BLACK
#main()

def gtp():
    while True:
        gui_command = input()
        
        if gui_command == 'name': print('= Wally\n')
        elif gui_command == 'version': print('= 1.0\n')
        elif gui_command == 'protocol_version': print('= 1\n')
        elif gui_command == 'list_commands': print('= protocol_version\n')
        elif gui_command == 'quit': sys.exit()
        elif 'play' in gui_command:
            square_str = gui_command.split()[-1]
            _file = ord(square_str[0]) - ord('A') + 1
            _rank = 10 - (ord(square_str[1]) - ord('0'))
            square = _rank * 11 + _file
            board[square] = BLACK if gui_command[1] == 'B' else WHITE
            print('=\n')
        elif 'genmove' in gui_command:
            random_square = random.randrange(len(board))
            while board[random_square] != 0:
                random_square = random.randrange(len(board))
            board[random_square] = BLACK
            
            
            
            print('= E4\n' )
        else: print('=\n')
gtp()







