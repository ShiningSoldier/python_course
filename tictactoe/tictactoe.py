import random

symbols = ["x", "o"]
current_player = 0
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def game_loop():
    choose_player_symbols()
    show_board()
    while True:
        if show_player_input():
            break

def show_board():
    print("The current game board is:...")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def choose_player_symbols():
    print("Welcome to the game! Let's choose the symbols for the players!")
    print("...deciding...")
    random.shuffle(symbols)
    print("Player 1, your symbol is %s" % symbols[0])
    print("Player 2, your symbol is %s" % symbols[1])

def check_if_won():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in winning_combinations:
        if (board[combo[0]] == board[combo[1]] == board[combo[2]] 
            and board[combo[0]] in symbols):
            return True
    
    if " " not in board:
        print("It's a draw!")
        return True
    
    return False
        
def validate_player_input(player_input):
    allowed_values = (1,2,3,4,5,6,7,8,9)
    if not player_input.isnumeric():
        return False
    player_input = int(player_input)
    if player_input not in allowed_values:
        return False
    if board[player_input - 1] in symbols:
        return False
    return True

def show_player_input():
    global current_player
    player_input = ""
    while not validate_player_input(player_input):
        player_input = input("Player %d, enter the field number!" % (current_player + 1))
    board[int(player_input) - 1] = symbols[current_player]
    show_board()
    if check_if_won():
        print("Player %d is a winner!" % (current_player + 1))
        return True
    current_player = 1 - current_player
    return False
    
game_loop()