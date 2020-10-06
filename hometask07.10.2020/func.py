def task2(path):
    lst = os.listdir(path)
    for name in lst:
        if os.path.isfile(path + "\\" + name):
            yield path + "\\" + name
        else:
            for el in task2(path + "\\" + name):
                yield el


def fixed(number, digits):
    return f"{number:.{digits}f}"


def myRange(l, r, step=1.0):
    while (l < r):
        yield l
        l += step


def timeRange(hour=0, min=0, sec=0, step_hour=0, step_min=0, step_sec=1):
    while (hour < 24):
        if sec >= 60:
            min += sec // 60
            sec = sec % 60
        if min >= 60:
            hour += min // 60
            min = min % 60
        yield hour, min, sec
        hour += step_hour
        min += step_min
        sec += step_sec


def enum(lst):
    for i in range(0, len(lst)):
        yield i, lst[i]