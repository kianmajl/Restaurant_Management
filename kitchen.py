import os
import time
import graphlib
from collections import defaultdict
import copy

# {food name, its graph(dictionary:name to requirement)}
FOODS_RECIPES = {}
# list all foods
FOOD_MENU = []
# {all recipes, preparation time}
FOOD_PREP = {}


def initialize():
    graph = defaultdict(set)
    with open(os.path.join("Food Recipes", "TestDataKianAdrina.txt"), "r") as food_input:
        new_food = False
        for line in food_input:
            line = line.strip()

            if line == "New Food:":
                new_food = True
                continue

            if line == "End of instructions":
                FOODS_RECIPES[FOOD_MENU[-1]] = copy.deepcopy(graph)
                graph.clear()
                continue

            if new_food:
                new_food = False
                FOOD_MENU.append(line)

            else:
                data, temp_food = line.split(), list()
                time_prep = 0

                for food in data[1:]:
                    if not food.isdigit():
                        graph[data[0]].add(food)
                        temp_food.append(food)
                    else:
                        time_prep += int(food)

                for tp in temp_food:
                    time_prep += FOOD_PREP.get(tp, 0)

                FOOD_PREP[data[0]] = time_prep


if __name__ == "__main__":

    os.system("cls")
    print("Initializing... Please Wait")
    start_time = time.time()
    initialize()

    main_food_prep = dict(filter(lambda l: l[0] in FOOD_MENU, FOOD_PREP.items()))
    main_food_rec = dict(filter(lambda l: l[0] in FOOD_MENU, FOODS_RECIPES.items()))

    print(f"File Loaded!\nTime = {time.time() - start_time}s")
    input("\nPress Enter to continue")

    while True:
        os.system("cls")
        print("\n-------------------- Welcome to Kitchen of Kharkhon Bashi Restaurant ---------------------\n")
        print("\n1. Show Foods\n")
        print("\n2. Delete a Food\n")
        print("\n3. Show Food Recipes\n")
        print("\n4. Add a requirement to the food\n")
        print("\n5. Get the food with the most time needed\n")
        print("\n6. Get the food with the least time needed\n")
        print("\n7. Get the food with the most requirements\n")

        print("\n-------------------------------------------------------------------------------------------\n")

        try:
            selection = int(input("\nPlease enter a number: "))

            if selection == 1:
                for foods in FOOD_MENU:
                    print(foods, FOOD_PREP[foods])

                input("\nPress Enter to go back to menu")

            elif selection == 2:
                pass

            elif selection == 3:
                for fdr in FOOD_MENU:
                    try:
                        print(fdr, *graphlib.TopologicalSorter(FOODS_RECIPES[fdr]).static_order())
                    except graphlib.CycleError as gce:
                        print("Cycle detected!", gce)

                input("\nPress Enter to go back to menu")

            elif selection == 4:
                for foods in FOOD_MENU:
                    print(foods, FOOD_PREP[foods])

                food_name = input("Enter a food name: ")
                req = input("Enter a line of requirement: ").split()
                FOODS_RECIPES[food_name][req[0]].add(req[1])
                print("Successfully added!")
                input("\nPress Enter to go back to menu")

            elif selection == 5:
                maximum = max(main_food_prep, key=main_food_prep.get)
                print(maximum, main_food_prep[maximum])
                input("\nPress Enter to go back to menu")

            elif selection == 6:
                minimum = min(main_food_prep, key=main_food_prep.get)
                print(minimum, main_food_prep[minimum])
                input("\nPress Enter to go back to menu")

            elif selection == 7:

                maximum_rec_count, maximum_rec_names = 0, []

                for k, v in main_food_rec.items():
                    len_v = len(tuple(graphlib.TopologicalSorter(v).static_order()))

                    if len_v > maximum_rec_count:
                        maximum_rec_names.clear()
                        maximum_rec_names.append(k)
                        maximum_rec_count = len_v

                    elif len_v == maximum_rec_count:
                        maximum_rec_names.append(k)

                for name in maximum_rec_names:
                    print(name)
                    print(*graphlib.TopologicalSorter(FOODS_RECIPES[name]).static_order())

                input("\nPress Enter to go back to menu")

        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")
