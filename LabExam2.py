# Python
# Laboratory Exam 2 - Session 1 (1h30)



# 1. Create a function IsSorted(...) that checks whether an array of integers is sorted in the ascending order.
# DONE

# 2. Create a function SearchInSorted(...) that searches a value in a sorted array (ascending order) of integers. It uses the previous function to check if the received array is sorted or not. If yes it search the value and returns its position, if any, or -1. Otherwise, it returns -2.

# Note : you should take advantage of the fact that the array is sorted (i.e. if you encounter a value in the array that is bigger than the researched value, then you stop the function and returns -1 : the value does not exist in the array).
# DONE

# 3. Create a function DicoSearchInSorted(...) similar to the previous function but using dichotomy principle.
# DONE

# 4. Write a main python program allowing to check the previous functions.
# IN PROGRESS...

# --------------------------------------------------


# TEST Variables Aera

SArray = [1,3,5,7,8,41,54,75]
USArray = [1,3,5,7,8,41,54,75,4]

searchFor = 41
SearchForNotExisting = 12

# End of TEST Variables Aera


# --------------------------------------------------

# Exercice 1
def IsSorted(a):
    l = len(a)
    status = True
    i = 0
    while i < l-1 and status == True:
        if a[i] > a[i+1]:
            status = False
        i += 1
    return status

# Expecting True, GOT True TEST OK
# print("Exercice 1, sorted Array: ", IsSorted(SArray))

# Expecting False, GOT False TEST OK
# print("Exercice 1, unsorted Array: ", IsSorted(USArray), "\n")

# Exercice 2
def SearchInSorted(a,s):
    if IsSorted(a) == False:
        return -2
    else:
        l = len(a)
        i = 0
        while i < l-1:
            if a[i] > s:
                return -1
            if a[i] == s:
                return i
            i += 1
        return -1

# Expecting 5, GOT 5 TEST OK
# print("Exercice 2, sorted Array: ", SearchInSorted(SArray, searchFor))

# Expecting -2, GOT -2 TEST OK
# print("Exercice 2, unsorted Array: ", SearchInSorted(USArray, searchFor))

# Expecting -1, GOT -1 TEST OK
# print("Exercice 2, sorted Array + not existing value: ", SearchInSorted(SArray, SearchForNotExisting), "\n")



# Exercice 3
def DicoSearchInSorted(a,s):
    if IsSorted(a) == False:
        return -2
    else:
        l = len(a)
        i = 0
        if s < a[int(l/2)]:
            if s < a[int(l/4)]:
                while i < l/4:
                    if a[i] > s:
                        return -1
                    if a[i] == s:
                        return i
                    i += 1
            if s > a[int(l/4)]:
                i = int(l/4)
                while i < l/2:
                    if a[i] > s:
                        return -1
                    if a[i] == s:
                        return i
                    i += 1
        if s > a[int(l/2)]:
            i = int(l/2)
            if s < a[int((1/4)*3)]:
                while i < l/4*3:
                    if a[i] > s:
                        return -1
                    if a[i] == s:
                        return i
                    i += 1
            if s > a[int((1/4)*3)]:
                i = int((1/4)*3)
                while i < l-1:
                    if a[i] > s:
                        return -1
                    if a[i] == s:
                        return i
                    i += 1
        return -1


# Expecting 5, GOT 5 TEST OK
# print("Exercice 3, sorted Array: ", DicoSearchInSorted(SArray, searchFor))

# Expecting -2, GOT -2 TEST OK
# print("Exercice 3, unsorted Array: ", DicoSearchInSorted(USArray, searchFor))

# Expecting -1, GOT -1 TEST OK
# print("Exercice 3, sorted Array + not existing value: ", DicoSearchInSorted(SArray, SearchForNotExisting), "\n")



# Exercice 4
def main():
    choice = int(input("Welcome! Please select your choice:\n1 - Check if an Array is sorted\n2 - Search for a value in a sorted Array\n3 - Search for a value in a sorted Array using dichotomy principle\nChoice: "))
    stop = False
    Array = []
    i = 1
    while stop == False:
        insert = input("Value number " + str(i) + " (enter value or \"stop\" to finish): ")
        if str(insert) == "stop" or str(insert) == "Stop" or str(insert) == "STOP" or str(insert) == "ok" or str(insert) == "Ok" or str(insert) == "STOP" or str(insert) == "cancel" or str(insert) == "Cancel" or str(insert) == "CANCEL" or str(insert) == "finish" or str(insert) == "Finish" or str(insert) == "FINISH":
            stop = True
        else:
            Array.append(int(insert))
        i += 1

    if choice == 1:
        if IsSorted(Array) == True:
            print("The provided Array is sorted!")
        else:
            print("The provided Array is not sorted.")

    elif choice == 2 or choice == 3:
        search = int(input("What value are you looking for? "))
        if choice == 2:
            res = SearchInSorted(Array, search)
        if choice == 3:
            res = DicoSearchInSorted(Array, search)
        if res == -2:
            print("The Array provided is not sorted!")
        elif res == -1:
            print("The value you're looking for seems not to be in this Array.")
        else:
            print("The value ", search, " was found in position ", res, ".")
    else:
        print("There were an error in the selection\n\n")
        main()

# Start the execution of the program
main()
