def create_board():
    board = []
    for square in range(9):
        board.append(square +1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("_+_+_")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("_+_+_")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()