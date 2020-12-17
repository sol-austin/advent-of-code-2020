from copy import deepcopy
f = open('text.txt', 'r')

old_arr = [[list(i) for i in f.read().split('\n')]]

def getActiveNeighbors(arr, layer_idx, row_idx, col_val_idx):
    active_count = 0

    for x in range(-1, 2, 1):
        layer_idx_loop = layer_idx + x
        if layer_idx_loop < 0:
            continue
        for y in range(-1, 2, 1):
            row_idx_loop = row_idx + y
            if row_idx_loop < 0:
                continue
            for z in range(-1, 2, 1):
                col_val_idx_loop = col_val_idx + z
                if col_val_idx_loop < 0:
                    continue
                if x == 0 and y == 0 and z == 0:
                    continue
                try:
                    value = arr[layer_idx_loop][row_idx_loop][col_val_idx_loop]
                    if value == '#':
                        active_count += 1
                except:
                    continue

    return active_count



def newActiveVal(arr, layer_idx, row_idx, col_val_idx):
    active_count = getActiveNeighbors(arr, layer_idx, row_idx, col_val_idx)
    if active_count == 2 or active_count == 3:
        return '#'
    else:
        return '.'

def newInactiveVal(arr, layer_idx, row_idx, col_val_idx):
    active_count = getActiveNeighbors(arr, layer_idx, row_idx, col_val_idx)
    if active_count == 3:
        return '#'
    else:
        return '.'

def addPadding(arr):
    for layer in arr:
        layer.append(list(len(layer[0])*'.'))
        layer.insert(0, list(len(layer[0])*'.'))
        for row in layer:
            row.append('.')
            row.insert(0, '.')
    arr.append([list(len(arr[0]) * '.') for i in range(len(arr[0]))])
    arr.insert(0, [list(len(arr[0]) * '.') for i in range(len(arr[0]))])
    return arr

count = 0
new_arr = []
old_arr = addPadding(old_arr)

while True:
    count += 1
    new_arr = deepcopy(old_arr)
    for layer_idx, layer in enumerate(old_arr):
        for row_idx, row in enumerate(layer):
            for col_val_idx, col_val in enumerate(row):
                if col_val == '#':
                    # Active
                    new_arr[layer_idx][row_idx][col_val_idx] = newActiveVal(old_arr, layer_idx, row_idx, col_val_idx)
                else:
                    # Inactive
                    new_arr[layer_idx][row_idx][col_val_idx] = newInactiveVal(old_arr, layer_idx, row_idx, col_val_idx)
    old_arr = addPadding(deepcopy(new_arr))
    if count == 6:
        break

fin_count = 0

for layer in old_arr:
    for row in layer:
        for val in row:
            if val == '#':
                fin_count += 1
print(fin_count)