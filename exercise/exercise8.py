import random
def again():
    again = input("do you want to play again? y/n: ")
    while (again != "y") and (again != "n"):
        again = input("do you want to play again? y/n: ")
    if again == "y":
        rockpaperscissors()
    elif again == "n":
        print("GAME OVER")
def rockpaperscissors():
    answers = ["rock","paper", "scissors"]
    player1 = input("Choose 'Rock' 'Paper' or 'Scissors'")
    player1 = player1.lower()
    while player1 not in answers:
        player1 = input("Choose 'Rock' 'Paper' or 'Scissors'")
        player1 = player1.lower()
    player2 = random.choice(answers)
    print("Player2 chose: ",player2)
    if player1== "rock":
        if player2 == "rock":
            print("Tie, try again")
            rockpaperscissors()
        elif player2 == "scissors":
            print("Player1 Wins!")
            again()
        elif player2 == "paper":
            print("Player2 Wins!")
            again()
    elif player1 == "paper":
        if player2 == "rock":
            print("Player1 Wins!")
            again()
        elif player2 == "scissors":
            print("Player2 Wins!")
            again()
        elif player2 == "paper":
            print("Tie, try again")
            rockpaperscissors()
    elif player1 == "scissors":
        if player2 == "rock":
            print("Player2 Wins!")
            again()
        elif player2 == "scissors":
            print("Tie, try again")
            rockpaperscissors()
        elif player2 == "paper":
            print("Player1 Wins!")
            again()


rockpaperscissors()
