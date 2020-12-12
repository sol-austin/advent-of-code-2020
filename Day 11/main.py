f = open('text.txt', 'r')
from collections import Counter
import copy

# Convert text file to 2D array
old_arr = [list(i) for i in f.read().split('\n')]
"""

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
"""
# Part 2
def getSeatsInView(arr, row_idx, letter_idx, _debug_iteration):
    ret_arr = []
    # Above
    for x in range(row_idx-1, -1, -1):
        item = arr[x][letter_idx]
        if item == '#':
            ret_arr.append('#')
            break
        if item == 'L':
            break
    # Below
    for x in range(row_idx+1, len(arr)):
        item = arr[x][letter_idx]
        if item == '#':
            ret_arr.append('#')
            break
        if item == 'L':
            break
    # Left
    for x in range(letter_idx-1, -1, -1):
        item = arr[row_idx][x]
        if item == '#':
            ret_arr.append('#')
            break
        if item == 'L':
            break
    # Right
    for x in range(letter_idx+1, len(arr[row_idx])):
        item = arr[row_idx][x]
        if item == '#':
            ret_arr.append('#')
            break
        if item == 'L':
            break

    # Top Left
    for x in range(row_idx-1, -1, -1):
        row = arr[x]
        diff = row_idx - x
        try:
            if letter_idx - diff >= 0:
                item = row[letter_idx-diff]
                if item == '#':
                    ret_arr.append('#')
                    break
                if item == 'L':
                    break
        except:
            continue

    # Top Right
    for x in range(row_idx-1, -1, -1):
        row = arr[x]
        diff = row_idx - x
        try:
            item = row[letter_idx + diff]
            if item == '#':
                ret_arr.append('#')
                break
            if item == 'L':
                break
        except:
            continue

    # Bottom Left
    for x in range(row_idx+1, len(arr)):
        row = arr[x]
        diff = x - row_idx
        try:
            if letter_idx - diff >= 0:
                item = row[letter_idx - diff]
                if item == '#':
                    ret_arr.append('#')
                    break
                if item == 'L':
                    break
        except:
            continue

    # Bottom Right
    for x in range(row_idx+1, len(arr)):
        row = arr[x]
        diff = x - row_idx
        try:
            item = row[letter_idx + diff]
            if item == '#':
                ret_arr.append('#')
                break
            if item == 'L':
                break
        except:
            continue

    return ret_arr

f = open('text.txt', 'r')
old_arr = [list(i) for i in f.read().split('\n')]
outer_count = 0
while True:
    outer_count += 1
    new_arr = copy.deepcopy(old_arr)

    for row_idx, row in enumerate(old_arr):
        for letter_idx, letter in enumerate(row):
            view_arr = getSeatsInView(old_arr, row_idx, letter_idx, outer_count)
            count = Counter(view_arr)
            if letter == '.':
                continue
            if letter == 'L':
                if count['#'] == 0:
                    new_arr[row_idx][letter_idx] = '#'
            if letter == '#':
                if count['#'] > 4:
                    new_arr[row_idx][letter_idx] = 'L'

    if old_arr == new_arr:
        print(outer_count)
        print(new_arr)
        print(sum([x.count('#') for x in new_arr]))
        break
    else:
        old_arr = copy.deepcopy(new_arr)

