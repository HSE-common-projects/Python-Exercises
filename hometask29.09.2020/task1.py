def evalNumber(a):
    return a


def countElements(arr):
    cnt = 0
    for it in arr:
        cnt += 1
    return cnt


def sumElements(arr):
    summ = 0
    for it in arr:
        summ += it
    return summ


def numberNulls(arr):
    cnt = 0
    for it in arr:
        if it == 0:
            cnt += 1
    return cnt


def strLen(string):
    return len(string)


def evalStr(string):
    return string


def findMaxOrMin(criterion, *args,  max_or_min=True):
    result = args[0]
    if max_or_min == False:
        for item in args:
            if criterion(item) < criterion(result):
                result = item
    else:
        for item in args:
            if criterion(item) > criterion(result):
                result = item
    return result
