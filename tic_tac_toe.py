# tic_tac_toe.py

import math

def print_board(board):
    print("\n")
    for row in board:
        print("|".join(row))
    print("\n")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] != ' ':
            return board[0][col]

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != ' ':
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != ' ':
        return board[0][2]

    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe (You = X, AI = O)\n")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        print_board(board)

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # AI move
        i, j = best_move(board)
        board[i][j] = 'O'
        print("AI has made its move.")
        print_board(board)

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()