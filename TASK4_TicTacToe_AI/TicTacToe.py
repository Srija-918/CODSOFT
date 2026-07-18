import math

# Empty board
board = [" " for i in range(9)]

# Display board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Show position numbers
def show_positions():
    print("Board Positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()

# Check winner
def check_winner(b, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for win in wins:
        if b[win[0]] == b[win[1]] == b[win[2]] == player:
            return True
    return False

# Check draw
def is_full():
    return " " not in board

# Minimax Algorithm
def minimax(b, is_max):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best

# Computer move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Player move
def player_move():
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1

            if pos < 0 or pos > 8:
                print("Please enter a number between 1 and 9.")
            elif board[pos] != " ":
                print("Position already occupied. Try again.")
            else:
                board[pos] = "X"
                break
        except ValueError:
            print("Please enter a valid number.")

# Main game
while True:

    board = [" " for i in range(9)]

    print("\n===== TIC-TAC-TOE AI =====")
    print("You : X")
    print("Computer : O\n")

    show_positions()

    while True:

        print_board()

        player_move()

        if check_winner(board, "X"):
            print_board()
            print("🎉 Congratulations! You Win!")
            break

        if is_full():
            print_board()
            print("🤝 It's a Draw!")
            break

        print("\nComputer is thinking...\n")
        ai_move()

        if check_winner(board, "O"):
            print_board()
            print("🤖 Computer Wins!")
            break

        if is_full():
            print_board()
            print("🤝 It's a Draw!")
            break

    choice = input("\nPlay Again? (y/n): ").lower()

    if choice != "y":
        print("Thanks for playing!")
        break