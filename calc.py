"""
This is a simple arithmetic calculator for testing purposes
"""
# get to Integer inputs for calculation
int1 = int(input("Enter an integer: "))
int2 = int(input("Another one: "))

# ask for an operation to perform
result = None
while True:
    op = int(input("Do you want to add (1) / subtract (2) / multiply (3) / divide (4) ? "))
    if op == 1:
        print("Let's add!")
        result = int1 + int2
        break
    elif op == 2:
        print("Let's subtract!")
        result = int1 - int2
        break
    elif op == 3:
        print("Let's multiply!")
        result = int1 * int2
        break
    elif op == 4:
        if int2 == 0:
            print("Can't divide by zero, please try again")
            continue
        print("Let's divide!")
        result = int1 // int2
        break

# Print the result
print("The result is", result)

