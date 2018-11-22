choice = choice = int(input("Welcome. Chose one option to start.\n1 - Fill a list\n2 - Minimum value and average\n3 - search\n4 - number of occurence\n5 - insert value in sorted array\n6 - check if array is sorted\n7 - PENDING...\n"))
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
    
else:
    print("Error on in the selection.")

