import csv


def findtop(lst, criterion="richer"):
    quakes = lst.copy()
    if criterion == "richer":
        quakes.sort(key=lambda x: float(x[3]), reverse=True)
        return [(float(quakes[i][1]), float(quakes[i][2])) for i in range(10)]
    if criterion == "depth":
        quakes.sort(key=lambda x: float(x[0]), reverse=True)
        return [(float(quakes[i][1]), float(quakes[i][2])) for i in range(10)]


def task1():
    with open("quake.csv") as quake_file:
        reader = csv.reader(quake_file, delimiter=',')
        quakes = list()
        for row in reader:
            quakes.append(row)
        quakes.pop(0)
        # a
        cnt = 0
        for row in quakes:
            if float(row[3]) > 6.0:
                cnt += 1
        print(cnt)
        # b
        print("top 10 by Richer")
        print(*findtop(quakes, criterion="richer"))
        print("top 10 by Focal depth")
        print(*findtop(quakes, criterion="depth"))

        # c
        north_quakes = [quake for quake in quakes if float(quake[1]) > 0]
        print(len(north_quakes))
        print(*findtop(north_quakes, criterion="richer"))
        print(*findtop(north_quakes, criterion="depth"))

        south_quakes = [quake for quake in quakes if float(quake[1]) <= 0]
        print(len(south_quakes))
        print(*findtop(south_quakes, criterion="richer"))
        print(*findtop(south_quakes, criterion="depth"))

        east_quakes = [quake for quake in quakes if float(quake[2]) > 0]
        print(len(east_quakes))
        print(*findtop(east_quakes, criterion="richer"))
        print(*findtop(east_quakes, criterion="depth"))

        west_quakes = [quake for quake in quakes if float(quake[2]) <= 0]
        print(len(west_quakes))
        print(*findtop(west_quakes, criterion="richer"))
        print(*findtop(west_quakes, criterion="depth"))

        # d


def maxFeature(data, feature, max=True):
    for i in range(len(data[0])):
        if data[0][i] == feature:
            value = float(data[1][i])
            result_time = data[1][0] + " " + data[1][1]
            for j in range(2, len(data)):
                if data[j][i] != "-200":
                    if float(data[j][i]) > value and max:
                        value = float(data[j][i])
                        result_time = data[j][0] + " " + data[j][1]
                    elif float(data[j][i]) < value and not max:
                        value = float(data[j][i])
                        result_time = data[j][0] + " " + data[j][1]
            return result_time, value


def maxminAverageFeature(data, feature):
    i = 0
    for j in range(len(data[0])):
        if data[0][j] == feature:
            i = j
    max = -10000
    min = 10000
    max_day = ""
    min_day = ""
    average = 0
    cnt = 0
    cdata = data.copy()
    cdata.pop(0)
    pred_day = cdata[0][0]
    for line in cdata:
        if float(line[i]) != -200:
            if line[0] == pred_day:
                average += float(line[i])
                cnt += 1
            else:
                average = average / cnt
                if average > max:
                    max = average
                    max_day = line[0]
                if average < min:
                    min = average
                    min_day = line[0]
                cnt = 1
                average = float(line[i])
                pred_day = line[0]
    average = average / cnt
    if average > max:
        max_day = cdata[len(cdata) - 1][0]
        max = average
    if average < min:
        min_day = cdata[len(cdata) - 1][0]
        min = average
    return max_day, min_day, max, min


def locMinTime(day, fi):
    loc_mins = list()
    for i in range(3, len(day) - 3):
        flag = 1
        for j in range(i - 3, i):
            if (float(day[j][fi]) < float(day[j + 1][fi])) or float(day[j][fi]) == -200:
                flag = 0
        for j in range(i, i + 3):
            if (float(day[j][fi]) > float(day[j + 1][fi])) or float(day[j][fi]) == -200:
                flag = 0
        if flag == 1:
            loc_mins.append(day[i][1])
    return loc_mins


def findLocMin(data, feature):
    fi = 0  # feature index
    for j in range(len(data[0])):
        if data[0][j] == feature:
            fi = j
    cdata = data.copy()
    cdata.pop(0)
    day = list()
    all_loc_min = list()
    pred_day = cdata[0]
    for line in cdata:
        if line[0] == pred_day[0]:
            day.append(line)
        else:
            all_loc_min.extend(locMinTime(day, fi))
            day.clear()
            day.append(line)
            pred_day = line
    return all_loc_min


def findMostCommon(lst):
    result = ""
    most_repetitions = 0
    recycled = list()
    for el in lst:
        if el not in recycled:
            current_rep = lst.count(el)
            if current_rep > most_repetitions:
                most_repetitions = current_rep
                result = el
            recycled.append(el)
    return result


def task2():
    with open("AirQualityUCI.csv") as air_file:
        reader = csv.reader(air_file, delimiter=';')
        data = list()
        for row in reader:
            data.append(row)
        # a
        print(*maxFeature(data, "AH", max=False))

        # b
        print(*maxminAverageFeature(data, "C6H6(GT)"))

        # c
        all_loc_min = findLocMin(data, "AH")
        # print(*all_loc_min)
        print(findMostCommon(all_loc_min))


if __name__ == '__main__':
    # task1()
    task2()
