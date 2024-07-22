import random
from enum import Enum
from collections import defaultdict
MAX_NUMBER = 100


class Clue(Enum):
    HIGHER = "too low!"
    LOWER = "too high!"
    MATCH ="a match!"

def generate_random_number(n):
    return random.randint(1, n)

def compare_guess_to_number(guess, target) -> Clue:
    # implement me
    if guess < target:
        return Clue.HIGHER
    elif guess > target:
        return Clue.LOWER
    else:
        return Clue.MATCH

def play_round(lowest, highest, number):
    tries = 1
    while True:
        print("Attempt:", tries)
        print(f"Suggestions {(lowest + highest)//2}")
        guess = int(input(f'{lowest}-{highest}> '))

        result = compare_guess_to_number(guess, number)
        if result == Clue.HIGHER:
            lowest = guess + 1
        elif result == Clue.LOWER:
            highest = guess - 1
        else:
            break
        print(f"Your guess was {result.value}")
        tries += 1
    print("Well done!")
    print(f"It took you {tries} tries")

    return tries
def game():
    result_table = defaultdict(list)
    while True:
        print("How hard do you want to make it?")
        print("10/100/1000/10,000/more!")
        max_value = int(input("Max value> "))
        number = generate_random_number(max_value)
        print(f"Guess a number between 1 and {max_value}")
        result = play_round(1, max_value, number)
        result_table[max_value].append(result)
        if input("Play again y/n>").casefold() != 'y':
            break

if __name__ == '__main__':
    game()
