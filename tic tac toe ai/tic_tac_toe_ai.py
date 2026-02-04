
import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in win) for win in wins)

def empty_positions():
    return [i for i, spot in enumerate(board) if spot == " "]

def ai_move():
   
    for i in empty_positions():
        board[i] = "O"
        if check_winner("O"):
            return
        board[i] = " "

    
    for i in empty_positions():
        board[i] = "X"
        if check_winner("X"):
            board[i] = "O"
            return
        board[i] = " "

    if 4 in empty_positions():
        board[4] = "O"
        return

    
    board[random.choice(empty_positions())] = "O"

def play():
    print("You are X | AI is O")
    print("Positions: 1-9\n")

    while True:
        print_board()

      
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] != " ":
                print("Position taken! Try again.")
                continue
            board[move] = "X"
        except:
            print("Invalid input!")
            continue

        if check_winner("X"):
            print_board()
            print(" You win!")
            break

        if not empty_positions():
            print_board()
            print("It's a draw!")
            break

        
        ai_move()

        if check_winner("O"):
            print_board()
            print(" AI wins!")
            break

        if not empty_positions():
            print_board()
            print("It's a draw!")
            break

play()
