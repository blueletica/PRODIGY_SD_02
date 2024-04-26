import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (between 1 and 100): ")

        try:
            guess = int(guess)
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
