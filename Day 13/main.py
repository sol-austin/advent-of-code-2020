f = open('text.txt', 'r')
string = f.read()

aim_num = int(string.split('\n')[0])
arr = [int(i) for i in string.split('\n')[1].split(',') if i != 'x']

diff_dict = {}

for bus in arr:
    diff = bus - (aim_num % bus)
    diff_dict[bus] = diff

#print(min(diff_dict, key=diff_dict.get)*min(diff_dict.values()))

# Part 2
import math

arr = [(i, int(e)) for i, e in enumerate(string.split('\n')[1].split(',')) if e.isdigit()]
times = [t for _, t in arr]
offsets = [time-idx for idx, time in arr]

def crt(ns, bs):
    # Chinese Remainder Theorem
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = math.prod(ns)
    x = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(bs, ns))
    return x % N

print(crt(times, offsets))