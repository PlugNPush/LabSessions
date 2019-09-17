from time import sleep
import math
import sys
choice = choice = int(input("Welcome. Chose one option to start.\n1 - Addition of 2 numbers\n2 - Addition of 3 numbers\n3 - Draw an F with # signs\n4 - Draw a C with # signs\n5 - Draw 5 F with # signs\n6 - Write personal informations\n7 - Hello!\n8 - Average calculation\n9 - Elapsed time calculator\n10 - Check if two number are equal\n11 - Even or Odd numbers\n12 - Maximum and minimum\n13 - Sum of x*x.\n14 - Xn and Wn\n15 - Leap Year\n16 - DELTA (Python Edition)\n17 - Calculator\n18 - PENDING...\n"))
print("\n")
if choice == 1:
    nb = int(input("Enter the first number : "))
    nb += int(input("\nEnter the second number : "))
    print("\nThe result is", nb)
elif choice == 2:
    nb = int(input("Enter the first number : "))
    nb = nb + int(input("\nEnter the second number : "))
    nb += int(input("\nEnter the third number : "))
    print("\nThe result is", nb)
elif choice == 3:
    print("", "#" * 5, "\n", "#" * 1, "\n", "#" * 1, "\n", "#" * 4, "\n", "#" * 1, "\n", "#" * 1, "\n", "#" * 1, "\n")
elif choice == 4:
    print(" " * 7, "#" * 6, "\n", " " * 2, "#" * 2, " " * 10, "#" * 2, "\n", "#" * 1, "\n", "#" * 1, "\n", "#" * 1, "\n", "#" * 1, "\n", "#" * 1, "\n",  " " * 2, "#" * 2, " " * 10, "#" * 2, "\n", " " * 7, "#" * 6, "\n")
elif choice == 5:
    print("", "#" * 5, " " * 3, "#" * 5, " " * 3, "#" * 5, " " * 3, "#" * 5, " " * 3, "#" * 5, "\n", "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, "\n", "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, "\n", "#" * 4, " " * 4,  "#" * 4, " " * 4,  "#" * 4, " " * 4,  "#" * 4, " " * 4,  "#" * 4, "\n",  "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, "\n",  "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, "\n",  "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, " " * 7, "#" * 1, "\n")
elif choice == 6:
    print("Name: Michael\nDate of birth: 07/07/2000\nMobile phone number: +33 6 52 72 77 23\n")
elif choice == 7:
    firstname = input("What's your first name? ")
    lastname = input("Okay, what about your last name? ")
    print("Hello first name last name")
    sys.stdout.flush()
    sleep(3)
    print("\nJust kidding, Hello", firstname, lastname, "!\n")
elif choice == 8:
    nb = int(input("Enter the first number : "))
    nb += int(input("\nEnter the second number : "))
    nb += int(input("\nEnter the third number : "))
    print("\nThe result is", nb/3)
elif choice == 9:
    odays = int(input("How many days elapsed? "))
    nbyears = odays/int(365)
    restyears = odays%365
    nbweeks = restyears/7
    restweeks = restyears%7
    nbdays = restweeks
    print("For", odays, "elapsed days, it has been", int(nbyears), "years,", int(nbweeks), "weeks and", nbdays, "days.")
elif choice == 10:
    nba = int(input("Please enter the first number: "))
    nbb = int(input("Please enter the second number: "))
    if nba == nbb:
        print("These two numbers are equal.")
    else:
        print("These two numbers are not equal.")
elif choice == 11:
    number = int(input("Please enter the number: "))
    if number % 2 == 0:
        print(number, "is an Even number.")
    else:
        print(number, "is an Odd number.")
elif choice == 12:
    nba = int(input("Please enter the first number: "))
    nbb = int(input("Please enter the second number: "))
    nbc = int(input("Please enter the third number: "))
    print("The maximum of these number is", max(nba, nbb, nbc), "and the minimum is", min(nba, nbb, nbc))
    sys.stdout.flush()
    sleep(3)
    print("OKAY FINE I will calculate it by my self instead of using the built-in Python function... Please wait.\n")
    sys.stdout.flush()
    sleep(3)
    if nba < nbb:
        maximum = nbb
        minimum = nba
        if nbb > nbc:
            maximum = nbb
            if nbc > nba:
                minimum = nba
            else:
                minimum = nbc
        else:
            maximum = nbc
            if nbb > nba:
                minimum = nba
            else:
                minimum = nbb
    else:
        maximum = nba
        minimum = nbb
        if nba > nbc:
            maximum = nba
            if nbb > nbc:
                minimum = nbc
            else:
                minimum = nbb
        else:
            maximum = nbc
            if nba > nbb:
                minimum = nbb
            else:
                minimum = nba
    print("The maximum of these number is", maximum, "and the minimum is", minimum)
elif choice == 13:
    x = int(input("What's the value of x? "))
    n = int(input("What's the value of n? "))
    res = 0
    i = 1
    for i in range(1, n+1):
        print(res, "=", res, "+", pow(x,i))
        res = res + pow(x,i)
    print("\n")
    if res == 0:
        print(res+1)
    else:
        print(res)
elif choice == 14:
    x = -1
    w = 2
    n = int(input("Enter the value of n: "))
    i = 1
    while i != n:
        print(i, "X:", x, "=", x, "-", w)
        x = x - w
        print(i, "W:", x, "=", x, "+", w)
        w = x + w
        i = i + 1
    print("\n")
    print("Xn =", x, "and Wn =", w)
elif choice == 15:
    year = int(input("Please enter the year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print ("The year", year, "is a leap year.")
    else:
        print ("The year", year, "is not a leap year.")
elif choice == 16:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    delta = b*b - 4*a*c
    if b < 0 and c < 0:
        print("For " + str(a) + "x² " + str(b) + "x " + str(c) + ", Δ = " + str(delta))
    elif b < 0 and c > 0:
        print("For " + str(a)+ "x² " + str(b) + "x + " + str(c) + ", Δ = " + str(delta))
    elif b > 0 and c < 0:
        print("For " + str(a) + "x² + " + str(b) + "x " + str(c) + ", Δ = " + str(delta))
    else:
        print("For " + str(a) + "x² + " + str(b) + "x + " + str(c) + ", Δ = " + str(delta))
    if delta < 0:
        print("No real solution in R.")
    elif delta == 0:
        x0 = -b / 2*a
        print("There is one solution in R for this equation.\nx0 =", x0)
    else:
        print(math.sqrt(delta))
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("There are two solutions in R for this equation.\nx0 =", x1, "\nx1 =", x2)
elif choice == 17:
    op = str(input("Please chose an operation (+, /, * or -): "))
    a = int(input("What's the first number? "))
    b = int(input("What's the second number? "))
    if op == "+":
        print(str(a) + " + " + str(b) + " = " + str(a+b))
    elif op == "-":
        print(str(a) + " - " + str(b) + " = " + str(a-b))
    elif op == "*":
        print(str(a) + " * " + str(b) + " = " + str(a*b))
    elif op == "/":
        print(str(a) + " / " + str(b) + " = " + str(a/b))
    else:
        print("The operation symbol has not been recognized.")
else:
    print("Error on in the selection.")

