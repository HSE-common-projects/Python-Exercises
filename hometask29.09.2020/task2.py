def allSimpleNumbers(n):
    lst = []
    for i in range(2, n + 1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

def NOD(a,b):
    while a!=b:
        if a<b:
            b=b-a
        else:
            a=a-b
    return a

def allDenominators(x):
    lst=[]
    for numb in range(1,int(x/2)):
        if x%numb==0:
            lst.append(numb)
    return lst

# THIRD TASK
def convert(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, to_base) + alphabet[n % to_base]