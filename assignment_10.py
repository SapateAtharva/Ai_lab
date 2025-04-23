import random


def print_board(board):
    print("\nCurrent Board:")
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {'|'.join(row)}")
        if i < 2:
            print("  -----")


def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    return (board[0][0] == board[1][1] == board[2][2] == player or
            board[0][2] == board[1][1] == board[2][0] == player)


def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']


def make_ai_move(board):
    # Win if possible
    for (i, j) in get_empty_cells(board):
        board[i][j] = 'O'
        if check_winner(board, 'O'):
            return
        board[i][j] = ' '

    # Block player
    for (i, j) in get_empty_cells(board):
        board[i][j] = 'X'
        if check_winner(board, 'X'):
            board[i][j] = 'O'
            return
        board[i][j] = ' '

    # Take center
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return

    # Random move
    i, j = random.choice(get_empty_cells(board))
    board[i][j] = 'O'


def get_player_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    return
                else:
                    print("Cell is already taken. Choose another.")
            else:
                print("Coordinates out of range. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers only.")


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O.")
    print_board(board)

    for _ in range(9):
        get_player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("🎉 You win!")
            return

        if not get_empty_cells(board):
            break

        print("AI is making a move...")
        make_ai_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("💻 AI wins!")
            return

        if not get_empty_cells(board):
            break

    print("It's a draw!")


# Run the game
play_tic_tac_toe()
