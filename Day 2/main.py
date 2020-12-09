f = open('Day 2/text.txt', 'r')

arr_1d = [i.replace(':', '').replace('-', ' ') for i in f.read().split('\n')]
arr_2d = [i.split(' ') for i in arr_1d]

x = 0

for item in arr_2d:
    count = item[3].count(item[2])

    if (count >= int(item[0]) and count <= int(item[1])):
        x += 1

print(x)