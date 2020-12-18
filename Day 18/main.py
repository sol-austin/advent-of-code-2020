f = open('text.txt', 'r')

arr = f.read().split('\n')

def solve_section(section):
    ops_idx_arr = [idx for idx, char in enumerate(section) if char=='*' or char=='+']
    prev_num = section[:ops_idx_arr[0]]
    for op_idx in range(len(ops_idx_arr)):
        op_start_idx = ops_idx_arr[op_idx]
        try:
            op_end_idx = ops_idx_arr[op_idx+1]
        except:
            op_end_idx = len(section)
        prev_num = int(eval(str(prev_num) + section[op_start_idx:op_end_idx]))
    return prev_num
def solve_arr(arr):
    fin_arr = []
    for calculation in arr:
        bracket_pairs_count = calculation.count('(')
        for i in range(bracket_pairs_count-1, -1, -1):
            opening_brackets_arr = [pos+1 for pos, char in enumerate(calculation) if char == '(']
            closed_brackets_idx = calculation.index(')', opening_brackets_arr[i])
            if closed_brackets_idx == -1:
                raise Exception('fuck')
            if len(opening_brackets_arr) == 0:
                continue
            section = calculation[opening_brackets_arr[i]:closed_brackets_idx]
            section_solution = solve_section(section.lstrip().rstrip())
            if i == 0:
                calculation = calculation[:(opening_brackets_arr[i]-1)] + str(section_solution) + calculation[closed_brackets_idx+1:]
            else:
                calculation = calculation[:(opening_brackets_arr[i]-1)] + str(section_solution) + calculation[closed_brackets_idx+1:]
        fin_ans = solve_section(calculation)
        fin_arr.append(fin_ans)
    return fin_arr
print(sum(solve_arr(arr)))