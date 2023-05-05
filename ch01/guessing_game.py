import random


def guessing_game():
    secret_num = random.randint(0, 100)

    loop = True
    while loop:
        guess = input("Guess a number from 0 to 100 inclusive: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid guess")
            continue

        if guess == secret_num:
            print("Correct!")
            loop = False
        elif guess < secret_num:
            print("Too low")
        elif guess > secret_num:
            print("Too high")
        else:
            print("Invalid guess")

    print("Game over")


if __name__ == "__main__":
    guessing_game()

