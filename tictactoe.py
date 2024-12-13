def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]  
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("This position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    board = [' '] * 9  
    current_player = 'X'  

    while True:
        print_board(board)
        player_turn(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
