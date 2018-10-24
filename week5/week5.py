# Void Function (just like that bank statement bro)
def multiply_by_5(x):
    x *= 5
    print(x)


multiply_by_5(5)
print("This is a parameter")


# Return Function
def multiply_by_5(x):
    x *= 5
    return x


print(multiply_by_5(5))
y = multiply_by_5(5)
y /= 5
print(y)

if multiply_by_5(1) > 5:
    print("true")
else:
    print("false")

example1 = {"one": "uno", 2: "two"}
print(example1[2])

example1["three"] = 3
print(example1)

example1.pop(2)
print(example1)

age = int(input("How old are you? "))
print("Your age is ", age)
multiply_by_5(age)
print(multiply_by_5(age))

file = open("Week5.txt.txt")
for line in file:
    print(line)

for line in file:
    if line.startswith("Name"):
        print(line)

file = open("Week5.txt", 'w')
file.write("I love Python and FTC!")
file = open("Week5.txt")
for line in file:
    print(line)
