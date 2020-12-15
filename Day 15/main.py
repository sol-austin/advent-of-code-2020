f = open('text.txt', 'r')

arr = f.read().split('\n')

sorted_arr = []
mini_arr = {}

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

for item in arr:
    item_key = item.split('=')[0].rstrip()
    item_value = item.split('=')[1].lstrip()
    if item[:4] == 'mask':
        if len(mini_arr.keys()) > 0:
            sorted_arr.append(mini_arr)
        mini_arr = {}
        mini_arr[item_key] = item_value
    else:
        mini_arr[item_key] = item_value

final_values = {}

for group in sorted_arr:
    mask = group['mask']
    addresses = removekey(group, 'mask')
    for key, value in addresses.items():
        key_num = int(key[4:][:-1])
        bin_val = str(bin(int(value)))[2:].zfill(36)
        fin_str = ''
        for i in range(36):
            mask_i = mask[i]
            bin_val_i = bin_val[i]
            if mask_i == bin_val_i:
                fin_str += mask_i
            elif mask_i == 'X':
                fin_str += bin_val_i
            else:
                fin_str += mask_i
        fin_int = int(fin_str, 2)
        final_values[key_num] = fin_int

print(sum(final_values.values()))

# Part 2
import itertools
memory_dict = {}

for group in sorted_arr:
    mask = group['mask']
    addresses = removekey(group, 'mask')
    for key, value in addresses.items():
        key_num = int(key[4:][:-1])
        bin_val = str(bin(int(key_num)))[2:].zfill(36)
        temp_str = ''
        idx_dict = {}
        for i in range(36):
            mask_i = mask[i]
            mem_adr_i = bin_val[i]
            if mask_i == '0':
                temp_str += mem_adr_i
            elif mask_i == '1':
                temp_str += mask_i
            elif mask_i == 'X':
                temp_str += 'X'
                idx_dict[i] = ['0','1']
        keys, values = zip(*idx_dict.items())
        permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
        for permutation in permutations_dicts:
            mem_temp_str = temp_str
            mem_temp_list = list(mem_temp_str)
            for idx, idx_val in permutation.items():
                mem_temp_list[int(idx)] = idx_val
            mem_temp_str = ''.join(mem_temp_list)
            memory_dict[mem_temp_str] = int(value)
print(sum(memory_dict.values()))