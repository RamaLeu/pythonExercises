import random

words = ["betray",
         "price",
         "temptation",
         "interrupt",
         "Europe",
         "red",
         "shareholder",
         "fresh",
         "eternal",
         "hemisphere",
         "crossing",
         "factor",
         "primary",
         "joint",
         "sofa",
         "reference",
         "loyalty",
         "technique",
         "camp",
         "string",
         "nuance",
         "island",
         "hurl",
         "singer",
         "evoke",
         "plastic",
         "trail",
         "battery",
         "article",
         "medieval"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(",")", "_", "+"]


def main():
    pick = input("How strong do you want your password to be? 'Weak' 'Strong' or 'Uncrackable")
    pick = pick.lower()
    password = ""
    if pick == "weak":
        password = random.choice(words) + random.choice(words)
    elif pick == "strong":
        password = random.choice(words) + random.choice(words).upper() + str(random.randint(1, 9999))
    elif pick == "uncrackable":
        password = random.choice(symbols) + str(random.randint(1, 9999)) + random.choice(words).upper() + random.choice(words).lower() + random.choice(symbols) + str(random.randint(1, 9999))
    print(password)

main()
