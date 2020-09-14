import random

# define constant
MIN = 100
MAX = 999

# define count
count = 0
player_credits = 15


# define credits
def apply_credits(guesses):
    global count
    max_credits = 60
    if count <= 5:
        num_credits = max_credits // guesses
    elif 5 < count <= 10:
        num_credits = 10
    else:
        num_credits = 0
    return num_credits


# define numeric
def check_numeric(prompt):
    global count
    guess = input(prompt)
    count += 1
    while not is_integer(guess):
        print("Must be an integer. Try again.")
        guess = input(prompt)
        count += 1
    return int(guess)


# define range
def check_range(prompt):
    guess = check_numeric(prompt)
    while guess < MIN or guess > MAX:
        print("Out of range. Try again.")
        guess = check_numeric(prompt)
    return guess


# define game intro
def game_intro():
    message = """
                   --- G U E S S I N G   G A M E ---

                       L E T' S     P L A Y !

             Try to guess my three_digit combination, and
             I will tell you if any your numbers match my
             combination.

             Credits
                        1-4   Guesses: up to 60 credits
                        5-10  Guesses: 10 credits
    """
    print(message)


# define input is integer or not
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# define matches
def matches(number, guess):
    num_matches = 0

    num_hundreds = number // 100
    num_units = number % 100

    guess_hundreds = guess // 100
    guess_units = guess % 100

    if num_hundreds == guess_hundreds or num_hundreds == guess_units:
        num_matches += 1

    if num_units == guess_hundreds or num_units == guess_units:
        num_matches += 1

    return num_matches


# define playing game
def play_game():
    global count, player_credits
    count = 0
    player_credits -= 10
    right_answer = random.randint(MIN, MAX)
    print(f"right_answer: {right_answer}")
    done = False
    print("player credits:", player_credits)

    while not done:
        guess = check_range("Your guess? ")
        if guess != right_answer:
            num_matches = matches(right_answer, guess)
            print(f"Matched {num_matches} numbers.")

            if guess < right_answer:
                print("It's lower.")
            elif guess > right_answer:
                print("It's higher.")
        else:
            print(f"You got it right in {count} tries!")
            done = True
    return count


# runs all definition
def main():
    # create a while loop for multiple games
    # game_credits += apply_credits()
    global player_credits
    game_credits = 0
    game_intro()
    again = "y"
    print("player credits:", player_credits)

    # repetitive games
    while again[0].lower() == "y":
        if player_credits >= 10:
            game_credits += apply_credits(play_game())
            print(f"Game Credits: {game_credits}")
            player_credits += game_credits
            again = input("Would you like to try again? y/n: ")
        else:
            again = "no"

    print("player credits:", player_credits)
    print("E N D   G A M E")
    print("Goodbye")
    print("Overall results:")
    print(f"Total games   = ")
    print(f"Total guesses = ")
    print(f"Guesses/game  = ")
    print(f"Best game     = ")
    print(f"Total Credits = ", {player_credits})


main()
