# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 02:41:17 2025

@author: SambesiweSli
"""

# Python program to play 21 Number game

import sys

# this function returns the nearest multiple to 4
def nearestMultiple(number):
    
    if number >= 4:
        near = number + (4 - (number % 4))
    else:
        near = 4
    return near

# this function prints if the user has lost
# and it exits the game
def lose():
    print('\n\nYOU LOSE!')
    print('Better luck next time.')
    sys.exit()
    
# this function checks whether the numbers are consecutive
def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i]-xyz[i-1]) != 1:
            return False
        i = i + 1
    return True

# this function starts the game
def start():
    xyz = []
    last = 0
    while True:
        print('Enter "F" to play FIRST.')
        print('Enter "S" to play SECOND.')
        chance = input('> ')
        
        # this is for the player who plays FIRST
        if chance == 'F':
            while True:
                if last == 20:
                    lose()
                else:
                    print('\nYour Turn.')
                    print('\nHow many numbers do you wish to enter?')
                    number_input = int(input('> '))
                    
                    if number_input > 0 and number_input <=3:
                        comp = 4 - number_input
                    else:
                        print('Wrong  input. You are disqualified from the game.')
                        lose()
                        
                    i, j = 1, 1
                    
                    print('Now enter the value(s)')
                    while i <= number_input:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i = i + 1
                        
                    # this is where we store the last element of xyz
                    last = xyz[-1]
                    
                    # checks whether the input
                    # numbers are consecutive
                    if check(xyz) == True:
                        if last == 21:
                            lose()
                            
                        else:
                            # computers turn
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print('\nYou did not input consecutive integers.')
                        lose()
                        
        elif chance == 'S':
            comp = 1
            last = 0
            while last < 20:
                # computers turn
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j += 1
                print("Order of inputs after computer's turn is: ")
                print(xyz)
                if xyz[-1] == 20:
                    lose()
                    
                else:
                    print('\nYour turn now.')
                    print('\How many numbers do you wish to enter?')
                    number_input = input('> ')
                    number_input = int(number_input)
                    i = 1
                    print('Enter your values')
                    while i <= number_input:
                        xyz.append(int(input('> ')))
                        i = i + 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        # print (xyz)
                        near =  nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print('\nYou did not input consecutive integers.')
                        print('You are disqualified from the game.')
                        lose()
            print('\n\nCONGRATULATIONS!!!')
            print('YOU WIN!')
            exit(0)
            
        else:
            print('Wrong choice')
            
game = True
while game == True:
    print('Player 2 is COMPUTER.')
    print('Do you want to play the 21 Number game? (YES / NO)')
    answer = input('> ')
    if answer == 'yes':
        start()
    else:
        print('Do you want to quit the game? (YES / NO)')
        next = input('> ')
        if next == 'yes':
            print('You are quitting the game...')
            exit(0)
        elif next == 'no':
            print('Continuing...')
        else:
            print('Wrong choice')