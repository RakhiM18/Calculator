def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    return a / b

print("Select Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1','2','3','4'):
        n1 = float(input("Enter first number:"))
        n2 = float(input("Enter second number:"))

        if choice == '1':
            print(n1, "+", n2, "=", add(n1,n2))

        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1,n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1,n2))

        elif choice == '4':
            print(n1, "/", n2, "=", div(n1,n2))
        break
    else:
        print("Invalid input")