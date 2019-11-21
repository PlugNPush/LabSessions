def pri():
    print("INIT OK !")

def cro(x, n):
    if x <= n:
        return cro(x+1, n)
    else:
        return x
        
    
