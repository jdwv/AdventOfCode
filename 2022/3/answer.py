#!/usr/bin/env python3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename, "r") as file:
    Data = [line.strip() for line in file]


# Generate Priority Map
# - a:a = 1:26
# - A:Z = 27:52
PriorityMap = {}
priority = 1
for x in range(ord('a'), ord('z') + 1):
    PriorityMap[chr(x)] = priority
    priority += 1
for x in range(ord('A'), ord('Z') + 1):
    PriorityMap[chr(x)] = priority
    priority += 1

Test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

Total = 0

for t in Data:
    MidPoint = int((len(t) / 2))
    FirstCompartment = set(t[0:MidPoint])
    SecondCompartment = set(t[MidPoint:])
    CommonCharacter = list(FirstCompartment.intersection(SecondCompartment))
    print("Compartment String: ", "".join(FirstCompartment), " | ", "".join(SecondCompartment))
    print("Common Char: {0} = {1}".format(CommonCharacter[0], PriorityMap[CommonCharacter[0]]))
    Total += PriorityMap[CommonCharacter[0]]

print("\nTotal priority: ", Total)
