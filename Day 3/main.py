f = open('text.txt', 'r')

arr_1d = [i.replace('#', 'T').replace('.', 'N') for i in f.read().split('\n')]
arr_2d = [list(i) for i in arr_1d]

line_len = len(arr_2d[0]) - 1
col_idx = 0
# row_idx = 0
tree_count = 0
num_rows = len(arr_2d)

for x in range(num_rows):
    x_tree = arr_2d[x][col_idx]
    if x_tree == 'T':
        tree_count += 1

    if line_len - col_idx < 3:
        col_idx = (col_idx + 3) - (line_len+1) # Because its an index, you need to subtract an extra 1
    else:
        col_idx += 3

print(tree_count)