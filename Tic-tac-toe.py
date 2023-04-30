# IMPORT FUNCTION

from random import randrange

# ---------------------------------------------------------------------------------------------------------
# MY FUNCTIONS

def start():
    # The function prints the greeting and prompts the user to start the game

    # Printing the greeting
    print("Welcome to the tic-tac-toe game! Here, you can play tic-tac-toe with the computer.\n")
    print("The first move is always done by the computer. The computer's move is marked by X.")
    print("Your moves will be marked by O. You can make your move by entering the number of")
    print("the field.\n")

    # Asking the user to start the game
    while(True):
        try:
            start_game = int(input("Enter 1 to start the game.\n"))
            if start_game != 1:
                continue
            else:
                return True
        except:
            continue

    
            
    
def save_user_move(user_move, board):
    # The function saves the user's move and updates the board
    for row in range(board_width):
        for column in range(board_height):
            if board[row][column] == user_move:
                board[row][column] = 'O'
                
    taken_fields.append(user_move)
    
    return board

def computer_move(board):
    # The function does the computer's move and updates the board

    # Creating the list of possible computer's moves
    possible_moves = []
    
    for row in range(board_width):
        for column in range(board_height):
            if board[row][column] != 'X' and board[row][column] != 'O':
                possible_moves.append(board[row][column])
                
    # Making computer's move
    computer_move = possible_moves[randrange(len(possible_moves))]
    taken_fields.append(computer_move)

    # Updating the board after computer's move
    for row in range(board_width):
        for column in range(board_height):
            if board[row][column] == computer_move:
                board[row][column] = 'X'
                
    return board

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, updates the board
    
    # Accepting the user's move and dealing with possible exceptions
    try:
        user_move = int(input("Enter your move: "))
    except ValueError:
        print("Please, enter a valid value.")
        user_move = None
        return user_move
    except:
        print("Something went wrong. Please, restart the program.")
        user_move = None
        return user_move

    # Checking if the user entered the number in the acceptable range
    if user_move < 1 or user_move > 9:
        print("Please, enter the value in the range 1 <= value <= 9.")
        user_move = None
        return user_move

    # Checking if the user chose the free field
    for field in range(len(taken_fields)):
        if user_move == taken_fields[field]:
            print("The field is taken. Please, choose another one.")
            user_move = None
            return user_move
                
    return user_move
                
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free fields

    # Filling the board with values from 1 to 9
    field_num = 1
    for row in range(board_width):
        row_list = []
        for column in range(board_height):
            row_list.append(field_num)
            field_num += 1
        board.append(row_list)
    # Computer's first move is always in the middle of the board
    board[1][1] = 'X'
    taken_fields.append(5)

    return board
                  
def if_victory(board):
    # The function analyzes the board's status in order to check
    # if the player using 'O's or 'X's has won the game
    
    X_counter = 0
    O_counter = 0

    # Checking if a row contains all Xs or all Os
    for row in range(board_width):
        for column in range(board_height):  
            if board[row][column] == 'X':
                    X_counter += 1
            if board[row][column] == 'O':
                    O_counter += 1
                    
            if column == board_height - 1:
                if if_winner(X_counter, O_counter):
                    return True
                X_counter = 0
                O_counter = 0

    # Checking if a column contains all Xs or all Os
    for column in range(board_width):
        for row in range(board_height):
            if board[row][column] == 'X':
                    X_counter += 1
            if board[row][column] == 'O':
                    O_counter += 1
                    
            if row == board_height - 1:
                if if_winner(X_counter, O_counter):
                    return True
                X_counter = 0
                O_counter = 0
                
    # Checking if the diagonals contain all Xs or all Os
    
    # Diagonal 1
    for row in range(board_width):
        for column in range(board_height):
            if row == column:
                if board[row][column] == 'X':
                    X_counter += 1
                if board[row][column] == 'O':
                    O_counter += 1
                    
            if row == column and row == board_width - 1:
                if if_winner(X_counter, O_counter):
                    return True
                X_counter = 0
                O_counter = 0
                
    # Diagonal 2
    for row in range(board_width):
        for column in range(board_height):
            if (row == 2 and column == 0) or (row == 0 and column == 2) or (row == 1 and column == 1):
                if board[row][column] == 'X':
                    X_counter += 1
                if board[row][column] == 'O':
                    O_counter += 1
                    
            if (row == 2 and column == 0):
                if if_winner(X_counter, O_counter):
                    return True
                X_counter = 0
                O_counter = 0
                
                
    return False

def if_tie(board):
    # The function announces the tie if there is one
    X_O_counter = 0
    
    for row in range(board_width):
        for column in range(board_height):
            if board[row][column] == 'O' or board[row][column] == 'X':
                X_O_counter += 1

    if X_O_counter == 9:
        print("\nTie.")
        return True
    else:
        return False
            
def if_winner(X_counter, O_counter):
    # The function announces the winner if there is one
    if X_counter == 3:
        print("\nComputer won.")
        return True
    if O_counter == 3:
        print("\nYou won. Well done!")
        return True
    
    return False
    

def draw_board(board):
    # The function draws the board.
    
    # Printing the board
    print("+---------"*3, end = "+\n")
    for row in range(board_width):
        print("|         "*3, end = "|\n")
        for column in range(board_height):
            if column == (board_width - 1):
                print("|   ", board[row][column], end = "    |\n")
                print("|         "*3, end = "|\n")
                print("+---------"*3, end = "+\n")
            else:
                print("|   ", board[row][column], "   ", end = "")

# ---------------------------------------------------------------------------------------------------------
# ASSIGNING VARIABLES
board_height = 3
board_width = 3
board = []
taken_fields = []
PLAYING_MODE = True

# ---------------------------------------------------------------------------------------------------------
# EXECUTING FUNCTIONS
board = make_list_of_free_fields(board)

if start():

    while(PLAYING_MODE):
        draw_board(board)
        user_move = enter_move(board)
        if user_move == None:
            continue
        else:
            board = save_user_move(user_move, board)
            if  if_victory(board):
                draw_board(board)
                PLAYING_MODE = False
                break
    
            board = computer_move(board)
            if  if_victory(board):
                draw_board(board)
                PLAYING_MODE = False
                break

            if if_tie(board):
                draw_board(board)
                PLAYING_MODE = False
                break
        
