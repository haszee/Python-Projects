import random

print('Welcome to Tic Tac Toe!')

def display(board):
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-----')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
    print('-----')
    print(board[3][0] + '|' + board[3][1] + '|' + board[3][2])

def player_input():
    # initialize 
    player_choice = 0

    # check whether input is either X or O and if it's a string
    while player_choice != 'X' and player_choice != 'O' and player_choice is not isinstance(player_choice, str):
        player_choice = input('Turn player: Please enter your marker: ').upper()
    return player_choice

def replace_pos(newboard,row,column,playermarker):
    newboard[row][column] = playermarker
    return newboard

def check_win(tictactoe):
    win = False
    win_condition1 = ['X', 'X', 'X']
    win_condition2 = ['O', 'O', 'O']
    if tictactoe[1] == win_condition1 or tictactoe[1] == win_condition2 or tictactoe[2] == win_condition1 or tictactoe[2] == win_condition2 or tictactoe[3] == win_condition1 or tictactoe[3] == win_condition2 or [tictactoe[1][0], tictactoe[2][0],tictactoe[3][0]] == win_condition1 or [tictactoe[1][0], tictactoe[2][0],tictactoe[3][0]] == win_condition2 or [tictactoe[1][1], tictactoe[2][1],tictactoe[3][1]] == win_condition1 or [tictactoe[1][1], tictactoe[2][1],tictactoe[3][1]] == win_condition2 or [tictactoe[1][2], tictactoe[2][2],tictactoe[3][2]] == win_condition1 or [tictactoe[1][2], tictactoe[2][2],tictactoe[3][2]] == win_condition2 or [tictactoe[1][0], tictactoe[2][1],tictactoe[3][2]] == win_condition1 or [tictactoe[1][0], tictactoe[2][1],tictactoe[3][2]] == win_condition2 or [tictactoe[1][2], tictactoe[2][1],tictactoe[3][0]] == win_condition1 or [tictactoe[1][2], tictactoe[2][1],tictactoe[3][0]] == win_condition2:
        win = True
    return win

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        print('Host goes 1st')
    else:
        print('Host goes 2nd')

def space_check(board,row,column):
    check_available = False
    if board[row][column] != ' ':
        print('This position is taken. Please choose another.')
    else:
        check_available = True
    return check_available

def full_board_check(tictactoe):
    full = True
    for pos in tictactoe:
        if tictactoe[pos][0] == ' ' or tictactoe[pos][1] == ' ' or tictactoe[pos][2] == ' ':
            full = False
            break
        else:
            continue
    return full

def player_choice():
    # acceptable input for row & column
    acceptable_values = range(1,4)

    # choose which row
    pos1 = input('Turn player please enter the row: ')

    # check whether row is a digit and between 1-3
    while pos1.isdigit() == False or int(pos1) not in acceptable_values:
        print('Sorry please enter a valid digit between 1-3')
        pos1 = input('Turn player please enter the row: ')

    # choose which column
    pos2 = input('Turn player please enter the column: ')

    # check whether column is a digit and between 1-3
    while pos2.isdigit() == False or int(pos2) not in acceptable_values:
        print('Sorry please enter a valid digit between 1-3')
        pos2 = input('Turn player please enter the column: ')

    return (int(pos1), int(pos2)-1)

def ready_play():
    readyplay = False
    while not readyplay:
        askready = input('Are you ready? (yes or no) ').lower()
        if askready == 'yes' or askready == 'y':
            readyplay = True
        else:
            confirm_play = input('Do you wish to wait? (yes or no) ').lower()
            if confirm_play == 'yes' or play == 'y':
                continue
            else:
                print('Player does not wish to play anymore. Game has ended.')
                readyplay = False
                break
    return readyplay

continue_playing = True

while continue_playing:
    tictactoe = {1: [' ', ' ', ' '], 2: [' ', ' ', ' '], 3: [' ', ' ', ' ']}

    # display tictactoe board
    display(tictactoe)

    # randomly chooses who goes 1st
    choose_first()

    # assign player 1 & 2
    player1 = player_input()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Player 1 has chosen {player1}. Player 2 is {player2}. Player 1 will go 1st.')

    # checks if players are ready
    play = ready_play()

    while play:
        # player chooses to be either X or O
        playermarker = player_input()
        
        checkspace = False
        while not checkspace:
            row, column = player_choice() # player chooses a position
            checkspace = space_check(tictactoe,row,column) # checks if position is available

        # update tictactoe board
        tictactoe = replace_pos(tictactoe,row,column,playermarker)

        display(tictactoe)

        # check if player won or board is full
        playerwin = check_win(tictactoe)
        fullboard = full_board_check(tictactoe)

        if playerwin:
            print('Congrats you won!')
        elif fullboard:
            print('Game has ended in a draw')
        else:
            continue

        # choose if wish to continue playing
        if playerwin or fullboard:
            play_again = input('Do you wish to play again? (yes or no) ')
            if play_again == 'yes':
                print('\n'*100)
                break
            else:
                print('Thank you for playing!')
                continue_playing = False
                break