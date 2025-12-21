import math
from operator import add

class Calculator:
    print("Simple Calculator")
    print("\nWelcome")

    print("\nSelect operations:")
    print("\n1. Addition")
    print("\n2. Subtraction")
    print("\n3. Multiplication")
    print("\n4. Division")
    print("\n5. Square Root")
    print("\n6. power(a^b)")
    print("\n7. modulus")
    print("\n8. Exit")

    option = (input("\nEnter choice(1/2/3/4/5/6/7/8): "))
        
    a = int(input("\nEnter first number (a): "))
    b = int(input("\nEnter second number (b): "))

    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b
    
    def power(a, b):
        return a ** b
    
    def modulus(a, b):
        return a % b
    
    match option:
        case '1':
            print("Result:", add(a, b))

        case '2':
            print("Result:", subtract(a, b))

        case '3':
            print("Result:", multiply(a, b))
        case '4':
            print("Result:", divide(a, b))
        
        case '5':
            print("Result:", math.sqrt(a))
        
        case '6':
            print("Result:", power(a, b))
        
        case '7':
            print("Result:", modulus(a, b))

        case '8':
            print("Exiting the calculator.")

        case _:
            print("Invalid input")