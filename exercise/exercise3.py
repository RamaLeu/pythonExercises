def less_then_5():
    a = [1, 1, 2, 3, 6, 8, 13, 21, 34, 55, 89]
    b = []
    number = int(input("enter a number u want to see smaller elements than: "))
    for item in a:
        if item < number:
            b.append(item)
    print(b)

less_then_5()