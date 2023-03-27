"Creating a guessing game"
secret_word = "gear"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("What moves has teeth and as well doesn't bite ")

while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter the correct answer ")
            guess_count += 1
        else:
            out_of_guesses = True

if out_of_guesses:
        print("Oops you've ran out of guesses, YOU LOSE!!")
else:
        print("You got the correct answer, YOU WIN!!")
