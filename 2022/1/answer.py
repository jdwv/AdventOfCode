#!/usr/bin/env python3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename, "r") as file:
    ElfCalorieInput = file.read()

# Strip leading/trailing newlines
ElfCalorieInput = ElfCalorieInput.strip('\n') 

# Empty array 
ElfCalories = []

# Add cleaned up str arrays to new array
[ ElfCalories.append(x.split('\n')) for x in ElfCalorieInput.split('\n\n')] 

# Empty dict to store total with number
ElfTotals = {}

# Convert and sum string arrays into dict
for x in range(len(ElfCalories)):
    ElfName = "Elf " + str(x + 1)
    TotalElfCalories = sum([int(e) for e in ElfCalories[x]])
    ElfTotals[ElfName] = TotalElfCalories

# Return max value from dict
print("Result - {0} has {1} calories".format(max(ElfTotals, key=ElfTotals.get), max(ElfTotals.values())))
