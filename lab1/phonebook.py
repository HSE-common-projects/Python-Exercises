from abonent import Abonent

def isAbonent(string):
    info_fields = string.split(';')
    return len(info_fields) > 3

def isName(string):
    return string.isalpha()

def isNumber(string):
    return (string[0]=='+' and string[2:].isdigit) or string.isdigit

def isDate(string):
    nums=string.split(".")
    if len(nums)!=3:
        return 0
    else:
        return nums[0].isdigit and nums[1].isdigit and nums[2].isdigit()

def remove7(number):
    if number[:2] == "+7":
        number = '8' + number[2:]
    return number

if __name__ == '__main__':
    with open("phonebook.txt") as book_file:
        lines=book_file.readlines()
        book=list()
        for line in lines:
            if isAbonent(line):
                book.append(Abonent(line))

        commands_list="This is the list of commands for the smart phonebook:"\
                      "!print ---> this commans prints all records in the phonebook" \
                      "!add ---> this command adds new record to the phonebook" \
                      "!del ---> this command deletes record" \
                      "!quit ---> this command exits the phonebook and saves changes"
        print("Smart phonebook greets you!")
        print(commands_list)
        while(True):
            command=input()

            if command=="!quit":
                rewrite_book=open("phonebook.txt", "w")
                i=1
                for el in book:
                    rewrite_book.write(el.forwrite())
                    i+=1
                break

            elif command=="!print":
                i = 1
                for el in book:
                    print("{}.".format(i), str(el))
                    i += 1
                continue

            elif command=="!add": #нужны проверки на корректность
                print("Input abonent's surname >>", end=" ")
                surname=input()
                print("Input abonent's name >>", end=" ")
                name=input()
                print("Input abonent's phone number >>", end=" ")
                p_number=input()
                birth_date=""
                print("Are you want to add Abonent's birth date? Input \"Y\" if you want or input anything else if no >>", end=" ")
                response=input()
                if response.strip() =="Y":
                    print("Input abonent's birth date >>", end=" ")
                    birth_date=input()
                new_ab=Abonent(surname+';'+name+';'+p_number+';'+birth_date)
                book.append(new_ab)
                print("New abonent was added succesfully")
                continue

            elif command=="!del":
                print("What way are you choose?\n input \"1\" ---> deletion by name+surname\n input \"2\" ---> deletion by the phone number")
                response=input()
                if response.strip()=='1':
                    print("Input abonent's surname >>", end=" ")
                    surname = input()
                    print("Input abonent's name >>", end=" ")
                    name = input()
                    flag=0
                    for el in book:
                        if el.name==name and el.surname==surname:
                            book.remove(el)
                            print("Abonent was deleted successfully")
                            flag=1
                            break
                    if flag==0:
                        print("I can not find this Abonent. Please, try again")
                elif response.strip()=='2':
                    print("Input abonent's phone number >>", end=" ")
                    p_number = input()
                    flag = 0
                    for el in book:
                        if el.phone_number == p_number:
                            book.remove(el)
                            print("Abonent was deleted successfully")
                            flag = 1
                            break
                    if flag == 0:
                        print("I can not find this Abonent. Please, try again")
                continue

            else:
                print("Unknown command. Please, repeat. Maybe you forgot \"!\"?")






