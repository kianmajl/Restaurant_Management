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
