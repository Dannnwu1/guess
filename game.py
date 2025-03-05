import random


def main():
    guess_number()


def guess_number():
    number = random.randint(1, 100)
    while True:

        try:
            level = int(input("Level: "))
            if level < 0:
                raise ValueError
            break
        except ValueError:
            pass

    while True:

        while True:
            try:
                guess = int(input("Guess: "))
                break
            except ValueError:
                pass

        if guess == number:
            print("Just right!")
            break
        elif guess < number:
            print("Too small!")
        else:
            print("Too large!")


if __name__ == "__main__":
    main()
