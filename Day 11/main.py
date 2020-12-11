f = open('text.txt', 'r')

old_arr = [list(i) for i in f.read().split('\n')]


def getAdjacentSeatsFromArr(arr, row_idx, letter_idx):
    ret_arr = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            try:
                to_add = arr[row_idx+x][letter_idx+y]
            except:
                to_add = '.'
            ret_arr.append(to_add)
    return ret_arr

from collections import Counter
import copy
outer_count = 0

while True:
    new_arr = copy.deepcopy(old_arr)
    outer_count += 1

    for row_idx, row in enumerate(old_arr):
        for letter_idx, letter in enumerate(row):
            adj_arr = getAdjacentSeatsFromArr(old_arr, row_idx, letter_idx)
            count = Counter(adj_arr)
            if letter == '.':
                continue
            if letter == 'L':
                if count['#'] == 0:
                    new_arr[row_idx][letter_idx] = '#'
            if letter == '#':
                if count['#'] > 3:
                    new_arr[row_idx][letter_idx] = 'L'

    if old_arr == new_arr:
        print(outer_count)
        print(sum([x.count('#') for x in new_arr]))
        print('done')
        break
    else:
        old_arr = copy.deepcopy(new_arr)

to_file_str = ''
for outer_item in old_arr:
    for inner_item in outer_item:
        to_file_str += inner_item
    to_file_str += '\n'

text_file = open("output.txt", "w")
text_file.write(to_file_str)
text_file.close()