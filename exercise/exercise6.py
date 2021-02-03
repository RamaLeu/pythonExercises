string = input("Enter a word u want to be checked for a palindrome: ")
string_list = []
for item in string:
    string_list.append(item)

string_list.reverse()
print(string_list)