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

BLACK = 1
WHITE = 2

board = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 2, 2, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 1, 2, 0, 0, 7,
    7, 2, 2, 0, 0, 2, 2, 0, 0, 0, 7,
    7, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 2, 2, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]


pieces = '.#o  bw +'
liberties = 0
block = []

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
        liberties += 1

def restore_board():
    global liberties, block
    liberties = 0
    block = []
    
    for square in range(len(board)):
        if board[square] != 7: board[square] &= 3

def weffect():
    for square in range(len(board)):
        piece = board[square]
        if piece == 7: continue
        if piece & BLACK:
            count(square, BLACK)
            #print('liberties:', liberties)
            #print('block:', block)
            print_board()
            if liberties == 0:
                for captured in block:
                    board[captured] = 0
            
            restore_board()
            

def main():
    color = BLACK
    while True:        
        print_board()
        square_str = input('Your move: ')
        if square_str == '': continue
        _file = ord(square_str[0]) - ord('a') + 1
        _rank = 10 - (ord(square_str[1]) - ord('0'))
        square = _rank * 11 + _file
        board[square] = color
        color = 3 - color
        weffect()

main()
#weffect()

