from itertools import combinations
import operator
import numpy

f = open('text.txt', 'r')
num_arr = f.read().split('\n')
r = 3

combinations_arr = list(combinations(map(int, num_arr), r))

for x in combinations_arr:
    ans = sum(x)
    if ans == 2020:
        print('Product is '+ str(numpy.prod(x)))