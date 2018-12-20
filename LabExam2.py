#Python
#Laboratory Exam 2 - Session 1 (1h30)



# 1. Create a function IsSorted(...) that checks whether an array of integers is sorted in the ascending order.


# 2. Create a function SearchInSorted(...) that searches a value in a sorted array (ascending order) of integers. It uses the previous function to check if the received array is sorted or not. If yes it search the value and returns its position, if any, or -1. Otherwise, it returns -2.

# Note : you should take advantage of the fact that the array is sorted (i.e. if you encounter a value in the array that is bigger than the researched value, then you stop the function and returns -1 : the value does not exist in the array).


# 3. Create a function DicoSearchInSorted(...) similar to the previous function but using dichotomy principle.

# 4. Write a main python program allowing to check the previous functions.


SArray = [1,3,5,7,8,41,54,75]
USArray = [1,3,5,7,8,41,54,75,4]

def IsSorted(a):
    l = len(a)
    status = True
    i = 0
    while i < l-1 and status == True:
        if a[i] > a[i+1]:
            status = False
        i += 1
    return status


print("Exercice 1, sorted Array: ", IsSorted(SArray))
print("Exercice 1, unsorted Array: ", IsSorted(USArray))

def SearchInSorted(a):
    if IsSorted(a) == False:
        return -2
    else:


print("Exercice 2, sorted Array: ", SearchInSorted(SArray))
print("Exercice 2, unsorted Array: ", SearchInSorted(USArray))
