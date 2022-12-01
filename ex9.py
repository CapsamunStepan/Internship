from random import randint
rand_number = randint(1, 9)
k = 0

while True:
    number = input('Try to guess a number: ')
    if number == "exit":
        print("Goodbye!")
        break
    number = int(number)
    k += 1
    if number > rand_number:
        print("It's to high!")
    elif number < rand_number:
        print("It's to low!")
    elif number == rand_number:
        print("You guessed it!")
        print(f'You have taken {k} guesses.')
        break
