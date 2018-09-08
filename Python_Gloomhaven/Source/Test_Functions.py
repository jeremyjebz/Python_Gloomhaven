def data_types ():
    print("***Data Types***")
    
    MyFloat = float(10)
    MyString = "hello"
    MyInt = 20
    
    print("Float: " + str(isinstance(MyFloat, float)))
    print("String: " + str(isinstance(MyString, str)))
    print("Int: " + str(isinstance(MyInt, int)))

def lists():
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


def miscellaneous():
    print("***Miscellaneous***")
    
    x = 11
    y = 13
    
    if x == 10:
        print(1)
    elif y == 12:
        print(2)
    else:
        print(3)
    
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    for num in numbers:
        if not (num < 15):
            break
        elif num % 2 == 0:
            print("Even! - %d" % num)
        else:
            print("Odd! - %d" % num)