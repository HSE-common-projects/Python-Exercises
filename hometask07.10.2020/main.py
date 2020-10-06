import os
from func import task2, fixed, myRange, timeRange, enum


# C:\Users\User\Desktop\УЧЕБА\2 курс\IAD\files_for_fun
# C:\Users\User\Desktop\УЧЕБА\2 курс\IAD\files_for_fun_2

class Fold:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.list_f = os.listdir(folder_path)
        for el in self.list_f:
            if not (el.find('.txt')):
                self.list_f.remove(el)
        self.all_strings = list()
        for name in self.list_f:
            f = open(folder_path + "\\" + name, 'r', encoding='utf-8')
            if len(f.read()) > 140:
                f.seek(0)
                self.all_strings += f.readlines()
            f.close()
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.all_strings):
            raise StopIteration
        else:
            str = self.all_strings[self.index]
            self.index += 1
            if str[len(str) - 1] == '\n':
                str = str[:len(str) - 1]
            return str


if __name__ == '__main__':
    # TASK 1 and 2

    # path = input()
    # my_fold=Fold(path)
    # for line in my_fold:
    #     print(line)
    # for el in task2(path):
    #     print(el)

    # TASK 3ab
    for i in myRange(2.1, 100.3, 5.2):
        print(fixed(i, 2), end=" ")
    print("\n")
    for h, m, s in timeRange(2, 10, 0, 0, 15, 20):
        print(h, m, s, sep=":", end="   ")
    print("\n")

    # TASK 4
    for item in enum([1, 3232, 4343, 6545, 343]):
        print(item, end=" ")
