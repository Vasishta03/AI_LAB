ROWS = 6
COLS = 7
EMPTY = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * 29)

def is_valid_move(board, col):
    if col < 0 or col >= COLS:
        return False
    if board[0][col] != EMPTY:
        return False
    return True

def get_next(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1

def check_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player:
                if col + 3 < COLS and all(board[row][col+i] == player for i in range(4)):
                    return True
                if row + 3 < ROWS and all(board[row+i][col] == player for i in range(4)):
                    return True
                if row + 3 < ROWS and col + 3 < COLS and all(board[row+i][col+i] == player for i in range(4)):
                    return True
                if row - 3 >= 0 and col + 3 < COLS and all(board[row-i][col+i] == player for i in range(4)):
                    return True
    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == EMPTY:
            return False
    return True

def play_game():
    board = create_board()
    turn = 0  
    while True:
        print_board(board)
        cur_player = PLAYER_1 if turn % 2 == 0 else PLAYER_2
        print(f"Player {cur_player}'s turn")

        while True:
            try:
                col = int(input(f"Enter column (0-{COLS-1}): "))
                if is_valid_move(board, col):
                    break
                else:
                    print("Invalid move.")
            except ValueError:
                print("Invalid input.")

        row = get_next(board, col)
        board[row][col] = cur_player

        if check_winner(board, cur_player):
            print_board(board)
            print(f"Player {cur_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("Draw!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()ROWS = 6
COLS = 7
EMPTY = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * 29)

def is_valid_move(board, col):
    if col < 0 or col >= COLS:
        return False
    if board[0][col] != EMPTY:
        return False
    return True

def get_next(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1

def check_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player:
                if col + 3 < COLS and all(board[row][col+i] == player for i in range(4)):
                    return True
                if row + 3 < ROWS and all(board[row+i][col] == player for i in range(4)):
                    return True
                if row + 3 < ROWS and col + 3 < COLS and all(board[row+i][col+i] == player for i in range(4)):
                    return True
                if row - 3 >= 0 and col + 3 < COLS and all(board[row-i][col+i] == player for i in range(4)):
                    return True
    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == EMPTY:
            return False
    return True

def play_game():
    board = create_board()
    turn = 0  
    while True:
        print_board(board)
        cur_player = PLAYER_1 if turn % 2 == 0 else PLAYER_2
        print(f"Player {cur_player}'s turn")

        while True:
            try:
                col = int(input(f"Enter column (0-{COLS-1}): "))
                if is_valid_move(board, col):
                    break
                else:
                    print("Invalid move.")
            except ValueError:
                print("Invalid input.")

        row = get_next(board, col)
        board[row][col] = cur_player

        if check_winner(board, cur_player):
            print_board(board)
            print(f"Player {cur_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
