from collections import defaultdict


def generate_coefficients(m):
    """ Generates coefficients for Partition Function Q (https://archive.lib.msu.edu/crcmath/math/math/p/p121.htm).
        Returns a dictionary of all coefficients for exponents <= m """
    index = defaultdict(int)
    index[0] = 1
    index[1] = 1
    for n in range(2, m+1):
        for k in range(m, n-1, -1):
            index[k] += index[k - n]
    return index

# Generate once for all values up to 200 and keep in memory
coeffs = generate_coefficients(200)


def answer(n):
    # Partition Function Q includes (X+0) in number of distinct sums for X, so subtract 1 to ignore this
    return coeffs[n]-1
