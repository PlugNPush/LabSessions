from collections import deque
choice = choice = int(input("Welcome. Chose one option to start.\n1 - Fill a list\n2 - Minimum value and average\n3 - search\n4 - number of occurence\n5 - insert value in sorted array\n6 - check if array is sorted\n7 - Shift a list\n8 - longest 0\n9 - same values same position\n10 - same values on all array\n11 - eliminate doubles\n12 - PENDING...\n"))
print("\n")
if choice == 1:
    Array = []
    stop = False
    i = 0
    while stop == False:
        request = input("Array number " + str(i) + " (enter \"stop\" to stop): ")
        if str(request) == "stop" or str(request) == "Stop":
            stop = True
        else:
            Array.append(int(request))
            i += 1
    c = 0
    while c != i:
        print(Array[c])
        c += 1
elif choice == 2:
    Array = []
    stop = False
    i = 0
    while stop == False:
        request = input("Array number " + str(i) + " (enter \"stop\" to stop): ")
        if str(request) == "stop" or str(request) == "Stop":
            stop = True
        else:
            Array.append(int(request))
            i += 1
    min = Array[0]
    c = 0
    total = 0
    while c != i:
        if min > Array[c]:
            min = Array[c]
        total += Array[c]
        c += 1
    average = total/i
    print("The minimum value is ", min, " and the average is ", average)
elif choice == 3 or choice == 4 or choice == 6:
    print("Please refer to LabSession2 - choice 4.")
elif choice == 5:
    Array = []
    stop = False
    i = 0
    while stop == False:
        request = input("Array number " + str(i) + " (enter \"stop\" to stop): ")
        if str(request) == "stop" or str(request) == "Stop":
            stop = True
        else:
            Array.append(int(request))
            i += 1
    Array.sort()
    insert = int(input("Which value do you want to save in the array? "))
    Array.append(insert)
    Array.sort()
    c = 0
    while c != i:
        print(Array[c])
        c += 1
elif choice == 7:
    Array = deque(["D", "E", "C", "A", "L", "A", "G", "E"])
    Array.rotate(-1)
    c = 0
    while c != 8:
        print(Array[c])
        c += 1
elif choice == 8:
    Array = [0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0]
    i = 19
    definitivei = 0
    definitivel = 0
    c = 0
    estop = False
    while c != 19 and estop == False:
        if Array[c] == 0:
            print("INIT FOR C : ", c)
            midc = c
            midl = 0
            while Array[midc] == 0 and estop == False:
                if midc+1 != 19:
                    midc += 1
                    midl += 1
                else:
                    print("EMERGENCY BREAK ENABLED.")
                    estop = True
            if midl > definitivel:
                definitivel = midl
                definitivei = c
            c = midc
        else:
            c += 1
    print("The i where you find the longest serie of 0 is : ", definitivei, "and is ", definitivel, " \"0\" long.")
elif choice == 9 or choice == 10:
    print("please refer to the MASTERMIND project.")
elif choice == 11:
    Array = []
    stop = False
    i = 0
    while stop == False:
        request = input("Array number " + str(i) + " (enter \"stop\" to stop): ")
        if str(request) == "stop" or str(request) == "Stop":
            stop = True
        else:
            Array.append(int(request))
            i += 1
        c = 0
#       TBC.

# IMPORTED FROM LABSESSION 2
# 4 - Array management
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
    
    
    
else:
    print("Error on in the selection.")

