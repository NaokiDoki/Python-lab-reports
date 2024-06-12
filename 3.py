# Write a program to find the simple interest using user input

p = float(input("Enter principle: "))
t = float(input("Enter Time in years: "))
r = float(input("Enter rate: "))

SI = (p*t*r)/100

print(f'the simple interest is {SI}')
