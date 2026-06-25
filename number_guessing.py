
import random

def guess_number(low, high, num_attempts):
    """
    This function, named 'guess_number', generates a psudo-random integer in a given range, inclusive.
    The user is given a certain number of attempts to guess the correct number.
    The function prints the range to the user and informs the user of how many attempts they have.
    The function asks the user to guess the number the given number of times.
    You must use the random module's randint function to generate the pseudo-random integer.
    You must use a for loop to give the user multiple attempts.
    If the user enters a non-numeric response, the program must not crash, but simply count that as an incorrect answer.
    If the user guesses any attempt correctly, the function immediately exits the loop and returns True.
    If the user enters all attempts incorrectly, the function returns False.

    :param low: The low end of the range in which the pseudo-random number is generated.
    :param high: the high end of the range in which the pseudo-random number is generated.
    :param num_attempts: The number of attempts the user is given to guess the correct number.
    :returns: True if the user answers any attempt correctly, False otherwise.
    """
    # Generate random number
    secret_num = random.randint(low, high)
    # Print game info
def guess_number(low, high, num_attempts):
    secret = random.randint(low, high)
    print(f"Guess a number between {low} and {high}. You have {num_attempts} attempts.")
    
    for _ in range(num_attempts):
        user_input = input("Enter your guess: ")
        try:
            guess = int(user_input)
        except ValueError:
            # 非数字直接算作错误，继续下一轮
            continue
        
        if guess == secret:
            return True
    # 用尽所有机会
    return False



