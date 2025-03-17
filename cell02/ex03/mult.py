f_number = int(input("Enter your first number : "))
s_number = int(input("Enter your second number : "))

multi = f_number * s_number

print(str(f_number) + " * " + str(s_number) + " =" ,multi)

if multi < 0 :
    print("Negative")
elif multi > 0 :
    print("Positive")
else:
    print("Zero")