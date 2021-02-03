def get_number():
    return int(input("Give me a number: "))

def prime_check():
    number = get_number()
    list = range(2, number)

    for item in list:
        if number % item == 0:
            print("The number is not prime")
            break
        else:
            print("the number is prime")
            break

prime_check()