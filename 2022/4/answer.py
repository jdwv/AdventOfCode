#!/usr/bin/env python3

import os
DirName = os.path.dirname(__file__)
FileName = os.path.join(DirName, 'input.txt')

with open(FileName, "r") as File:
    Data = [line.strip() for line in File]

Test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")
#Data = Test

Total = 0

for x in Data:
    Group1, Group2 = [ [int(i) for i in j.split('-')] for j in  x.split(',')]
    Group1Set = set([y for y in range(min(Group1), (max(Group1) + 1))])
    Group2Set = set([y for y in range(min(Group2), (max(Group2) + 1))])
    print("#########")
    print("Group 1", Group1, "Group 2", Group2)
    print(Group1Set, "and", Group2Set)

    if (not Group1Set.difference(Group2Set)) or (not Group2Set.difference(Group1Set)):
        print(">>>One set has difference of zero - fully contained in other set")
        Total += 1

print("\nTotal fully contained pairs: ", Total)

    