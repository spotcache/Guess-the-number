from gtn_func import gtn
from os import system
from time import sleep

system('cls')
x = 0
try:
    x = int(input("Enter the max number for the guess: "))
except ValueError:
    print('Enter a number!')
    sleep(2)
    exit()
system('cls')

while True:
    gtn(x) # type: ignore
    system('cls')
    replay = input("Would you like to play again? (y/n): ").lower()
    system('cls')
    if replay == 'y':
        continue
    else:
        sleep(0.5)
        exit("Bye bye then... 👋")