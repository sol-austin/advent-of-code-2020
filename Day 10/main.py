f = open('text.txt', 'r')

arr = sorted([int(i) for i in f.read().split('\n')])
arr.append(arr[-1]+3)

diff_1_count = 0
diff_3_count = 0

for idx, value in enumerate(arr):
    if idx == 0:
        prev_num = 0
    else:
        prev_num = arr[idx-1]
    if value - prev_num == 1:
        diff_1_count += 1
    if value - prev_num == 3:
        diff_3_count += 1

print(diff_1_count*diff_3_count)

# Part 2
import itertools
start_idx = 0
arr_2d = []
for idx, value in enumerate(arr):
    try:
        next_num = arr[idx+1]
    except:
        next_num = value + 3
    if next_num - value == 3:
        arr_2d.append(arr[start_idx:idx+1])
        start_idx = idx + 1
print(arr)

from collections import Counter
count = Counter()
count[0] = 1

for value in arr:
    count[value] = count[value - 1] + count[value - 2] + count[value - 3]

print(count[arr[-1]])