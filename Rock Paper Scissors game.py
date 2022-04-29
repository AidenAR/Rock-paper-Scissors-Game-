##A simple Rock Paper Scissors game with the option of a rematch,
## if the user desires.

import random


## Constants:

symbol_msg = "Please enter 'p' for paper, 'r' for rock or 's' for scissors: "
sym_lst = ['r', 's', 'p']
comp_move_text = "Computer's move is: {0}"
player_move_text = "{0} move is: {1}"
win_msg = "Congratulations, you won, {0}!"
loss_msg = "Sorry, the computer won. Better luck next time, {0} :)"
replay_msg = "Would you like to play again, {0}?\nType y for Yes and n for No:"
goodbye_msg = "Thanks for playing, {0}. Bye!!"


def rps_rules(player, opp):
    if (player == 'r' and opp == 's') or \
        (player == 's' and opp == 'p') or \
        (player == 'p' and opp == 'r'):
        return True 
    else:
        return False


def rps():
    player_move = None
    name = input("Please enter your name: ")
    name_move_output = name + "'s"
    print("Hello " + name + "!")
    while True:
        print("Let's play!")
        computer_move = random.choice(sym_lst)
        while player_move not in sym_lst:
            player_move = input(symbol_msg).lower()
        print(comp_move_text.format(computer_move))
        print(player_move_text.format(name_move_output, player_move))
        if computer_move == player_move:
            print("Tied game :)")
        else:
            result = rps_rules(player_move, computer_move)
            if result == True:
                print(win_msg.format(name))
            else:
                print(loss_msg.format(name))
        rematch = input(replay_msg.format(name)).lower()
        if rematch != 'y':
            break
    print(goodbye_msg.format(name))


rps()