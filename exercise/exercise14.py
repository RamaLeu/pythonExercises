import random


def makelist_loop():
    size_l = random.randint(5, 10)
    l = []
    while len(l)<= size_l:
        item = random.randint(1, 20)
        if item not in l:
            l.append(item)
    return l

def makelist_set():
    size_s = random.randint(1, 10)
    s = set()
    while len(s) <= size_s:
        item = random.randint(1, 20)
        s.add(item)
    return s

def main():
    list_one = makelist_loop()
    list_two = makelist_set()
    print(list_one)
    print(list_two)

main()
