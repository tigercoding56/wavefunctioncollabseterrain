import random


def randomly(start , end):
    temp = list(range(start,end))
    random.shuffle(temp)
    return temp