import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def ch(x,a,b):
    if x == "*":
        return mul(a,b)
    elif x == "-":
        return sub(a,b)
    elif x == "+":
        return add(a,b)
    elif x == "/":
        return div(a,b)
    else:
        return "ERR_SYM_DETECT_FAILED"
def calc():
    chs = str(input("Hello, please choose between *, /, + and - : "))
    a = int(input("Number a ? "))
    b = int(input("Number b ? "))
    print(ch(chs,a,b))

# calc()

def maxmin(nba,nbb,nbc):
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
    return minimum, maximum

# min, max = maxmin(1, 2, 3) # Then call either min or max as a variable

def factorial(n):
    if n <= 0:
        return 0
    else:
        result = n*(n-1)
        n = n-2
        while n > 0:
            result *= n
            n -= 1
        return result

# print(factorial(5))

def RANGE(x,a,b):
    if a > b:
        s = b
        b = a
        a = s
    if x >= a and x <= b:
        return True
    else:
        return False

# print (RANGE(74,12,650))

def prime(x):
    i = 2
    while i < math.sqrt(x):
        if (x%i == 0):
            return False
        i += 1
    return True

# print (prime(41))

def perfect(x):
    sum = 0
    i = x-1
    while i > 0:
        if (x%i == 0):
            sum += i
        i -= 1
    if sum == x:
        return True
    else:
        return False

# print(perfect(6))

def reverse(str):
    return str[::-1]

# print(reverse("GROUPE MINASTE"))

