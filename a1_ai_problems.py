# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

string = "?eman ruoy s'tahw ,nivek si eman ym  "
reverse_string = string[::-1]

print(reverse_string)  # Output should be "Your stored value"




# Function to print Fibonacci sequence
def fibonacci(n):
    sequence = [1, 2]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Input from the user
num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))

# Display the sequence
print(f"Fibonacci sequence with {num_terms} terms: {fibonacci(num_terms)}")








import random

def spin_wheel():
    return random.randint(1, 36)

def get_bet():
    while True:
        try:
            bet = int(input("Enter a number between 0 and 36 to bet on: "))
            if 0 <= bet <= 36:  # Changed condition to include 0
                return bet
            else:
                print("Invalid input. Please enter a number between 0 and 36.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to Roulette!")
    while True:
        bet = get_bet()
        print("Spinning the wheel...")
        
        result = spin_wheel()
        print(f"The wheel landed on {result}.")
        
        if bet == result:
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Better luck next time!")
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    main()
