import os
import heapq
import datetime

MAP_NUMBER = 0
TABLES, NUMBER_OF_TABLES = [], 0
TABLE_OVERVIEW = {}


class Table:
    def __init__(self, name="", time_sit=datetime.datetime.now(), time_t=0):
        self.name = name
        self.time_sit = time_sit
        self.time_t = time_t

    def __str__(self):
        string_ans = ""
        string_ans += f"\n---> Customer: {self.name}\n"
        string_ans += f"\n     Duration: {self.time_t} minutes\n"
        string_ans += f"""\n     Sitting Time: {self.time_sit.strftime("%A - %d %b %Y - %I:%M %p")}\n"""
        return string_ans


with open(os.path.join("Maps", "data" + str(MAP_NUMBER) + ".txt"), "r") as map_input:
    for line in map_input:
        for ch in line:
            if ch.isalpha():
                heapq.heappush(TABLES, (0, ch))
                TABLE_OVERVIEW[ch] = []
                NUMBER_OF_TABLES += 1


class Customer:
    def __init__(self):
        self.name = ""
        self.time_eat = 0
        self.time_prep = 0
        self.time_t = 0
        self.foods = list()

    def order_food(self):
        print("\n----------------------------------------------------------------------------\n")
        self.name = input("---> Enter your name: ")

        try:
            t = int(input("\n---> Enter the number of food you want to order: "))
            for i in range(1, t + 1):
                self.foods.append(input("\n-> Food [" + str(i) + "] : "))

            self.time_eat, self.time_prep = int(input("\n---> Enter your eating time: ")), int(
                input("\n---> Enter the preparation time: "))
            self.time_t = self.time_eat + self.time_prep

        except ValueError:
            input("\nOops!  That was no valid number. Let's back to the menu")
            os.system("cls")
            return

        for ind_table in range(NUMBER_OF_TABLES):
            table_data = TABLE_OVERVIEW[TABLES[ind_table][1]]
            to_delete = list()
            for t in range(len(table_data)):
                if table_data[t].time_sit + datetime.timedelta(minutes=table_data[t].time_t) < datetime.datetime.now():
                    time = TABLES[ind_table][0] - table_data[t].time_t
                    TABLES[ind_table] = (time, TABLES[ind_table][1])
                    to_delete.append(t)

            for ind in to_delete:
                del table_data[ind]

            heapq.heapify(TABLES)

        table_min_to_eat, table_name_to_eat = heapq.heappop(TABLES)

        if len(TABLE_OVERVIEW[table_name_to_eat]):

            final_time = TABLE_OVERVIEW[table_name_to_eat][-1].time_sit + datetime.timedelta(
                minutes=TABLE_OVERVIEW[table_name_to_eat][-1].time_t)

            now_time = datetime.datetime.now()

            waiting_time = final_time - datetime.timedelta(
                now_time.day, 0, 0, 0, now_time.minute, now_time.hour)

            print("\n------> Dear {name}, you can sit at table \"{table}\" after {time} hours and {min} minutes.\n"
                  .format(name=self.name, table=table_name_to_eat, time=waiting_time.hour,
                          min=waiting_time.minute))

            time_sit = datetime.datetime.now() + datetime.timedelta(
                hours=waiting_time.hour, minutes=waiting_time.minute, seconds=waiting_time.second)

            TABLE_OVERVIEW[table_name_to_eat].append(Table(self.name, time_sit, self.time_t))
            heapq.heappush(TABLES, (self.time_t + table_min_to_eat, table_name_to_eat))

        else:
            print(
                "\n------> Dear {name}: Please sit at table: {table}\n".format(name=self.name, table=table_name_to_eat))
            TABLE_OVERVIEW[table_name_to_eat].append(Table(self.name, datetime.datetime.now(), self.time_t))
            heapq.heappush(TABLES, (self.time_t, table_name_to_eat))

        print("----------------------------------------------------------------------------------")
        input("\nPress Enter to go back to menu")
        os.system("cls")


if __name__ == '__main__':

    while True:
        os.system("cls")
        print("\n-------------------- Welcome to Kharkhon Bashi Restaurant ---------------------\n")
        print("\n1. Order Food\n")
        print("\n2. Show Tables\n")

        try:
            selection = int(input("\nPlease enter a number: "))

            if selection == 1:
                new_customer = Customer()
                new_customer.order_food()

            elif selection == 2:
                print("\n----------------------------------------------------------------------------------")
                for k, v in TABLE_OVERVIEW.items():
                    print(f"\nTable {k}:")

                    for c in range(len(v)):
                        if not v[c].time_sit + datetime.timedelta(minutes=v[c].time_t) < datetime.datetime.now():
                            print(v[c])

                    print("\n----------------------------------------------------------------------------------")

                input("\nPress Enter to go back to menu")
                os.system("cls")

        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")
