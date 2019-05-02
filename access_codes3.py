from collections import defaultdict
from time import time

start = time()


def answer(l):
    #factors = defaultdict(list)
    #factors[2].append((number, index))
    print l
    # find factors
    total = 0

    for i, x in enumerate(l):
        print '\nchecking', x
        for j in xrange(i):
            a = l[j]
            print 'against', a
            if x % a == 0:
                print 'found ', a, 'in', x
                for m in xrange(j):
                    if a % l[m] == 0:
                        print 'Found Again', l[m], 'in', a
                        total += 1


    print 'total:', total

    return total


l = [1, 1, 1]
l2 = [1, 2, 3, 4, 5, 6]
print answer(l)

from test import data


for d in data:
    #print answer(d)
    pass

print 'Time taken:', time()-start