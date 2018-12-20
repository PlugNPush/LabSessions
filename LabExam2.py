#Python
#Laboratory Exam 2 - Session 1 (1h30)



# 1. Create a function IsSorted(...) that checks whether an array of integers is sorted in the ascending order.


# 2. Create a function SearchInSorted(...) that searches a value in a sorted array (ascending order) of integers. It uses the previous function to check if the received array is sorted or not. If yes it search the value and returns its position, if any, or -1. Otherwise, it returns -2.

# Note : you should take advantage of the fact that the array is sorted (i.e. if you encounter a value in the array that is bigger than the researched value, then you stop the function and returns -1 : the value does not exist in the array).


# 3. Create a function DicoSearchInSorted(...) similar to the previous function but using dichotomy principle.

# 4. Write a main python program allowing to check the previous functions.




# Variable Aera

SArray = [1,3,5,7,8,41,54,75]
USArray = [1,3,5,7,8,41,54,75,4]

searchFor = 41
SearchForNotExisting = 12

# End of Variable Aera

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

# Expecting True
print("Exercice 1, sorted Array: ", IsSorted(SArray))
# Expecting False
print("Exercice 1, unsorted Array: ", IsSorted(USArray), "\n")

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

# Expecting 5
print("Exercice 2, sorted Array: ", SearchInSorted(SArray, searchFor))
# Expecting -2
print("Exercice 2, unsorted Array: ", SearchInSorted(USArray, searchFor))
# Expecting -1
print("Exercice 2, sorted Array + not existing value: ", SearchInSorted(SArray, SearchForNotExisting), "\n")

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


# Expecting 5
print("Exercice 3, sorted Array: ", DicoSearchInSorted(SArray, searchFor))
# Expecting -2
print("Exercice 3, unsorted Array: ", DicoSearchInSorted(USArray, searchFor))
# Expecting -1
print("Exercice 3, sorted Array + not existing value: ", DicoSearchInSorted(SArray, SearchForNotExisting), "\n")



# Exercice 4
def main():
    return 0
