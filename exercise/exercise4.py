def divisors():
    number = int(input("Input a number u want divisors of: "))
    x = range(1, number + 1)
    divisors = []
    for item in x:
        if number % item == 0:
            divisors.append(item)

    print("Divisors: ", divisors)

divisors()