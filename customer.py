import os
import heapq
import datetime
import time

# file number
MAP_NUMBER = 6
# our heap which is a list of tuples (total time, table name) and number of them
tables = []
global number_of_tables
# situation of reservation {table name: list(Table)}
table_overview = {}

global foods


# class for table situation and its customers
class Table:
    # constructor
    def __init__(self, name="", time_sit=datetime.datetime.now(), time_t=0):
        # customer name of table
        self.name = name
        # time of sitting
        self.time_sit = time_sit
        # waiting time + eating time
        self.time_t = time_t

    # function to print table situation
    def __str__(self):
        string_ans = ""
        string_ans += f"\n---> Customer: {self.name}\n"
        string_ans += f"\n     Duration: {self.time_t} minutes\n"
        string_ans += f"""\n     Sitting Time: {self.time_sit.strftime("%A - %d %b %Y - %I:%M %p")}\n"""
        return string_ans


def start(food_data=None):
    # read our table names from file and add them to a heap queue
    if food_data is None:
        food_data = dict()

    global number_of_tables
    global foods
    number_of_tables, foods = 0, food_data

    with open(os.path.join("Maps", "data" + str(MAP_NUMBER) + ".txt"), "r") as map_input:
        for line in map_input:
            for ch in line:
                # find the alphabets
                if ch.isalpha():
                    # push table name and time to TABLES which is our heapq
                    heapq.heappush(tables, (0, ch))
                    # set the table reservation an empty list
                    table_overview[ch] = []
                    # add the number of tables
                    number_of_tables += 1


# class for adjectives of customers
class Customer:

    # constructor
    def __init__(self):
        self.name = ""
        self.time_eat = 0
        self.time_prep = 0
        self.time_t = 0

    # function for ordering food
    def order_food(self):
        print("\n----------------------------------------------------------------------------\n")

        # get name
        self.name = input("---> Enter your name: ")

        try:
            # get food
            print("Food name\tTime")
            for f, t in foods.items():
                print("{food}\t{times}".format(food=f, times=t))

            # t = int(input("\n---> Enter the number of food you want to order: "))
            self.time_eat, self.time_prep = int(input("\n---> Enter your eating time: ")), int(
                input("\n---> Enter the preparation time: "))
            # calculate total time
            self.time_t = self.time_eat + self.time_prep

        except ValueError:
            input("\nOops!  That was no valid number. Let's back to the menu")
            os.system("cls")
            return

        # check table and customers if anybody left delete it
        for ind_table in range(number_of_tables):
            # get a list of objets Table for each table
            table_data = table_overview[tables[ind_table][1]]
            to_delete = list()

            # for each Table object calculate the passed time and delete them of time has passed
            for t in range(len(table_data)):
                # time of sitting + time needed for preparation and eating < now
                if table_data[t].time_sit + datetime.timedelta(minutes=table_data[t].time_t) < datetime.datetime.now():
                    # total time of table reservation - total time of a lived customer
                    timed = tables[ind_table][0] - table_data[t].time_t
                    # set new time for the table
                    tables[ind_table] = (timed, tables[ind_table][1])
                    # append the Table object number which needs to be deleted to list
                    to_delete.append(t)
            # delete the free Table object
            for ind in to_delete:
                del table_data[ind]
        # arrange out heap again
        heapq.heapify(tables)

        # min time and name of the table
        table_min_to_eat, table_name_to_eat = heapq.heappop(tables)

        # if a table has customer
        if len(table_overview[table_name_to_eat]):
            # time sit of last customer + time pass after sitting time = final time (the table will be empty)
            final_time = table_overview[table_name_to_eat][-1].time_sit + datetime.timedelta(
                minutes=table_overview[table_name_to_eat][-1].time_t)

            # now time
            now_time = datetime.datetime.now()

            # calculate waiting time(for customer) = final time - now
            waiting_time = final_time - datetime.timedelta(
                now_time.day, 0, 0, 0, now_time.minute, now_time.hour)

            # print the waiting time and the table
            print("\n------> Dear {name}, you can sit at table \"{table}\" after {time} hours and {min} minutes.\n"
                  .format(name=self.name, table=table_name_to_eat, time=waiting_time.hour,
                          min=waiting_time.minute))

            # calculate time sit = now + time pass after waiting time
            time_sit = datetime.datetime.now() + datetime.timedelta(
                hours=waiting_time.hour, minutes=waiting_time.minute, seconds=waiting_time.second)

            # add Table object to dict
            table_overview[table_name_to_eat].append(Table(self.name, time_sit, self.time_t))

            # add Table object ro hash queue
            heapq.heappush(tables, (self.time_t + table_min_to_eat, table_name_to_eat))

        # there's an empty table
        else:
            # print the table
            print(
                "\n------> Dear {name}, you can sit at table \"{table}\"\n".format(name=self.name,
                                                                                   table=table_name_to_eat))
            # add Table object to dict
            table_overview[table_name_to_eat].append(Table(self.name, datetime.datetime.now(), self.time_t))

            # add Table object to hash queue
            heapq.heappush(tables, (self.time_t, table_name_to_eat))

        print("----------------------------------------------------------------------------------")
        input("\nPress Enter to go back to menu")
        os.system("cls")


def main():
    # start
    os.system("cls")
    print("Loading Restaurant Map... Please Wait")
    start_time = time.time()
    if not foods:
        start()

    print(f"File Loaded!\nTime = {time.time() - start_time}s")
    input("\nPress Enter to continue")

    while True:
        os.system("cls")
        print("\n-------------------- Welcome to Kharkhon Bashi Restaurant ---------------------\n")
        print("\n1. Order Food\n")
        print("\n2. Show Tables\n")
        print("\n3. Exit\n")

        try:
            selection = int(input("\nPlease enter a number: "))

            # order food and reserve table
            if selection == 1:
                new_customer = Customer()
                new_customer.order_food()

            elif selection == 2:
                print("\n----------------------------------------------------------------------------------")
                for k, v in table_overview.items():
                    print(f"\nTable {k}:")

                    for c in range(len(v)):
                        if not v[c].time_sit + datetime.timedelta(minutes=v[c].time_t) < datetime.datetime.now():
                            print(v[c])

                    print("\n----------------------------------------------------------------------------------")

                input("\nPress Enter to go back to menu")
                os.system("cls")

            elif selection == 3:
                print("GoodBye!")
                print("by: Adrina & Kian")
                exit(0)

        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")


if __name__ == "__main__":
    main()
