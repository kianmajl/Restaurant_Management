import os
import heapq
import datetime

MAP_NUMBER = 0
TABLES = []
TABLE_OVERVIEW = {}


class Table:
    def __init__(self, name, time_sit, time_t, is_empty):
        self.name = name
        self.time_sit = time_sit
        self.time_t = time_t
        self.is_empty = is_empty

    def __str__(self):
        string_ans = ""
        if not self.is_empty:
            string_ans += f"---> Customer: {self.name}\n"
            string_ans += f"""     Sitting Time: {self.time_sit.strftime("%A - %d %b %Y - %I:%M %p")}\n"""
            string_ans += f"     Duration: {self.time_t} minutes\n"
        else:
            string_ans = "EMPTY!"

        return string_ans


with open(os.path.join("Maps", "data" + str(MAP_NUMBER) + ".txt"), "r") as map_input:
    for line in map_input:
        for ch in line:
            if ch.isalpha():
                heapq.heappush(TABLES, (0, ch))
                TABLE_OVERVIEW[ch] = Table("EMPTY!", 0, 0, True)


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

        table_to_eat = heapq.heappop(TABLES)[1]

        if not TABLE_OVERVIEW[table_to_eat].is_empty:

            final_time = TABLE_OVERVIEW[table_to_eat].time_sit + datetime.timedelta(
                minutes=TABLE_OVERVIEW[table_to_eat].time_t)

            now_time = datetime.datetime.now()

            waiting_time = final_time - datetime.timedelta(
                now_time.day, now_time.second, now_time.microsecond, 0, now_time.minute, now_time.hour)

            print("Dear {name} you can sit at table {table} after {time} hours and {min} minutes."
                  .format(name=self.name, table=table_to_eat, time=waiting_time.hour,
                          min=waiting_time.minute))

            TABLE_OVERVIEW[table_to_eat].time_sit = datetime.datetime.now() + datetime.timedelta(
                hours=waiting_time.hour, minutes=waiting_time.minute, seconds=waiting_time.second)

            heapq.heappush(TABLES, (self.time_t + int(waiting_time.hour * 60) + waiting_time.minute, table_to_eat))

        else:
            print("Dear {name}: Please sit at table: {table}".format(name=self.name, table=table_to_eat))
            TABLE_OVERVIEW[table_to_eat].time_sit = datetime.datetime.now()
            heapq.heappush(TABLES, (self.time_t, table_to_eat))

        TABLE_OVERVIEW[table_to_eat].name = self.name
        TABLE_OVERVIEW[table_to_eat].time_t = self.time_t
        TABLE_OVERVIEW[table_to_eat].is_empty = False

        input("Press Enter to go back to menu")
        os.system("cls")


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
                for k, v in TABLE_OVERVIEW.items():
                    print(f"Table {k}:")
                    print(v)

                input("Press Enter to go back to menu")
                os.system("cls")

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
