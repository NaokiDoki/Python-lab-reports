# Write a program to find the Compound interest

p = float(input("Enter principle: "))
t = float(input("Enter Time in years: "))
r = float(input("Enter rate: "))

CI = (p * (1 + r/100)**t) - p

print(f'the compound interest is {CI:.2f}')
