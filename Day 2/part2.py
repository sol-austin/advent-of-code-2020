f = open('text.txt', 'r')

arr_1d = [i.replace(':', '').replace('-', ' ') for i in f.read().split('\n')]
arr_2d = [i.split(' ') for i in arr_1d]

x = 0

for item in arr_2d:
    idx1 = int(item[0]) - 1
    idx2 = int(item[1]) - 1

    if (item[3][idx1] == item[2]) != (item[3][idx2] == item[2]):
        x += 1

print(x)