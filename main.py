from checkwin import CheckWin
import os
import random

# Defining the board
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
def board(A, B, C, D, E, F, G, H, I):
    print(f'''         {A} | {B} | {C}
        ---|---|--- 
         {D} | {E} | {F}
        ---|---|---
         {G} | {H} | {I}''')

player_won = CheckWin()

game_on = True
xo_list = ['X']
played_coords = []
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

opponent = input("Type 'C' to play against computer or 'H' to play against a human: ").lower()

if opponent == 'h':
    while game_on:
        os.system('cls')
        board(A, B, C, D, E, F, G, H, I)
        # putting the location of the letter
        player_input = int(input(f"Player {xo_list[-1]}\nEnter your position (1-9): "))
        print("\n")
        while player_input not in range(1, 10):
            print("Error: choose between 1 and 9")
            player_input = int(input("\nEnter your position (1-9): "))
        while player_input in played_coords:
            print("Error: That positon has been played")
            player_input = int(input("\nEnter your position (1-9): "))
            if player_input not in range(1, 10):
                while player_input not in range(1, 10):
                    print("Error: choose between 1 and 9")
                    player_input = int(input("\nEnter your position (1-9): "))       
        played_coords.append(player_input)


        if player_input == 1:
            A = xo_list[-1]
        elif player_input == 2:
            B = xo_list[-1]
        elif player_input == 3:
            C = xo_list[-1]
        elif player_input == 4:
            D = xo_list[-1]
        elif player_input == 5:
            E = xo_list[-1]
        elif player_input == 6:
            F = xo_list[-1]
        elif player_input == 7:
            G = xo_list[-1]
        elif player_input == 8:
            H = xo_list[-1]
        elif player_input == 9:
            I = xo_list[-1]
        
        if xo_list[-1] == "X":
            xo_list.append("O")
        elif xo_list[-1] == "O":
            xo_list.append("X")

        if player_won.win_check(A, B, C, D, E, F, G, H, I):
            os.system('cls')
            board(A, B, C, D, E, F, G, H, I)
            print(f"\nPlayer {xo_list[-2]} wins!")
            break

        elif len(xo_list) == 9:
            os.system('cls')
            board(A, B, C, D, E, F, G, H, I)
            print("Draw!")
            break

else:
    print("Player plays first, letter is X")
    list_of_choice = 1
    while game_on:
        os.system('cls')
        board(A, B, C, D, E, F, G, H, I)
        player_input = int(input("\nEnter your position (1-9): "))
        while player_input not in choices:
            print("Error: That positon has been played")
            player_input = int(input("\nEnter your position (1-9): "))
        choices.remove(player_input)

        if player_input == 1:
            A = 'X'
        elif player_input == 2:
            B = 'X'
        elif player_input == 3:
            C = 'X'
        elif player_input == 4:
            D = 'X'
        elif player_input == 5:
            E = 'X'
        elif player_input == 6:
            F = 'X'
        elif player_input == 7:
            G = 'X'
        elif player_input == 8:
            H = 'X'
        elif player_input == 9:
            I = 'X'

        if player_won.win_check(A, B, C, D, E, F, G, H, I):
            os.system('cls')
            board(A, B, C, D, E, F, G, H, I)
            print("\nPlayer wins!")
            break
        
        elif len(choices) == 0:
            os.system('cls')
            board(A, B, C, D, E, F, G, H, I)
            print("\nDraw!")
            break

        computer_choice = random.choice(choices)
        choices.remove(computer_choice)

        if computer_choice == 1:
            A = 'O'
        elif computer_choice == 2:
            B = 'O'
        elif computer_choice == 3:
            C = 'O'
        elif computer_choice == 4:
            D = 'O'
        elif computer_choice == 5:
            E = 'O'
        elif computer_choice == 6:
            F = 'O'
        elif computer_choice == 7:
            G = 'O'
        elif computer_choice == 8:
            H = 'O'
        elif computer_choice == 9:
            I = 'O'
        
        list_of_choice += 1

        if player_won.win_check(A, B, C, D, E, F, G, H, I):
            os.system('cls')
            board(A, B, C, D, E, F, G, H, I)
            print("\nComputer wins!")
            break