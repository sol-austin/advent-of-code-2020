f = open('text.txt', 'r')

arr = [i.split('\n') for i in f.read().split('\n\n')]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count_arr = []

def checkGroup(alpha_letter, group):
    for person in group:
        if alpha_letter not in person:
            return 0
    return 1

for group in arr:
    count = 0
    for alpha_letter in alphabet:
        count += checkGroup(alpha_letter, group)
    count_arr.append(count)

print(sum(count_arr))