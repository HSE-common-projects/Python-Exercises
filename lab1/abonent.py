import datetime


def removeLast(string, char):
    if string != "":
        if string[-1] == char:
            return string[:-1]
    return string


class Abonent:
    surname = ""
    name = ""
    phone_number = ""
    birth_date = ""

    def setname(self, name):
        self.name = name.capitalize()

    def setsurname(self, surname):
        self.surname = surname.capitalize()

    def setphonenumber(self, number):
        if number[:2] == "+7":
            number = '8' + number[2:]
        self.phone_number = number

    def setbirthdate(self, date):
        self.birth_date = removeLast(date, '\n')

    def __init__(self, string):
        string.strip()
        info_fields = string.split(';')
        self.setsurname(info_fields[0])
        self.setname(info_fields[1])
        self.setphonenumber(info_fields[2])
        self.setbirthdate(info_fields[3])


    def __str__(self):
        return "{} {} {} {}".format(self.surname, self.name, self.birth_date, self.phone_number,)

    def forwrite(self):
        return "{};{};{};{}\n".format(self.surname, self.name, self.phone_number, self.birth_date)

    def age(self):
        if self.birth_date == "":
            return -1
        now = datetime.datetime.today()
        date = self.birth_date.split('.')
        abonent_age = now.year - int(date[2])
        if int(date[1]) > now.month:
            abonent_age -= 1
        elif int(date[1]) == now.month and int(date[0]) > now.day:
            abonent_age -= 1
        return abonent_age
