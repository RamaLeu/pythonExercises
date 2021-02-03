def second_exercise_with_extras():
    number = int(input("Enter a number"))
    if number % 4 == 0:
        print("Its a multiple of 4")
    elif number % 2 == 0:
        print("even")
    else:
        print("odd")

def extras():
    num = int(input("First number: "))
    check = int(input("Second number: "))

    if num % check == 0:
        print("first number divides evenly from second number")
    else:
        print("doesnt divide evenly")

extras()