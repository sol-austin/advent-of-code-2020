f = open('text.txt', 'r')

# Convert text file to 2D array
old_arr = [list(i) for i in f.read().split('\n')]


def getAdjacentSeatsFromArr(arr, row_idx, letter_idx):
    ret_arr = []
    # BASTARD - When you take 1 away from 0 it loops back around to -1!
    for x in range(-1, 2):
        if row_idx == 0 and x == -1:
            continue
        for y in range(-1, 2):
            if letter_idx == 0 and y == -1:
                continue
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

while True:
    new_arr = copy.deepcopy(old_arr)

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
        print(sum([x.count('#') for x in new_arr]))
        break
    else:
        old_arr = copy.deepcopy(new_arr)

# Part 2
