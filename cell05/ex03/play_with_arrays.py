#!/usr/bin/env python3

origin = [2, 8, 9, 48, 8, 22, -12, 2]
new = [i+2 for i in origin]

sum = {i for i in new if i >5}

print(origin)
print(sum)