import datetime


def isDataCorrect(day, month, year):
    try:
        datetime.date(int(year), int(month), int(day))
        return True
    except:
        return False


def isData(string):
    string.strip()
    arr = string.split('.')
    if len(arr) != 3:
        return False
    if not (arr[0].isdigit() and arr[1].isdigit() and arr[2].isdigit()):
        return False
    return isDataCorrect(arr[0], arr[1], arr[2])


def remove7(number):
    if number[:2] == "+7":
        number = '8' + number[2:]
    return number


def isName(string):
    for char in string:
        if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or char == ' ' or char.isdigit():
            continue
        else:
            return False
    return True


def isNumber(string):
    number = remove7(string)
    return number.isdigit() and len(number) == 11


def isNameAndSurname(surname, name):
    if not isName(surname):
        print("Incorrect surname!")
        return 0
    elif not isName(name):
        print("Incorrect name!")
        return 0
    return 1


def decoratorMinusFriendly(func, string):
    if string == '-':
        return True
    else:
        return func(string)


def comp(el, field):
    return el == field or field == "-"


def search(book, surname="-", name="-", pnumb="-", date="-"):
    result = list()
    for el in book:
        if comp(el.name, name) and comp(el.surname, surname) and comp(el.phone_number, pnumb) and comp(el.birth_date,
                                                                                                       date):
            result.append(el)
    return result


def printBook(arr):
    for el in arr:
        print(str(el))


def editing(book, i, surname="-", name="-", pnumb="-", date="-"):
    if surname != "-":
        book[i].surname = surname
    if name != "-":
        book[i].name = name
    if pnumb != "-":
        book[i].phone_number = pnumb
    if date != "-":
        book[i].birth_date = date


def ageComparison(book, criterion, N):
    flag = 0
    for el in book:
        if not el.age() == -1:
            if (el.age() > N and criterion == '>') or (el.age() < N and criterion == '<') or (
                    el.age() == N and criterion == '='):
                print(str(el))
                flag = 1
    if flag == 0:
        print("I didn't find anything(((")


def isInTimeInterval(delta, birth_date):
    now = datetime.datetime.today()
    date = birth_date.split('.')
    top_border = now + datetime.timedelta(days=delta)
    if top_border.year > now.year and int(date[1]) == 1:
        birth = datetime.datetime(year=top_border.year, month=int(date[1]), day=int(date[0]))
    else:
        birth = datetime.datetime(year=now.year, month=int(date[1]), day=int(date[0]))
    return now < birth < top_border
