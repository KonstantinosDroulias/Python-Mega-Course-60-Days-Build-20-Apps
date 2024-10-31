waiting_list = ('Sen', 'Ben', 'Tom')
waiting_list.sort()

for i, waiting in enumerate(waiting_list):
    row = f'{i}.{waiting.capitalize()}'
    print(row)