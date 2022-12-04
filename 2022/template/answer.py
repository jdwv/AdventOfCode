#!/usr/bin/env python3

import os
DirName = os.path.dirname(__file__)
FileName = os.path.join(DirName, 'input.txt')
Testing = False

TestData = """1
2
3
4""".split("\n")

if Testing:
    Data = TestData    
else:
    with open(FileName, "r") as File:
        Data = [line.strip() for line in File]

print(Data)