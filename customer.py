import os
import heapq

MAP_NUMBER = 6
TABLE_NAMES = list()
with open(os.path.join("Maps", "data" + str(MAP_NUMBER) + ".txt"), "r") as map_input:
    for line in map_input:
        for ch in line:
            if ch.isalpha():
                TABLE_NAMES.append(ch)

print(TABLE_NAMES)


class Customer:
    def __init__(self, name, time_eat, time_prep, time_t):
        self.name = name
        self.time_eat = time_eat
        self.time_prep = time_prep
        self.time_t = time_t


def order():
    print("----------------------------------------------------------------------------")
    print()
    name = input("Enter your name: ")

    food = list()

    t = int(input("Enter the number of food you want to order: "))

    for i in range(1, t + 1):
        food.append(input("Enter food number " + str(i) + " : "))

    time_eat, time_prep = input("inter your eating time: "), input("Enter the preparation time: ")

    customer = Customer(name, time_eat, time_prep, time_eat + time_prep)


def table():
    pass


class Table:
    pass


if __name__ == '__main__':
    print()
    print("--------------------Welcom to Kharkhon Bashi restaurant---------------------")
    print()
    print("----------------------------------------------------------------------------")
    print("1.Order Food")
    print("2.Show tables")

    if int(input()) == 1:
        order()
    else:
        table()
