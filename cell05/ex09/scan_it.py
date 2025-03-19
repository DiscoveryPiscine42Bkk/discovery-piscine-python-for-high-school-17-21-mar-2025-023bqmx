#!/usr/bin/env python3

import sys
import re

if len(sys.argv) !=3:
    print("none")
else:
    a = sys.argv[1]
    sent = sys.argv[2]
    
    sum = re.findall(a,sent)
    print(len(sum))