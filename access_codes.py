def answer(l):
    # Initialise arrays to count usage of l[i] as a factor
    len_l = len(l)
    uses = [0] * len_l
    used_in = uses[:]  # Make copy of uses list

    for i, x in enumerate(l):
        for j in xrange(i + 1, len_l):
            if l[j] % x == 0:
                uses[i] += 1
                used_in[j] += 1

    count = 0
    for k in xrange(len_l):
        count += uses[k] * used_in[k]

    return count
