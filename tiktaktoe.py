import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_moves_left(board):
    return any(cell == " " for row in board for cell in row)

def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == "X" else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == "X" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10

    return 0

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best

    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_value = minimax(board, 0, False)
                board[i][j] = " "
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', and the AI is 'X'.")

    while True:
        print_board(board)
        if evaluate(board) == 10:
            print("AI wins! Better luck next time.")
            break
        elif evaluate(board) == -10:
            print("Congratulations, you win!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break

        # Human player's turn
        move = input("Enter your move (row and column separated by space, e.g., '0 1'): ").split()
        row, col = int(move[0]), int(move[1])
        if board[row][col] == " ":
            board[row][col] = "O"
        else:
            print("Invalid move. Try again.")
            continue

        # AI's turn
        if is_moves_left(board):
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = "X"

if __name__ == "__main__":
    main()
