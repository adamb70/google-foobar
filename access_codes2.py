from collections import defaultdict


def answer(l):
    ints = sorted(l)

    # find factors
    factors = defaultdict(list)
    for i, x in enumerate(ints):
        for j in range(i):
            if x % ints[j] == 0:
                factors[x].append(ints[j])
    print factors

    total = 0
    for key in factors.keys()[::-1]:
        count = 0
        checked = set()
        print key, factors[key]

        # There is at least one factor if we are here. Loop through subfactors and count sub-subfactors
        for k in factors[key][::-1]:
            if k in checked:
                continue
            checked.add(k)
            print k, 'subkey'
            # Add count of subfactors to total count, since they are all 3rd order factors
            count += len(factors[k])

        total += count

    return total


l = [1, 1, 1]
l = [3, 3, 3]
print answer(l)

from test import data

for d in data:
    # print answer(d)
    pass
