f = open('text.txt', 'r')

arr = [int(i) for i in f.read().split('\n')]

def checkPrev25(i, check_num):
    for inner1 in range(i-25, i):
        for inner2 in range(i-25, i):
            inner_num1 = arr[inner1]
            inner_num2 = arr[inner2]
            if (inner_num1 + inner_num2 == check_num) and (inner1 != inner2):
                return True
    return False


for i in range(25, len(arr)):
    num = arr[i]
    ans = checkPrev25(i, num)
    if ans == False:
        print(num)
        print('Index ' + str(i))
        break

# Part 2
arr = arr[:558]
final_num = arr[557]

for start_idx in range(len(arr)):
    for end_idx in range(len(arr)):
        final_arr = arr[start_idx:end_idx]
        if sum(final_arr) == final_num:
            print(max(final_arr) + min(final_arr
                                       ))