import random

guesses_taken = 0
print('Hello! What is your name?')
name = raw_input()
number = random.randint(1, 20)
guess = 0
print('Well, {0}, I am thinking of a number between 1 and 20.').format(name)


print('Take a guess.')

while guess != number:
    guess = int(input())
    guesses_taken += 1
    if guess > number:
        print('Your guess is too high.')
    elif guess < number:
        print('Your guess is too low.')
    else:
        print('Good job, {0}!').format(name)
        print('You guessed my number in {0} guesses!').format(guesses_taken)
