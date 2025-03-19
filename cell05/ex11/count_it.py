#!/usr/bin/env python3

import sys

arg01 = sys.argv[1:]

if not arg01:
    print("none")
else:
    print(f"Parameter : {len(arg01)} ")
    
    for arg02 in arg01:
        print(f"{arg02} : {len(arg02)}")