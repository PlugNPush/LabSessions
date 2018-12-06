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

def palindrome(word):
    newword = word.lower()
    split = list(newword)
    l = len(split)/2
    a = 0
    b = len(split)-1

    while a <= l:
        if split[a] != split[b]:
            return False
        a += 1
        b -= 1
    return True

# print (palindrome("Ahoha"))

def sortlist(list):
    ARRAY = list.split("-")
    res = sorted(ARRAY, key=str.lower)
    return res

# print (sortlist("Eh-bah-comment-ça-va-toi-j'esprere-que-tu-vas-bien-au-moins-merci-a-bientot"))

def square(n,s,A):
    if n < s:
        AS = n*n
        A[n-1] = AS
        return square(n+1,s,A)
    return A

#print(square(1,30,[0] * 29))

def multiply(A, l, r):
    if l >= 0:
        r = A[l] * multiply(A, l-1, r)
    return r

# Array = [4,4,4,4]
# length = len(Array)-1
# print(multiply(Array, length, 1))

def sum(A, l, r):
    if l >= 0:
        r = A[l] + sum(A, l-1, r)
    return r

# Array = [4,4,4,4]
# length = len(Array)-1
# print(sum(Array, length, 0))

def occurence(A, l, t, s):
    if t <= l:
        if A[t] == s:
            return t
        else:
            return occurence(A, l, t+1, s)
    return -1

# Array = [4,34,7,6,2,65]
# length = len(Array)-1
# search = 6
# print(occurence(Array, length, 0, search))

def totaloccurence(A, l, t, s, o):
    if t <= l:
        if A[t] == s:
            return totaloccurence(A, l, t+1, s, o+1)
        else:
            return totaloccurence(A, l, t+1, s, o)
    return o

# Array = [4,34,7,6,2,65,8,5,6,8,3,6,2,7,2,6]
# length = len(Array)-1
# search = 6
# print(totaloccurence(Array, length, 0, search, 0))

def unique(A, l, t, NEWA, NEWl):
    if l >= t:
        x = 0
        add = True
        for x in range(0,NEWl):
            if A[t] == NEWA[x]:
                add = False
        if add == True:
            NEWA.append(A[t])
            NEWl += 1
        return unique(A, l, t+1, NEWA, NEWl)
    return NEWA


Array = [4,34,7,6,2,65,8,5,6,8,3,6,2,7,2,6]
length = len(Array)-1
print(unique(Array, length, 1, [Array[4]], 0))
