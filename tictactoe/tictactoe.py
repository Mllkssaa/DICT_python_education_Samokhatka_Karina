board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
winner = None
game_running = True

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " +board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def player_input(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9:
                if board[inp - 1] == "-":
                    board[inp - 1] = current_player
                    break
                else:
                    print("Oops player is already in that spot.=)")
            else:
                print("Invaild input! Choose a number between 1 and 9.")
        except ValueError:
            print("Invaalid input! Please enter a number between 1 and 9.")


def check_horizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            winner = board[i]
            return True
        return False


def check_row(board):
    global winner
    for i in range(3):
        if board[i] == board[i +3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            return True
    return False


def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False

def check_win():
    global game_running
    if check_diag(board) or check_horizontal(board) or check_row(board):
        print_board(board)
        print(f"The winner is {winner}")
        game_running = False


def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"



while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()