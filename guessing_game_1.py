def guessing_game():
    right_answer = 8
    done = False
    count = 0
    print("Thinking of a number 1 t0 20. ")
    print("What do you think it is?")
    while not done:
        guess = int(input("Your guess: "))
        count += 1
        if guess < right_answer:
            print("Too low.")
        elif guess > right_answer:
            print("Too high.")
        elif guess == right_answer:
            print(f"Congratulation! You guessed the right answer in {count} tries!")
            done = True


def main():
    print(" --- G U E S S I N G   G A M E --- ")
    guessing_game()
    print("Bye!")


main()