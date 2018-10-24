import random
import math

print(random.randint(5, 10))

x = 3
if x % 2 == 0:
    print(str(x) + " is even")
else:
    print(str(x) + " is odd")

print(math.sqrt(6))
print(int(math.pow(999, 3)))

print(math.ceil(32.3))
print(math.floor(57.98888))

n = 3
while n > 0:
    print(n)
    n -= 1
print("Blastoff!")

new_list = [1, 2, 3, 4, 27]
# keys =    0 1 2 3 4

# print(new_list.3)
print(new_list[2])
new_list.append(29)
print(new_list)

names = ["Varun", "Pasha", "Vinay", "Aarav", "Kinshuk"]
for name in names:
    x = random.randint(0, 4)
    print(names[x])
    print("Hello " + name)

for x in [1, 2, 3, 4, 5]:
    print(x)

for x in range(10):  # exclusive, starts at0
    print(x)

for y in reversed(names):
    print(y)

x = -1
while True:  # infinite loop
    x += 1
    if x == 3:
        continue
    print(x)
    if x == 5:
        break

y = 6
while y > 0:
    y -= 1
    if y == 2:
        continue
    print(y)

num_list = []
x = 8
while x <= 40:
    num_list.append(x)
    x += 1

for ihavenoidea in num_list:
    if ihavenoidea % 2 == 0:
        print(ihavenoidea)
