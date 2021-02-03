string = input("Enter a word u want to be checked for a palindrome: ")
string_list = []
for item in string:
    string_list.append(item)
string_list.reverse()
reverse_joined =''.join(string_list)
if reverse_joined == string:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")