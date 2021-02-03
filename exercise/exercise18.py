import random

def input_number():
    number = input("Enter a number: ")
    number = [int(i) for i in str(number)]
    return number

if __name__=="__main__":
    randnumb = random.randint(1000, 9999)
    rand_list = [int(i) for i in str(randnumb)]
    print(randnumb)
    correct = False
    while correct == False:
        cows = 0
        bulls = 0
        number = input_number()
        for i in range(len(rand_list)):
            if number[i] == rand_list[i]:
                cows +=1
            elif number[i] in rand_list:
                bulls += 1
        print("Cows: ", cows, "Bulls: ", bulls)
        if cows == 4:
            correct = True
    print("YOU WON, THE NUMBER WAS: ", randnumb)


