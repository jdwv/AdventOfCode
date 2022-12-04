#!/usr/bin/env python3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename, "r") as file:
    input = file.read()