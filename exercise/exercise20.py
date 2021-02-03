import random

def binary_search(find, list):
    half_num = int(len(list)/2)
    half = list[half_num]
    if find < half:
        copy = list[0:half_num]
        half_num2 = int(len(copy)/2)
        half = copy[half_num2]
        if find < half:
            answer = copy[0]
            if answer == find:
                print(find, "is in the list")
            else:
                print(find, "is not in the list")
        elif find > half:
            answer = copy[2]
            if answer == find:
                print(find, "is in the list")
            else:
                print(find, "is not in the list")
        elif find == half:
            print(find, "is in the list")
    elif find > half:
        copy = list[half_num+1:7]
        half_num2 = int(len(copy)/2)
        half = copy[half_num2]
        if find < half:
            answer = copy[0]
            if answer == find:
                print(find, "is in the list")
            else:
                print(find, "is not in the list")
        elif find > half:
            answer = copy[2]
            if answer == find:
                print(find, "in the list")
            else:
                print(find, "is not in the list")
        elif find == half:
            print(find, "is in the list")
    elif find == half:
        print(find, "is in the list")

if __name__ == '__main__':
    a = []
    for i in range(0, 7):
        number = random.randint(1, 500)
        a.append(number)
    a.sort()
    print("List: ", a)
    searchable = int(input("Input a number u want to search: "))
    binary_search(searchable, a)