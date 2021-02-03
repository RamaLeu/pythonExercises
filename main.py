# String, Integer, bool, float, double, char

skaicius = 0
zodis = "zodis"
flag = False
floatas = 0.00002
count = 0
# --- Data structures-----
tv_list = ["samsung", "lg", "lenovo", "silelis"]
phone_list = ["iphone 12", "samsung 20", "nokia 3310"]
phone_list1 = ["Stringes", 1, 2, 3, 4, 5, 6, False]
number_list = [1, 2, 3, 4, 5, 6]
no_duplicate_phone_list = set(phone_list1)

mutable = ["iphone12", "samsung20"]
mutable[0] = "iphone13"
print(mutable)

# CONSTAI
immutable = {"iphone12", "samsung20"}

# HashMap
dictionary = {"mobile_phones": phone_list, "tv": tv_list}

print(dictionary["mobile_phones"])

# -------------------if logic gates--------------
if zodis == skaicius:
    print("HELLO THERE")
else:
    print("GOODBYE THERE")

if len(phone_list) == len(immutable):
    print("SITIE LISTAI YRA LYGUS")
elif phone_list == immutable:
    print("LYGUS LISTAI")
else:
    print("ERROR")

# --------------loops-------------
for i in phone_list:
    print(i)

while flag == False:
    count += 1
    count += 1
    if count > 5:
        flag = True
        print("Flag was changed")


def funkcija(sarasas, sarasas1):
    print(sarasas)
    print(sarasas1)


class User:
    def method(self, sarasas, sarasas1):
        print(sarasas)
        print(sarasas1)


funkcija(phone_list, tv_list)

user = User()

user.method(phone_list, tv_list)

pirmas_indeksas = phone_list[1]
print(pirmas_indeksas)

print(dictionary["mobile_phones"])
print(dictionary.values())


# ----------------Bubble sort------------
# [7, 3, 2, 8, 2, 1 ,5, 3, 2, 1, 7, 3, 2] => Bubble sort
# 1: while loop
# 2: 7, 3 -> is 7 higher

def bubble_sort():
    unsorted_list = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    is_sorting_finished = False
    iteration_counter = 0
    while is_sorting_finished == False:
        did_sort_happen = False
        for i in range(len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp
                did_sort_happen = True
            iteration_counter += 1
        iteration_counter += 1
        if did_sort_happen == False:
            is_sorting_finished = True

    print(unsorted_list)
    print("iterations: ", iteration_counter)


#    -------------------------------
#   /  22222
#  /       22
# /       22
# /     2222222
bubble_sort()


# def fibonacci():
# n1 = 0
# n2 = 1
# do_fibonacci = True
# print(n1)
# print(n2)
# while do_fibonacci == True:
# nextN = n1 + n2
# n1 = n2
# n2 = nextN
# print(nextN)
# if nextN>40000:
# do_fibonacci= False

# fibonacci()

# def fibonacci(fib_index):
#     n1 = 0
#     n2 = 1
#     fib_sequence = [n1, n2]
#     for i in range(fib_index - 2):
#         n1 = fib_sequence[-2]
#         n2 = fib_sequence[-1]
#         newN = n1 + n2
#         fibonacci(fib_index)
#         fib_sequence.append(newN)
#     print(fib_sequence)
#
#
# fibonacci(100)
# i = 0
# def fibonacci_recursive(a, b, i, index):
#     a = 0
#     b = 1
#     i += 1
#     if index != i:
#         fibonacci_recursive(a, b, index)

#fibonacci_recursive(0, 1, i, 500)


# def carry_solver(n1, n2):
#     counter = 0
#     longer_number = max(len(str(n1)), len(str(n2)))
#     carry_in_mind = 0
#     for i in reversed(range(longer_number)):
#         carry_in_mind = n1 % 10 + n2 % 10 + carry_in_mind
#         if carry_in_mind >= 10:
#             carry_in_mind = 1
#         else:
#             carry_in_mind= 0
#         counter += carry_in_mind