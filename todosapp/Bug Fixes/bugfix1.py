try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

except ValueError:
    print(f'{name} is not in the list')


#Second method with if_else

waiting_list = ["john", "marry"]
name = input("Enter name: ")

# Check if the name is in the waiting list
if name in waiting_list:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
else:
    exit(f"{name} is not in the waiting list.")
