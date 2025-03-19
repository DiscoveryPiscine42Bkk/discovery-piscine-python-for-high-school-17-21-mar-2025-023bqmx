#!/usr/bin/env python3

import sys

if len(sys.argv) == 2 :
    para = sys.argv[1]
    userinput = input("What was the parameter? : ")

    if para == userinput:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")