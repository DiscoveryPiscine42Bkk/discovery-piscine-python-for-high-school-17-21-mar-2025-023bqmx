#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    input = sys.argv[1:]
    input.reverse()

    for string in input:
        print(string)