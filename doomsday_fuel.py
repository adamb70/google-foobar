from fractions import Fraction, gcd


def build_arrays(m):
    """ Takes array data and builds sub-matrices for terminal, non-terminal, zero, and identity. """
    absorbing = []
    not_absorbing = []
    row_sums = []

    for i, row in enumerate(m):
        row_sum = sum(row)
        row_sums.append(row_sum)
        if row_sum == 0:
            absorbing.append(i)
            continue
        else:
            not_absorbing.append(i)

    not_absorbing_matrix = [[Fraction(m[i][j], row_sums[i]) for j in not_absorbing] for i in not_absorbing]
    absorbing_matrix = [[Fraction(m[i][j], row_sums[i]) for j in absorbing] for i in not_absorbing]

    # Build identity matrix for non-absorbing states
    identity_matrix = []
    for i in range(len(absorbing_matrix)):
        a = [0] * len(absorbing_matrix)
        a[i] = 1
        identity_matrix.append(a)

    return absorbing_matrix, identity_matrix, not_absorbing_matrix


def invert_matrix(m):
    """ Inverts an NxN matrix """
    col = len(m[0])
    # Checks if matrix is square
    if len(m) == len(m[0]):
        # Create identity matrix
        inv = m
        ident = [[int(i == j) for i in range(len(m))] for j in range(len(m))]
        for i in range(len(inv)):
            for j in range(len(inv[i])):
                inv[i].append(ident[i][j])

        row2 = len(inv)
        col2 = len(inv[0])
        for c in range(0, row2):
            for c2 in range(c + 1, row2):
                factor = inv[c2][c] / inv[c][c]
                for r in range(c, col2):
                    inv[c2][r] -= (inv[c][r] * factor)

        for c in range(row2 - 1, 0 - 1, -1):
            factor = inv[c][c]
            for c2 in range(0, c):
                for r in range(col2 - 1, c - 1, -1):
                    inv[c2][r] -= inv[c][r] * inv[c2][c] / factor
            inv[c][c] /= factor

            for r in range(row2, col2):
                inv[c][r] /= factor

    result = []
    for i in range(0, len(inv)):
        arr = []
        for j in range(col, len(inv[i])):
            arr.append(inv[i][j])
        result.append(arr)

    return result


def answer(m):
    absorbing, identity, not_absorbing = build_arrays(m)

    if len(identity) == 0 and len(absorbing) == 0:
        return [1, 1]

    # Subtract non-absorbing matrix from identity matrix of the same size
    i_sub_q = []
    for i, row in enumerate(not_absorbing):
        temp = []
        for j, col in enumerate(row):
            temp.append(identity[i][j] - col)
        i_sub_q.append(temp)

    # Invert I-Q. Use quicker method for 2x2 matrix and long method for NxN matrices
    if len(i_sub_q) == 2:
        det = i_sub_q[0][0] * i_sub_q[1][1] - i_sub_q[0][1] * i_sub_q[1][0]
        inv = []
        for row in i_sub_q:
            inv.append([col / det for col in row])
        inv[0][1], inv[1][0] = -inv[0][1], -inv[1][0]
    else:
        inv = invert_matrix(i_sub_q)

    # Find probabilities of reaching terminal states
    totals = []
    for i in range(len(absorbing[0])):
        val = 0
        for j in range(len(absorbing)):
            val += absorbing[j][i] * inv[0][j]
        totals.append(val)

    # Find common denominator and write output
    ret = []
    l = [x.denominator for x in totals if x != 0]
    lcd = l[0]

    for i in l[1:]:
        lcd = lcd * i / gcd(lcd, i)

    for x in totals:
        if x == 0:
            ret.append(0)
            continue
        factor = lcd / x.denominator
        ret.append(x.numerator * factor)
    ret.append(lcd)

    return ret
