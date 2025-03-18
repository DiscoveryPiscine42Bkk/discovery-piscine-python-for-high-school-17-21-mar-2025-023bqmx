#!/usr/bin/env python3

def play_with_arrays(arr):

    unique_elements = set(arr)
    
    unique_list = list(unique_elements)
    
    return unique_list

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result = play_with_arrays(original_array)
print(result)