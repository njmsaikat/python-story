age = input("Tell me your age: ")
print(type(age))

age = int(age)  # type conversion string to integer
print(type(age), "\n")

new_age = age + 1

print("You are going to be: " + str(new_age) + "\n")  # type conversion int to str

print("you will be: {}".format(new_age))  # old way of formatting with format function

print(f"Your are gonna be: {new_age}")  # new way called literal string
