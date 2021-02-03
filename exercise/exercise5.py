import random

x = []
while len(x)<= 100:
    x.append(random.randrange(0, 100))
y = []
while len(y)<= 100:
    y.append(random.randrange(0, 100))
z = []

for item in y:
    if item in x:
        z.append(item)

print(z)