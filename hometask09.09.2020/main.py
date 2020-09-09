import random

def task2(n):
    max_iter = 0
    count = 0
    for number in range(1, n + 1):
        while number != 1:
            if number % 2 == 0:
                number /= 2
                count += 1
            else:
                number = number * 3 + 1
                count += 1
        if count > max_iter:
            max_iter = count
        count = 0
    return max_iter


def task3Guessing(n):
    mystery_number = random.randint(0, n)
    print("I thought of a number. Let's try to guess\nInput a number\n>>>", end="")
    user_number = n + 1
    try_count = 0
    while True:
        user_number = int(input())
        try_count += 1
        if user_number == mystery_number:
            print("You are right! Congratulations!")
            print("It took you", try_count, "tries")
            break
        if user_number > mystery_number:
            print("You number is greater than mine", "\n", "Let's try again\n>>>", end="", sep="")
            continue
        if user_number < mystery_number:
            print("You number is less than mine", "\n", "Let's try again\n>>>", end="", sep="")
            continue

    return


def task3_1ReverseGuessing(n):
    left_border = 0
    right_border = n
    try_count = 0
    flag = 0
    while True:
        number = left_border + int((right_border - left_border) / 2)
        print("Your number is", number, '?')
        try_count += 1
        if flag == 0:
            print("If your number is less type 1")
            print("If my number is correct type 2")
            print("If your number is greater type 3")
            flag = 1
        print(">>>", end="")
        code = int(input())
        if code == 2:
            print("It took me", try_count, "tries")
            return
        elif code == 1:
            right_border = number
            continue
        elif code == 3:
            left_border = number
            continue


def task1TextAnalysis():
    f = open("D:\\repos\\Python-Exercices\\hometask09.09.2020\\Cold.txt", 'r', encoding='utf-8')
    word_collection = dict()
    buf = ""
    word_count = 0
    for line in f:
        i = 0
        while (i < len(line)):
            if line[i].isalpha():
                while (line[i].isalpha()):
                    buf += line[i]
                    i += 1
                buf = buf.lower()
                if buf in word_collection:
                    word_collection[buf] += 1
                else:
                    word_collection[buf] = 1
                word_count = word_count + 1
                buf = ""
            i += 1
    print("Text contain", word_count, "words")
    # print(word_collection)

    for i in range(1, 101):
        max_value = 0
        key_buf = ""
        for key in word_collection:
            if word_collection[key] >= max_value:
                max_value = word_collection[key]
                key_buf = key
        print(i, ">>>", key_buf, word_collection[key_buf])
        del word_collection[key_buf]


# TASKS
# print(task2(1000))
# task3Guessing(10)
# task3_1ReverseGuessing(100)
task1TextAnalysis()
