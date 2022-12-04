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
#Data = Test
Size = 3
GroupCounter = 1
for x in range(0, len(Data), Size):
    ElfBadgeGroup = [set(x) for x in Data[x:(x + Size)]]
    ElfBadgeGroupIdentifier = list(set.intersection(*ElfBadgeGroup))
    Total += PriorityMap[ElfBadgeGroupIdentifier[0]]
    print("Group {0}: {1} = {2}".format(GroupCounter, ElfBadgeGroupIdentifier[0], PriorityMap[ElfBadgeGroupIdentifier[0]]))
    GroupCounter += 1

print("\nTotal priority: ", Total)
