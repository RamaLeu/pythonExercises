import random

def makelist():
    list = []
    size = random.randint(10, 20)
    for i in range(0, size):
        list.append(random.randint(1, 50))
    return list

def give_first_last(list):
    new_list = []
    new_list.append(list[0])
    new_list.append(list[len(list)-1])
    return new_list


def main():
    a = makelist()
    b = give_first_last(a)
    print(a)
    print(b)

main()