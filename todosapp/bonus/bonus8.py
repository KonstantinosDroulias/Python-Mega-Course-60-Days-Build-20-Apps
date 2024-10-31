date = input("Enter today's date: ")
mood = input("How was your mood from 1-10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f'../Journal/{date}.txt', 'w') as file:
    file.write('Mood rate: ' + mood + 2 * '\n')
    file.write(thoughts)