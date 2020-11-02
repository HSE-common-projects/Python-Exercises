import itertools as itt
import random


def task3(letters):
    collection = list(itt.permutations(letters, len(letters)))
    without_duplicates = list()
    all_str = list()
    for el in collection:
        if el not in without_duplicates:
            without_duplicates.append(el)
            string = ""
            for letter in el:
                string += letter
            all_str.append(string)
    collection.clear()
    without_duplicates.clear()
    return all_str


def task2(letters, output_size, repetitions=False):
    collection = list(letters)
    result = ""
    N = len(collection) - 1
    for i in range(output_size):
        rand_number = random.randint(0, N)
        result += collection[rand_number]
        if not repetitions:
            collection.remove(collection[rand_number])
            N -= 1
    return result

lst=task3("aabsurd")
print(lst,len(lst), sep="\n")
print(task2("aabdfdsfds", 3))
