import numpy as np

f = open('text.txt', 'r')

arr_1d = [i.replace('#', 'T').replace('.', 'N') for i in f.read().split('\n')]
arr_2d = [list(i) for i in arr_1d]

def check_rows(move_right, move_down = 1):
    line_len = len(arr_2d[0]) - 1
    col_idx = 0
    # row_idx = 0
    tree_count = 0
    num_rows = len(arr_2d)

    for x in range(0, num_rows, move_down):
        x_tree = arr_2d[x][col_idx]
        if x_tree == 'T':
            tree_count += 1

        if line_len - col_idx < move_right:
            col_idx = (col_idx + move_right) - (line_len+1) # Because its an index, you need to subtract an extra 1
        else:
            col_idx += move_right

    return tree_count

check_arr = [[1,1],[3,1],[5,1],[7,1],[1,2]]
arr_result = []

for x in check_arr:
    i = check_rows(x[0], x[1])
    arr_result.append(i)

print(np.prod(arr_result))