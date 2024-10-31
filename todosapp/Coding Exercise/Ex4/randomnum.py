import random

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

random_number = random.randint(lower, upper)
print(random_number)