from time import sleep
from array import array
from random import randrange
import math
import sys
import time
choice = choice = int(input("Welcome to LabSession 2. Chose one option to start.\n1 - Repeated Messages\n2 - Average\n3 - 2000 - 3200\n4 - Array management\n5 - Useless operations (includes GCD)\n6 - Perfect number\n7 - Mystery number (game)\n"))
print("\n")
if choice == 1:
    message = str(input("What message do you want to display? : "))
    count = int(input("How many times? "))
    print("Get ready.")
    sys.stdout.flush()
    sleep(3)
    s = 0
    while s != count:
        print(message)
        s = s + 1
elif choice == 2:
    count = int(input("How many numbers will you calculate the average for? "))
    s = 1
    total = 0
    while s != count+1:
        total = total + int(input("Number " + str(s) + ": "))
        s = s + 1
    print("The average of all these numbers is : " + str(total/count))
elif choice == 3:
    s = 2000
    count = 3200
    checker = True
    while s != count and checker:
        if s % 7 == 0 and s % 5 != 0:
            print(s, end='')
            checker = False
        s = s + 1
    while s != count:
        if (s % 7 == 0 and s % 5 != 0):
            print(", " + str(s), end='')
        s = s + 1
elif choice == 4:
    n = int(input("How many values in the Array? "))
    print("Now type all the numbers.")
    c = 0
    Array = [0] * n
    while c < n:
        Array[c] = int(input("Number " + str(c+1) + ": "))
        c += 1
    search = int(input("What term do you want to search for? "))
    c = 0
    stop = False
    found = False
    while c < n and stop == False:
        if Array[c] == search:
            stop = True
            found = True
        c += 1
    if found == True:
        print("\nFound first ", search, " in Array position ", c-1)
    else:
        print("\nCould not find ", search, " in the Array.")
    c = 0
    count = 0
    while c < n:
        if Array[c] == search:
            count += 1
        c += 1
    print("Found ", search, " in Array ", count, " times.")
    c = 0
    stop = False
    while c < n-1 and stop == False:
        if Array[c] < Array[c+1]:
            c += 1
            ordered = True
        else:
            print("This Array is not ordered. Fixing this now.")
            ordered = False
            stop = True
    c = 0
    d = 0
    if ordered == False:
        Array.sort()
        print(Array)
        while c < n:
            print(Array[c])
            c += 1
    else:
        print("This Array is ordered. Great!")
elif choice == 5:
    chs = int(input("Please chose between:\n1 - Multiplication by addition\n2 - Division by substraction (includes GCD)\n3 - x^n by multiplication\n"))
    if chs == 1:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
        count = 0
        result = 0
        while count != b:
            result = result + a
            count += 1
        print("The result is of " + str(a) + "x" + str(b) + " by addition is: " + str(result))
    elif chs == 2:
        div0 = False
        result = 0
        ADV = False
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
        if a < b:
            print("Inverting first and second number.")
            a, b = b, a
        if b == 0:
            print("Division by zero not possible.")
            div0 = True
        while (a-b) >= 0 and div0 == False:
            c = a - b
            print(a, "-", b, "=", c)
            a = c
            result += 1
        print("DECIMAL: ")
        if c > 0:
            ADV = True
            a = b
            b = c
            c = a - b
            print(a, "-", b, "=", c)
        else:
            print("none")
        while c > 0 and div0 == False:
            ADV = True
            a = b
            b = c
            if a-b > 0:
                c = a - b
            else:
                c = b - a
            print(a, "-", b, "=", c)
        print("The result is", result)
        if ADV == True:
            print("This result has a decimal value.")
            print("The GCD of these two numbers is: " + str(b))
        else:
            print("This result doesn't have any decimal value.")
            print("The GCD of these two numbers is: " + str(b))
    elif chs == 3:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
        count = 0
        result = 1
        while count != b:
            result = result * a
            count += 1
        print("The result is of " + str(a) + "^" + str(b) + " by multiplication is: " + str(result))
    else:
        print("Error on in the selection.")
elif choice == 6:
    a = int(input("Please enter the number: "))
    i = 1
    sum = 0
    while i != a-1:
        if a%i == 0:
            sum += i
        i += 1
    if sum == a:
        print("This number is a perfect number.")
    else:
        print("This number is not a perfect number.")
elif choice == 7:
    print("Welcome. Before we start, we need a couple of information.\n")
    playername = str(input("What's your name? "))
    enableassistance = str(input("Okay " + playername + ", I got that. Now, do you want to enable the game assistance? (reply \"yes\" or \"no\", default answer is no.): "))
    if enableassistance == "yes" or enableassistance == "\"yes\"":
        assistance = True
        print("Great " + playername + ", Game assistance is enabled, you'll get some help from me.")
    else:
        assistance == False
        print("Okay " + playername + ", Game assistance is disabled, you won't have any help from me.")
    max = int(input("Okay, so now " + playername + " I need to know what is the maximal value I should take for you to guess. By default, 10.000 will be chosen. So, what's your choice? "))
    if max < 100:
        print("That's a too small value, it's not fun... I changed it to 100. Good luck!")
        max = 100
    else:
        print("Okay, we're set " + playername + ", I'm not going to take a value higher than " + str(max) + ". Good luck!")
    numbertoguess = randrange(max)
    givennumber = int(input("All right " + playername + ", things get serious now! Please give your first guess. You will be timed just after you hit the Enter key! "))
    count = 0
    t0 = time.time()
    while givennumber != numbertoguess:
        if givennumber > numbertoguess:
            if assistance == True:
                if givennumber - numbertoguess > 10000:
                    print("The number you gave is WAAAAAAAAY too high.")
                elif givennumber - numbertoguess > 1000:
                    print("The number you gave is way too high.")
                elif givennumber - numbertoguess > 100:
                    print("The number you gave is too high.")
                else:
                    print("The number you gave is too high, but not that far from the good one.")
            else:
                print("The number you gave is too high.")
        if givennumber < numbertoguess:
            if assistance == True:
                if numbertoguess - givennumber > 10000:
                    print("The number you gave is WAAAAAAAAY too low.")
                elif numbertoguess - givennumber > 1000:
                    print("The number you gave is way too low.")
                elif numbertoguess - givennumber > 100:
                    print("The number you gave is too low.")
                else:
                    print("The number you gave is too low, but not that far from the good one.")
            else:
                print("The number you gave is too low.")
        count += 1
        givennumber = int(input("Enter your guess: "))
    t1 = time.time()
    totaltime = t1-t0
    print("Congrats! You found it! The number was indeed " + str(numbertoguess) + "! Here are some statistics about your game:\nIt took you " + str(totaltime) + " seconds to find the number, and " + str(count) + " attempts.")
else:
    print("Error on in the selection.")
