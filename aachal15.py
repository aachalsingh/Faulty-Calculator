# Faulty Calculator
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
print("1.Addition")
print("2.Sutraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter your choice(1,2,3 or 4) : "))
if choice == 1:
    if a == 56 and b == 9:
        print("Answer = 77")
    else:
        result = a+b
        print("Answer =", result)
elif choice == 2:
    if a == 45 and b == 10:
        print("Answer = 50")
    else:
        result = a-b
        print("Answer =", result)
elif choice == 3:
    if a == 45 and b == 3:
        print("Answer = 555")
    else:
        result = a*b
        print("Answer =", result)
elif choice == 4:
    if a == 56 and b == 6:
        print("Answer = 4")
    else:
        result = a/b
        print("Answer =", result)
else:
    print("INVALID INPUT!!!!")

