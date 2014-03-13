import random

guesses_taken = 0
print('Hello! What is your name?')
name = raw_input()
number = random.randint(1, 20)
guess = ''
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')


print('Take a guess.')

while guess != number:
    guess = input()
    guess = int(guess)
    if guess > number:
        guesses_taken = guesses_taken + 1
        print('Your guess is too high.')
    elif guess < number:
        guesses_taken = guesses_taken + 1
        print('Your guess is too low.')
    else:
        guesses_taken = guesses_taken + 1
        print('Good job, %s! You guessed my number in %d guesses!') % (name, guesses_taken)
