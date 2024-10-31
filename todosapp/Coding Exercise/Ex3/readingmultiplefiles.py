file = open('a.txt', 'r')
file.close()
text_a = file.read()

file = open('b.txt', 'r')
text_b = file.read()
file.close()

file = open('c.txt', 'r')
text_c = file.read()
file.close()

print(text_a, text_b, text_c)

#Better faster - Course Solution

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)