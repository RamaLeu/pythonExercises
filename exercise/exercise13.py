def fibonacci(num):
     n1 = 0
     n2 = 1
     list= []
     list.append(n1)
     list.append(n2)
     for i in range(num - 2):
         temp = n1 + n2
         n1 = n2
         n2 = temp
         list.append(n2)
     return list

def main():
    size = int(input("How many fibonacci numbers you want to generate?: "))
    fibonacci_list = fibonacci(size)
    print(fibonacci_list)

main()
