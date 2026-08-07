print()

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    if b==0:
        print(" Division by zero is undefined! Please enter a non-zero number and try again.")
        return None
    else:
        return a/b
print()
while True:
    print("========== SIMPLE CALCULATOR ==========")
    a = float(input("Enter a number: "))
    b = float(input("Enter second number: "))
    print()
    print("Select an Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter a choice (1,2,3,4, & 5): ")
    print()
    if choice == "1":
        print( a, " + ", b, " = ", add(a,b))
    elif choice == "2":
        print( a, " - ", b, " = ", subtract(a,b))
    elif choice == "3":
        print( a, " x ", b, " = ", multiply(a,b))
    elif choice == "4":
        print(f"{a} / {b} = {divide(a,b):.2f}")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("No operations are chosen!")
        break
    print()
print()