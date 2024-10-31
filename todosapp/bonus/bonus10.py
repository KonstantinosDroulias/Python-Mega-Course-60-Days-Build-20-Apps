try:
    width = float(input('Enter Rectangle width: '))
    length = float(input('Enter Rectangle length: '))

    if width == length:
        exit("This is a square")

    area = width * length
    print(area)

except ValueError:
    print('Please type number')