# TD PYTHON SESSION 2
#
# EXO 1 = 1
# EXO 2 = 2
# EXO 3 = 3
# EXO 4 = 4
# EXO 5, 6, 7, 11 = 5
# EXO 8 = 6
# EXO 9 = 7 et 8
# EXO 10 = 9 et 10
# EXO 12 = 11
# EXO SM = 12 et 13
# EXO NM = 14 et 15
#
# EXO DECIMAL A L'INFINI EN CONSTRUCTION = 20


from time import sleep
from array import array
from random import randrange
import math
import sys
import time
choice = choice = int(input("Welcome to LabSession 2. Chose one option to start.\n1 - Repeated Messages\n2 - Average\n3 - Live minimum\n4 - 2000 - 3200\n5 - Useless operations (includes *, /, x^n, GCD)\n6 - Sum for i=1\n7 - Pair number\n8 - 1000 pair numbers\n9 - Perfect numbers\n10 - 1000 perfect numbers\n11 - Factorial\n12 - Un\n13 - Wn and Xn\n14 - Mystery number v1\n15 - Mystery number v1.1 with 10x restriction\n"))
print("\n")
if choice == 1:
    message = str(input("What message do you want to display? : "))
    count = int(input("How many times? "))
    print("Get ready.")
    sys.stdout.flush()
    sleep(3)
    s = 0
    while s < count:
        print(message)
        s += 1
elif choice == 2:
    count = int(input("How many numbers will you calculate the average for? "))
    s = 1
    total = 0
    while s != count+1:
        total += int(input("Number " + str(s) + ": "))
        s = s + 1
    print("The average of all these numbers is : " + str(total/count))

elif choice == 3:
    stor = int(input("How many numbers to compare ? "))
    s = 0
    minimum = int(input("Enter number 1: "))
    while s < stor-1:
        tempinput = int(input("Enter number " + str(s+2) + ": "))
        if tempinput < minimum:
            minimum = tempinput
        s += 1
    print("The minimum is ", minimum)
    
elif choice == 4:
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
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))
    result = 0
    tempresult = 1
    for i in range(1, n+1):
        for r in range(1, i+1):
            tempresult *= x
        result += tempresult
        tempresult = 1
    print("The result is: ", result)
    
elif choice == 7:
    x = int(input("Enter x: "))
    if (x % 2 == 0):
        print("The number is pair.")
    else:
        print("The number is not pair.")
        
elif choice == 8:
    for x in range(0, 1001):
        if (x % 2 == 0):
            print("The number " + str(x) + " is pair.")
        
    
elif choice == 9:
    a = int(input("Please enter the number: "))
    if a <= 2:
        print("This number is not a perfect number.")
    else:
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

elif choice == 10:
    for a in range(2, 1001):
        i = 1
        sum = 0
        while i != a-1:
            if a%i == 0:
                sum += i
            i += 1
        if sum == a:
            print("The number " + str(a) + " is a perfect number.")
        
elif choice == 11:
    n = int(input("Enter n: "))
    nbak = n
    if n < 0:
        print("Impossible.")
    elif n == 0:
        print("0! = 1")
    else:
        result = n*(n-1)
        n = n-2
        while n > 0:
            result *= n
            n -= 1
        print(str(nbak) + "! = " + str(result))
    
elif choice == 12:
    u = 4.5
    n = int(input("Enter the value of n: "))
    i = 1
    print("0) U =", u)
    while i <= n:
        print(str(i) + ") U = 2*", u, "-3")
        u = (2*u)-3
        i += 1
    print("Un =", u)
    
    
elif choice == 13:
    x = -1
    w = 2
    n = int(input("Enter the value of n: "))
    i = 1
    print("X0 =", x, "and W0 =", w)
    while i <= n:
        print(i, "X:", x, "=", x, "-", w)
        x = x - w
        print(i, "W:", x, "=", x, "+", w)
        w = x + w
        i = i + 1
    print("\n")
    print("Xn =", x, "and Wn =", w)


elif choice == 14:
    print("Welcome. Before we start, we need a couple of information.\n")
    playername = str(input("What's your name? "))
    enableassistance = str(input("Okay " + playername + ", I got that. Now, do you want to enable the game assistance? (reply \"yes\" or \"no\", default answer is no.): "))
    if enableassistance == "yes" or enableassistance == "\"yes\"":
        assistance = True
        print("Great " + playername + ", Game assistance is enabled, you'll get some help from me.")
    else:
        assistance = False
        print("Okay " + playername + ", Game assistance is disabled, you won't have any help from me.")
    max = int(input("Okay, so now " + playername + " I need to know what is the maximal value I should take for you to guess. By default, 10.000 will be chosen. So, what's your choice? "))
    if max < 100:
        print("That's a too small value, it's not fun... I changed it to 100. Good luck!")
        max = 100
    else:
        print("Okay, we're set " + playername + ", I'm not going to take a value higher than " + str(max) + ". Good luck!")
    numbertoguess = randrange(max)
    givennumber = int(input("All right " + playername + ", things get serious now! Please give your first guess. You will be timed just after you hit the Enter key! "))
    count = 1
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
    
elif choice == 15:
    print("Welcome. Before we start, we need a couple of information.\n")
    playername = str(input("What's your name? "))
    enableassistance = str(input("Okay " + playername + ", I got that. Now, do you want to enable the game assistance? (reply \"yes\" or \"no\", default answer is no.): "))
    if enableassistance == "yes" or enableassistance == "\"yes\"":
        assistance = True
        print("Great " + playername + ", Game assistance is enabled, you'll get some help from me.")
    else:
        assistance = False
        print("Okay " + playername + ", Game assistance is disabled, you won't have any help from me.")
    attemptlimit = input("Should I restrict your attempts to 10? ")
    if attemptlimit == "yes" or attemptlimit == "\"yes\"":
        attemptlimit = True
        print("All right, attempt limit is now Enabled!")
    else:
        attemptlimit = False
        print("Okay, no attempt limit for this one.")
    max = int(input("Okay, so now " + playername + " I need to know what is the maximal value I should take for you to guess. By default, 10.000 will be chosen. So, what's your choice? "))
    if max < 100:
        print("That's a too small value, it's not fun... I changed it to 100. Good luck!")
        max = 100
    else:
        print("Okay, we're set " + playername + ", I'm not going to take a value higher than " + str(max) + ". Good luck!")
    numbertoguess = randrange(max)
    givennumber = int(input("All right " + playername + ", things get serious now! Please give your first guess. You will be timed just after you hit the Enter key! "))
    if givennumber == numbertoguess:
        didWon = True
    count = 1
    t0 = time.time()
    mustStop = False
    didWon = False
    while givennumber != numbertoguess and mustStop == False and didWon == False:
        if attemptlimit and count >= 9:
            mustStop = True
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
        elif givennumber < numbertoguess:
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
        if givennumber == numbertoguess:
            didWon = True
    t1 = time.time()
    totaltime = t1-t0
    if didWon == True:
        print("Congrats! You found it! The number was indeed " + str(numbertoguess) + "! Here are some statistics about your game:\nIt took you " + str(totaltime) + " seconds to find the number, and " + str(count) + " attempts.")
    else:
        print("Oh no! You did not succeed to find the number " + str(numbertoguess) + " in time. You'll do better next time!")
        
if choice == 20:
    print("EXPERIMENTAL ZONE")
    p = 803
    q = 619
    b = 803//619
    exb = 803/619
    print("p = " + str(p) + ", q = " + str(q) + ", b = " + str(b) + ", expecting: " + str(exb))
    stopvalue = 100
    i = 0
    print(str(b) + ",", end='')
    while i < stopvalue:
        res = 10 * (p%q)/q
        print(int(res), end='')
        res = res * 10 - int(res)
        i += 1

else:
    print("Error on in the selection.")

print("\n\n")
