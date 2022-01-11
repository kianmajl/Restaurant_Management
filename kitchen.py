import os
import graphlib

# {food name, its graph}
FOODS_RECIPES = {}
# list all foods
FOOD_MENU = []
# {all recipes, preparation time}
FOOD_PREP = {}


def initialize():
    graph = graphlib.TopologicalSorter()
    with open(os.path.join("Food Recipes", "TestDataKianAdrina.txt"), "r") as food_input:
        new_food = False
        for line in food_input:
            line = line.strip()

            if line == "New Food:":
                new_food = True
                continue

            if line == "End of instructions":
                # FOODS_RECIPES.append(graph)
                FOODS_RECIPES[FOOD_MENU[-1]] = graph
                del graph
                graph = graphlib.TopologicalSorter()
                continue

            if new_food:
                new_food = False
                FOOD_MENU.append(line)

            else:
                data, temp_food = line.split(), list()
                time_prep = 0

                for food in data[1:]:
                    if not food.isdigit():
                        graph.add(data[0], food)
                        temp_food.append(food)
                    else:
                        time_prep += int(food)

                for tp in temp_food:
                    time_prep += FOOD_PREP.get(tp, 0)

                FOOD_PREP[data[0]] = time_prep

    # for k, v in FOOD_PREP.items():
    #     print(k, v)
    #
    # for food_rep in FOODS_RECIPES:
    #     print(*food_rep.static_order())


if __name__ == "__main__":

    initialize()

    while True:
        os.system("cls")
        print("\n-------------------- Welcome to Kitchen of Kharkhon Bashi Restaurant ---------------------\n")
        print("\n1. Show Foods\n")
        print("\n2. Delete a Food\n")
        print("\n3. Show Food Recipes\n")
        print("\n4. Add a requirement to the food\n")
        print("\n5. Get the food with the most time needed\n")
        print("\n6. Get the food with the most requirements\n")

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
                    print(fdr, *FOODS_RECIPES[fdr].static_order())

                input("\nPress Enter to go back to menu")

            elif selection == 4:
                for foods in FOOD_MENU:
                    print(foods, FOOD_PREP[foods])

                food_name = input("Enter a food name: ")
                req = input("Enter a line of requirement").split()
                FOODS_RECIPES[food_name].add(req[0], req[1])
                print("Successfully added!")
                input("\nPress Enter to go back to menu")

            elif selection == 5:
                print(max(FOOD_PREP, key=lambda x: FOOD_PREP[x]))

                input("\nPress Enter to go back to menu")

            elif selection == 6:
                pass


        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")
