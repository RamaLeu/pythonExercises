import random

def exit():
    print("you did not guess the number")
def number_Guess():
    found = False
    counter = 0
    number = random.randint(1, 9)
    while found == False:
        guess = input("Guess a number!")
        counter += 1
        if guess == "exit":
            exit()
            return
        guess = int(guess)
        if guess == number:
            print("you found it!, the number was:", number)
            found = True
        elif guess < number:
            print("too low, try again!")
        elif guess > number:
            print("too high, try again!")
    print("you took", counter,"tries")
    number_Guess()

number_Guess()