from task1 import findMaxOrMin, evalNumber, countElements, sumElements, strLen, evalStr, numberNulls
from task2 import NOD, allSimpleNumbers, allDenominators, convert

# FIRST TASK
tup_ls = ([1, 90], [1, 2, 4], [0, 687, 7], [0, 0])
tup_str = ("abfgdsfdg", "adffd", "dfsdfuyuyuyuyuyisd", "zzzzzzzzzzzzzzzz")
tup_double = (2.6, 4.8, 765.665)
print(" ")
print(findMaxOrMin(strLen, max_or_min=False, *tup_str))
print(findMaxOrMin(evalStr, *tup_str))
print(findMaxOrMin(countElements, max_or_min=False, *tup_ls))
print(findMaxOrMin(numberNulls, *tup_ls))
print(findMaxOrMin(evalNumber, *tup_double))

print(" ")
# SECOND TASK

print(allSimpleNumbers(10))
print(NOD(2400, 400))
print(allDenominators(1000))

# THIRD TASK

print(convert(167,16,10))
