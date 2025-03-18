array01 =  [2, 8, 9, 48, 8, 22, -12, 2]
array02 = [i+2  for i in array01]
# sum_array = [i for i in array02 if i>=10]
sum_array = list(filter(lambda x: x >= 10, array02))

print(array01)
print(sum_array)