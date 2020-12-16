f = open('text.txt', 'r')

arr = [int(i) for i in f.read().split(',')]

while True:
    last_num = arr[-1]
    indices = [i for i, x in enumerate(arr) if x == last_num]
    if len(indices) == 1:
        arr.append(0)
    else:
        cur_idx = len(arr)
        old_idx = indices[-2] + 1
        arr.append(cur_idx - old_idx)
    if len(arr) == 2020:
        print(arr[-1])
        break

# Part 2
f = open('text.txt', 'r')

arr = [int(i) for i in f.read().split(',')]
last_spoken = {}
pos = 1
next_num = 0

for num in arr:
    last_spoken[int(num)] = pos
    pos += 1

while True:
    current_num = next_num
    if current_num in last_spoken:
        next_num = pos - last_spoken[current_num]
    else:
        next_num = 0
    last_spoken[current_num] = pos
    pos += 1
    if pos == 30000001:
        print(current_num)
        break