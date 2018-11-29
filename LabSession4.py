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

def uplowcase(str):
    AER = list(str)
    length = len(AER)
    low = 0
    up = 0
    i = 0
    while i < length:
        if (AER[i] == " ") or (AER[i] == "\n") or (AER[i] == ".") or (AER[i] == "?") or (AER[i] == "!"):
            a = 0
        
        elif AER[i].isupper():
            up += 1
        
        elif AER[i].islower():
            low += 1
    
        else:
            print("ERROR.")
        i += 1
    return low,up

# low, up = uplowcase("Добро Дошли на Груп Минаст !")
# print ("lowercase : ", low, " and UPPERCASE: ", up)


# This part is just for fun, you only can use it if you enter some cyrillic content.
# It has been entirely developed in cyrillic.

def воел(РЕЋ):
    
    СПЛИТ = list(РЕЋ)
    дугаћ = len(СПЛИТ)
    ТОТАЛ_ВОЕЛ = 0
    ж = 0
    while ж < дугаћ:
        if (СПЛИТ[ж] == "а") or (СПЛИТ[ж] == "А") or (СПЛИТ[ж] == "е") or (СПЛИТ[ж] == "Е") or (СПЛИТ[ж] == "у") or (СПЛИТ[ж] == "У") or (СПЛИТ[ж] == "и") or (СПЛИТ[ж] == "И") or (СПЛИТ[ж] == "о") or (СПЛИТ[ж] == "О"):
            ТОТАЛ_ВОЕЛ += 1
        ж += 1
    print("Има", ТОТАЛ_ВОЕЛ, "воел у то што си дао.")
    return ТОТАЛ_ВОЕЛ

def истивоел(РЕЋ1, РЕЋ2):
    print("Он зна само српски! This function works only for cyrillic, because WHY NOT? 😂\n\n")
    if воел(РЕЋ1) == воел(РЕЋ2):
        return True
    else:
        return False

# print("Са ово што си дао је: ", истивоел("Дали знаш само шта радиш бре! живиш у франсуска!", "Дали знаш само шта радиш бре! живиш у франсуском!"))

