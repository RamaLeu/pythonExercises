import random

size_a = random.randint(10, 20)
size_b = random.randint(10, 20)
a = []
b = []
c = []
while len(a)<= size_a:
    a.append(random.randint(1, 20))
while len(b)<= size_b:
    b.append(random.randint(1, 20))
c = [item for item in a if item in b]
c = list( dict.fromkeys(c))
print(a)
print(b)
print(c)