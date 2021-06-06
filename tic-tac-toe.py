##importing
import base64
import random
from game_board_class import *
import re 


##initializing window, game board, and player role


game_board = [[Square([1, 1]), Square([1, 2]), Square([1, 3])],
                      [Square([2, 1]), Square([2, 2]), Square([2, 3])],
                      [Square([3, 1]), Square([3, 2]), Square([3, 3])]]

game_board_display = [[[ ], [ ], [ ]], 
                      [[ ], [ ], [ ]],
                      [[ ], [ ], [ ]]]


used_coords = []

x=random.randint(1, 2)
if x == 1:
    human_role = 'X'
    computer_role = 'O'
    print('You are Xs')
    game_state = Game('H')
else:
    human_role = 'O'
    computer_role = 'X'
    print('You are Os')
    game_state = Game('C')


##game functions



def check_win():
    ##check horizontal wins
    for i in range(0, 3):
        if 'O' not in [c.contents for c in game_board[i]] and None not in [c.contents for c in game_board[i]]:
            win = 'X'
            if human_role==win:
                print('You win!')
                return True 
            if computer_role==win:
                print('You lose!')
                return True 
        if 'X' not in [c.contents for c in game_board[i]] and None not in [c.contents for c in game_board[i]]:
            win = 'O'
            if human_role==win:
                print('You win!')
                return True 
            if computer_role==win:
                print('You lose!')
                return True 
        else:
            win = False

    ##check vertical wins
    
    for i in range(0, 3):
        if len([c[i].contents for c in game_board if c[i].contents=='X'])==3:
            win = 'X'
            if human_role==win:
                print('You win!')
                return True 
            if computer_role==win:
                print('You lose!')
                return True 
        elif len([c[i].contents for c in game_board if c[i].contents=='O'])==3:
            win = 'O'
            if human_role==win:
                print('You win!')
                return True 
            if computer_role==win:
                print('You lose!')
                return True 
        else:
            win = False

    ##check diagonal wins
    diag_1 = [c.contents for c in [game_board[0][0], game_board[1][1], game_board[2][2]]]
    diag_2 = [c.contents for c in [game_board[0][2], game_board[1][1], game_board[2][0]]]    

    if 'O' not in diag_1 and None not in diag_1:
        win = 'X'
    elif 'X' not in diag_1 and None not in diag_1:
        win = 'O'
    elif 'O' not in diag_2 and None not in diag_2:
        win = 'X'
    elif 'X' not in diag_2 and None not in diag_2:
        win = 'O'
    else:
        win = False
    if human_role==win:
        print('You win!')
        return True 
    if computer_role==win:
        print('You lose!')
        return True 
    
    ##check if full
    if game_state.turns == 9:
        print('Tie!')
        return True 
    return False 
    
def player_move():
    if game_state.active == 'H':
        y_coord = int(input('Enter your row '))
        if y_coord > 3 or y_coord < 1:
            print('Input must be a single number between 1 and 3, try again')
            player_move()
            return
        x_coord = int(input('Enter your column '))
        if x_coord > 3 or x_coord < 1:
            print('Input must be a single number between 1 and 3, try again')
            player_move()
            return
        if (x_coord, y_coord) in used_coords:
            print('Sorry, this space is taken')
            player_move()
            return
        used_coords.append((x_coord, y_coord))
        game_board[y_coord-1][x_coord-1].fill_square(human_role)
        game_board_display[y_coord-1][x_coord-1] = human_role
        game_state.active = 'C'
        game_state.turns+=1
    else:
        message = 'Not your turn'
        return
    

def computer_move():
    y_coord = random.randint(1, 3)
    x_coord = random.randint(1, 3)
    if (x_coord, y_coord) in used_coords:
        computer_move()
        return
    print("Computer's turn\n")
    used_coords.append((x_coord, y_coord))
    game_board[y_coord-1][x_coord-1].fill_square(computer_role)
    game_board_display[y_coord-1][x_coord-1] = computer_role
    game_state.active = 'H'
    game_state.turns += 1  

while not check_win():
    print(game_board_display[0])
    print(game_board_display[1])
    print(game_board_display[2])
    print('')
    print('')
    """
    print([x.contents for x in game_board[0]])
    print([x.contents for x in game_board[1]])
    print([x.contents for x in game_board[2]])
    """
    if game_state.active == 'H':
        player_move()
    else:
        computer_move()

print(game_board_display[0])
print(game_board_display[1])
print(game_board_display[2])
