import math
f = open('text.txt', 'r')

arr = f.read().split('\n')

final_arr = []

for seat in arr:
    front_back = seat[:7]
    right_left = seat[7:]

    back_bound = 127
    front_bound = 0

    right_bound = 7
    left_bound = 0

    for letter in front_back:
        new_bound = (back_bound + front_bound + 1)/2

        if letter == 'F':
            back_bound = math.floor(new_bound - 1)
        else:
            front_bound = math.floor(new_bound)

    final_row = front_bound

    for letter in right_left:
        new_col_bound = (right_bound + left_bound + 1)/2

        if letter == 'R':
            left_bound = math.floor(new_col_bound)
        else:
            right_bound = math.floor(new_col_bound - 1)
    final_col = left_bound

    final_ans = (final_row * 8) + final_col
    final_arr.append(final_ans)


min_ans = min(final_arr)
max_ans = max(final_arr)
for i in range(min_ans, max_ans):
    if i not in final_arr:
        print(i)