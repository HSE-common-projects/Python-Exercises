from abonent import Abonent
from functions import isData, isName, isNumber, search, printBook, editing, isDataCorrect, ageComparison, isInTimeInterval
from functions import isNameAndSurname, decoratorMinusFriendly

def age(book):
    surname = input("Input abonent's surname >>")
    name = input("Input abonent's name >>")
    if not isNameAndSurname(surname,name):
        return
    result = search(book, surname=surname, name=name)
    if len(result) == 0:
        print("I can not find this Abonent. Please, try again")
        return
    if result[0].age() == -1:
        print("Age is not setted")
    else:
        print(result[0].age())


def find(book):
    print(
        "Hello! You will be promted to fill in user information. Input \"-\", if you don't want to specify field for search")
    surname = input("Input abonent's surname >>")
    name = input("Input abonent's name >>")
    p_number = input("Input abonent's phone number >>")
    birth_date = input("Input abonent's birth date >>")
    result = search(book, surname=surname, name=name, pnumb=p_number, date=birth_date)
    print("I found...")
    if len(result)==0:
        print("Nothing(((")
    else:
        printBook(result)


def add(book):
    surname = input("Input abonent's surname >>")
    name = input("Input abonent's name >>")
    if not isNameAndSurname(surname,name):
        return
    p_number = input("Input abonent's phone number >>")
    if not isNumber(p_number):
        print("Incorrect number!")
        return
    birth_date = ""
    response = input(
        "Are you want to add Abonent's birth date? Input \"Y\" if you want or input anything else if no >>")
    if response.strip() == "Y":
        birth_date = input("Input abonent's birth date >>")
        if not isData(birth_date):
            print("Incorrect date!")
            return
    ab = search(book, surname=surname, name=name)
    if len(ab) > 0:
        print("I found Abonent with same name and surname. What should I do? Input the number")
        response = input(
            "\"1\"---> delete old record and add new record\n\"2\"---> change name and surname of new record\n\"3\"---> adort addition")
        if response == '1':
            book.remove(ab[0])
            book.append(Abonent(surname + ';' + name + ';' + p_number + ';' + birth_date))
            print("Success")
        elif response == '2':
            surname = input("Input new abonent's surname >>")
            name = input("Input new abonent's name >>")
            book.append(Abonent(surname + ';' + name + ';' + p_number + ';' + birth_date))
            print("Success")
        elif response == '3':
            print("Addition aborted")
            return
        else:
            print("Incorrect number!")
            return
    else:
        book.append(Abonent(surname + ';' + name + ';' + p_number + ';' + birth_date))
        print("New abonent was added succesfully")


def delete(book):
    response = input("What way are you choose?\n input \"1\" ---> deletion by name+surname\n input \"2\" ---> deletion by the phone number\n>>>")
    if response.strip() == '1':
        surname = input("Input abonent's surname >>")
        name = input("Input abonent's name >>")
        if not isNameAndSurname(surname, name):
            return
        ab_arr = search(book, surname=surname, name=name)
        if len(ab_arr) == 0:
            print("I can not find this Abonent. Please, try again")
            return
        book.remove(ab_arr[0])
        print("Abonent was deleted successfully")
    elif response.strip() == '2':
        p_number = input("Input abonent's phone number >>")
        if not isNumber(p_number):
            print("Incorrect number!")
            return
        ab_arr = search(book, pnumb=p_number)
        if len(ab_arr) == 0:
            print("I can not find this Abonent. Please, try again")
            return
        elif len(ab_arr) == 1:
            book.remove(ab_arr[0])
            print("Abonent was deleted successfully")
            return
        else:
            print(
                "I found several Abonents. Which one of them are you want to delete? Specify the numbers (start from 1)(splitting by space)")
            printBook(ab_arr)
            response = input()
            response.strip()
            response = response.split(' ')
            N = len(ab_arr)
            for i in range(len(response)):
                if not response[i].isdigit():
                    print("I don't understand(((((")
                    return
                response[i] = int(response[i])
            for index in response:
                if index <= N:
                    book.remove(ab_arr[index - 1])
                    print("Abonent was deleted successfully")
    else:
        print("I don't understand(((((")


def edit(book):
    surname = input("Input abonent's surname >>")
    name = input("Input abonent's name >>")
    result = search(book, surname=surname, name=name)
    if len(result) == 0:
        print("I can not find this Abonent. Please, try again")
        return
    index = 0
    for i in range(len(book)):
        if book[i] == result[0]:
            index = i
    print("Hello! You will be promted to edit user information. Input \"-\", if you don't want to edit field")
    surname = input("Input abonent's surname >>")
    if not decoratorMinusFriendly(isName,surname):
        print("Incorrect surname!")
        return
    name = input("Input abonent's name >>")
    if not decoratorMinusFriendly(isName,name):
        print("Incorrect name!")
        return
    p_number = input("Input abonent's phone number >>")
    if not decoratorMinusFriendly(isNumber,p_number):
        print("Incorrect phone number!")
        return
    birth_date = input("Input abonent's birth date >>")
    if not decoratorMinusFriendly(isData,birth_date):
        print("Incorrect date!")
        return
    editing(book, index, surname=surname, name=name, pnumb=p_number, date=birth_date)
    print("Editing was successfull")


def birth(book):
    day = input("Input day of abonent's birth>>")
    if not day.isdigit():
        print("Incorrect day!")
        return
    else:
        day=int(day)
    month = input("Input month of abonent's birth>>")
    if not month.isdigit():
        print("Incorrect month!")
        return
    else:
        month=int(month)
    if not isDataCorrect(day, month, 2000):
        print("Incorrect date!")
        return
    flag = 0
    for el in book:
        if not el.age() == -1:
            arr = el.birth_date.split('.')
            if int(arr[0]) == day and int(arr[1]) == month:
                print(str(el))
                flag = 1
    if flag == 0:
        print("I didn't find anything(((")


def agelme(book):
    N = input("Input age>>")
    if not N.isdigit():
        print("Incorrect age!")
        return
    criterion = input("Input criterion for ages comparison (\">\", \"<\" or \"=\")>>")

    if criterion == '=' or criterion == '<' or criterion == '>':
        ageComparison(book, criterion, int(N))
    else:
        print("Incorrect criterion!")


def birthinm(book):
    flag = 0
    for el in book:
        if not el.age() == -1:
            if isInTimeInterval(30,el.birth_date):
                print(str(el))
                flag = 1
    if flag == 0:
        print("No birthdays in next 30 days")


def quit(book):
    rewrite_book = open("phonebook.txt", "w")
    i = 1
    for el in book:
        rewrite_book.write(el.forwrite())
        i += 1
    rewrite_book.close()
    print("Bye!")


def printWithNumbers(book):
    i = 1
    for el in book:
        print("{}.".format(i), str(el))
        i += 1

if __name__ == '__main__':
    with open("phonebook.txt") as book_file:
        lines = book_file.readlines()
        book = list()
        for line in lines:
            book.append(Abonent(line))

        commands_list = ["This is the list of commands for the smart phonebook:\n",
                         "!print ---> this commans prints all records in the phonebook\n",
                         "!add ---> this command adds new record to the phonebook\n",
                         "!del ---> this command deletes record\n",
                         "!find ---> \n",
                         "!edit ---> \n",
                         "!age ---> \n",
                         "!birth --->\n",
                         "!agelme ---> \n",
                         "!birthinm ---> \n",
                         "!quit ---> this command exits the phonebook and saves changes\n"]
        print("Smart phonebook greets you!")
        print(*commands_list)
        while (True):
            command = input()

            if command == "!quit":
                quit(book)
                break
            elif command == "!print":
                printWithNumbers(book)
            elif command == "!add":
                add(book)
            elif command == "!del":
                delete(book)
            elif command == "!find":
                find(book)
            elif command == "!age":
                age(book)
            elif command == "!edit":
                edit(book)
            elif command == "!birth":
                birth(book)
            elif command == "!agelme":
                agelme(book)
            elif command=="!birthinm":
                birthinm(book)
            else:
                print("Unknown command. Please, repeat. Maybe you forgot \"!\"?")

