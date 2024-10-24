import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range of numbers for guessing
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))

    # Generate a random number within the range
    target_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    max_attempts = 7  # Limiting the number of attempts for added challenge

    print(f"\nI have selected a number between {lower_limit} and {upper_limit}. You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        # Get user's guess
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        # Check the guess
        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts!")
            break

        # Display remaining attempts
        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts left.")
        else:
            print(f"Sorry, you've used all your attempts. The correct number was {target_number}.")

    print("\nGame Over. Thanks for playing!")

# Main Program
if __name__ == "__main__":
    number_guessing_game()
