import shutil

cols, rows = shutil.get_terminal_size()

def print_center(s):
    print(s.center(cols))

def pri():
    print("INIT OK !")




def cro(n, x = 0):
    print(x)
    if x < n:
        cro(n, x+1)
        
    
def decro(n):
    print(n)
    if n > 0:
        decro(n-1)


def tricro(n, x = 0):
    print("*" * x)
    if x < n:
        tricro(n, x+1)

def tridecro(n):
    print("*" * n)
    if n > 0:
        tridecro(n-1)

def etricro(n, x = 0):
    text = ""
    for i in range(0, x):
        if i < x-1:
            text = text + "* - "
        else:
            text = text + "*\n"
    print_center(text)
    if x < n:
        etricro(n, x+1)

def etridecro(n):
    text = ""
    for i in range(0, n):
        if i < n-1:
            text = text + "* - "
        else:
            text = text + "*\n"
    print_center(text)
    if n > 0:
        etridecro(n-1)


def reverse(x):
    if x == "":
        return ""
    else:
        return x[len(x)-1] + reverse(x[:len(x)-1])

def copy(x, n = 0):
    if len(x) <= n:
        return ""
    else:
        return x[n] + copy(x, n+1)

def самогласника(рећ, ж = 0, тотал_самогласника = 0):

    сплит = list(рећ)
    дугаћ = len(сплит)
    
    if ж >= дугаћ:
        return тотал_самогласника
    else:
        if (сплит[ж] == "а") or (сплит[ж] == "А") or (сплит[ж] == "е") or (сплит[ж] == "Е") or (сплит[ж] == "у") or (сплит[ж] == "У") or (сплит[ж] == "и") or (сплит[ж] == "И") or (сплит[ж] == "о") or (сплит[ж] == "О") or (сплит[ж] == "a") or (сплит[ж] == "A") or (сплит[ж] == "e") or (сплит[ж] == "E") or (сплит[ж] == "u") or (сплит[ж] == "u") or (сплит[ж] == "i") or (сплит[ж] == "i") or (сплит[ж] == "o") or (сплит[ж] == "O"):
            тотал_самогласника += 1
        ж += 1
        return самогласника(рећ, ж, тотал_самогласника)








def cyrtolat(x, n = 0):
    if len(x) <= n:
        return ""
    else:
        item = ""
        if x[n] == "а":
            item = "a"
        elif x[n] == "б":
            item = "b"
        elif x[n] == "в":
            item = "v"
        elif x[n] == "г":
            item = "g"
        elif x[n] == "д":
            item = "d"
        elif x[n] == "е":
            item = "e"
        elif x[n] == "к":
            item = "k"
        elif x[n] == "л":
            item = "l"
        elif x[n] == "љ":
            item = "lj"
        elif x[n] == "м":
            item = "m"
        elif x[n] == "н":
            item = "n"
        elif x[n] == "њ":
            item = "nj"
        elif x[n] == "и":
            item = "i"
        elif x[n] == "о":
            item = "o"
        elif x[n] == "п":
            item = "p"
        elif x[n] == "р":
            item = "r"
        elif x[n] == "с":
            item = "s"
        elif x[n] == "т":
            item = "t"
        elif x[n] == "у":
            item = "u"
        elif x[n] == "ш":
            item = "š"
        elif x[n] == "ћ":
            item = "č"
        elif x[n] == "ж":
            item = "ž"
        elif x[n] == "ч":
            item = "ć"
        elif x[n] == "ц":
            item = "c"
        elif x[n] == "џ":
            item = "đ"
        
        if item == "":
            return x[n] + cyrtolat(x, n+1)
        else:
            return item + cyrtolat(x, n+1)
