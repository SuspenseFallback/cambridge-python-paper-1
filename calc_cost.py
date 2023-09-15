import math


def calc_cost(weight):
    if weight <= 5:
        return 10
    else:
        extra = ((weight - 5) / 0.1) * 0.1
        num = math.floor((10 + extra) * 10) / 10

        return num
