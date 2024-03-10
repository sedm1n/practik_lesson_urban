import io

file = open('text.txt', 'r')

for line in file:
    print(line)

file.close()