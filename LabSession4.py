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

calc()

