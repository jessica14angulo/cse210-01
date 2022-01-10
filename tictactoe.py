""""
Tic-tac-toe game
Author: Jessica Angulo
"""

def main():
    player = player_turn("")
    board = create_board()
    print("Welcome to Tic-Tac-Toe game! Please enjoy!")
    while not (winner(board) or draw(board)):
        show_board(board)
        move(player, board)
        player = player_turn(player)
    show_board(board)
    print(f"Player '{player}' you lost!")
    print("Good game. Thanks for playing!")

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

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]) 