import os
import graphlib

GRAPH = graphlib.TopologicalSorter()
FOODS_RECIPES = []
FOOD_MENU = []
FOOD_PREP = {}

with open(os.path.join("Food Recipes", "TestData.txt"), "r") as food_input:
    new_food = False
    for line in food_input:
        line = line.strip()

        if line == "New Food:":
            new_food = True
            continue

        if line == "End of instructions":
            FOODS_RECIPES.append(GRAPH)
            del GRAPH
            GRAPH = graphlib.TopologicalSorter()
            continue

        if new_food:
            new_food = False
            FOOD_MENU.append(line)

        else:
            data, temp_food = line.split(), list()
            time_prep = 0

            for food in data[1:]:
                if not food.isdigit():
                    GRAPH.add(data[0], food)
                    temp_food.append(food)
                else:
                    time_prep += int(food)

            for tp in temp_food:
                time_prep += FOOD_PREP.get(tp, 0)

            FOOD_PREP[data[0]] = time_prep

for k, v in FOOD_PREP.items():
    print(k, v)

for food_rep in FOODS_RECIPES:
    print(*food_rep.static_order())
