import os
import time
import heapq

MAP_NUMBER = 0
TABLES = []

with open(os.path.join("Maps", "data" + str(MAP_NUMBER) + ".txt"), "r") as map_input:
    for line in map_input:
        for ch in line:
            if ch.isalpha():
                heapq.heappush(TABLES, (0, ch))


class Customer:
    def __init__(self):
        self.name = ""
        self.time_eat = 0
        self.time_prep = 0
        self.time_t = 0
        self.foods = list()

    def order_food(self):
        print("----------------------------------------------------------------------------\n")
        self.name = input("Enter your name: ")

        try:
            t = int(input("Enter the number of food you want to order: "))
            for i in range(1, t + 1):
                self.foods.append(input("Food [" + str(i) + "] : "))

            self.time_eat, self.time_prep = int(input("Enter your eating time: ")), int(
                input("Enter the preparation time: "))
            self.time_t = self.time_eat + self.time_prep

        except ValueError:
            print("Oops!  That was no valid number. Let's back to the menu")
            os.system("cls")
            return

        table_to_eat = heapq.heappop(TABLES)
        print("Dear {name}: Please sit at table: {table}".format(name=self.name, table=table_to_eat[1]))
        heapq.heappush(TABLES, (self.time_t, table_to_eat))

        input("Press Enter to go back to menu")
        os.system("cls")


class Table:
    def __init__(self, name, time_passed, time_sit, time_t):
        self.name = name
        self.time_sit = time_sit
        self.time_t = time_t


if __name__ == '__main__':

    while True:
        print("\n-------------------- Welcome to Kharkhon Bashi Restaurant ---------------------\n")
        print("1.Order Food")
        print("2.Show Tables")

        try:
            selection = int(input("Please enter a number: "))
            if selection == 1:
                new_customer = Customer()
                new_customer.order_food()
            elif selection == 2:
                pass

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
