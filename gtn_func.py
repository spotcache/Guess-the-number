from random import randint
from time import sleep

def gtn(x):
    secret_num, guess, attempts =  randint(1,x), 0, 0
    while guess != secret_num:
        try:
            guess = int(input(f"Guess the number between (0-{x}): "))
        except ValueError:
            print('Enter a number!')
        attempts += 1
        if guess > secret_num:
            print('Too high, try again 👆')
        elif guess < secret_num:
            print('Too low, try again 👇')
    print(f'Congrats you guessed the number {secret_num} in {attempts} attempts 🎉!')
    sleep(3)