#!/usr/bin/env python3

import os
DirName = os.path.dirname(__file__)
FileName = os.path.join(DirName, 'input.txt')

with open(FileName, "r") as File:
    Data = [line.strip() for line in File]

Test = """1
2
3
4""".split("\n")