def input_name():
    text = input("Type in some text: ")
    return text

def text_edit(text):
    text_list = text.split(" ")
    text_list.reverse()
    result = " ".join(text_list)
    return result
def main():
    text = input_name()
    result = text_edit(text)
    print(result)

main()