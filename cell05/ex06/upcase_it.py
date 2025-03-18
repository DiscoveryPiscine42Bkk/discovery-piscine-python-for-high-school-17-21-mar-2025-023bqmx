#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    uppercase_string = input_string.upper()
    print(uppercase_string)