#
# Data Types
#
print("***Data Types***")

MyFloat = float(10)
MyString = "hello"
MyInt = 20

print("Float: " + str(isinstance(MyFloat, float)))
print("String: " + str(isinstance(MyString, str)))
print("Int: " + str(isinstance(MyInt, int)))

#
# Lists
#
print("***Lists***")

numbers = []
strings = []
names = ["Billy", "Bob", "John"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("One")
strings.append("Two")
strings.append("Three")

print(numbers)
print(strings)
print(names[1])
