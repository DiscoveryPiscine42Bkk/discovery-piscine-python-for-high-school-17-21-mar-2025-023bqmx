#!/usr/bin/env python3
print("Give me the first number: ")
num1 = float(input())
print("Give me the second number: ")
num2 = float(input())
print("Thank You!")
try:
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 / num2}") 
    print(f"{num1} * {num2} = {num1 * num2}") 

except ZeroDivisionError:
    print(f"{num1} / {num2} = Undefined")

    print(f"{num1} x {num2} = {num1 * num2}")