f = open('text.txt', 'r')

arr = f.read().split('\n')

visited_idx = []
acc_val = 0
cur_idx = 0

while True:
    if cur_idx in visited_idx:
        break
    else:
        visited_idx.append(cur_idx)
    item = arr[cur_idx]
    instruction = item[:3]
    if instruction == 'jmp':
        cur_idx += int(item[4:])
    else:
        cur_idx += 1
    if instruction == 'acc':
        acc_val += int(item[4:])

print(acc_val)

for switch in range(1,len(arr)):
    acc_val = 0
    visited_idx = []
    cur_idx = 0
    broke = False
    while True:
        if cur_idx in visited_idx:
            break
        else:
            visited_idx.append(cur_idx)

        item = arr[cur_idx]
        instruction = item[:3]

        if switch == cur_idx:
            if instruction == 'jmp':
                instruction = 'nop'
            elif instruction == 'nop':
                instruction = 'jmp'

        if instruction == 'jmp':
            cur_idx += int(item[4:])
        else:
            cur_idx += 1
        if instruction == 'acc':
            acc_val += int(item[4:])

        if cur_idx == len(arr):
            broke = True
            break
    if broke:
        print(switch)
        print(acc_val)
        break