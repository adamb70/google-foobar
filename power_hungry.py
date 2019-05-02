from operator import mul


def answer(xs):
    """ Takes list of ints. Returns max product of list as a string. """
    positives = []
    negatives = []
    zero_found = False

    # Split values into positive and negative lists
    for val in xs:
        if val > 0:
            positives.append(val)
        elif val < 0:
            negatives.append(val)
        else:
            # Set flag if 0 is found
            zero_found = True

    # Assign length of negative list to variable for performance
    neg_length = len(negatives)
    if len(positives) == 0:
        if neg_length == 0:
            # Input list xs is either empty or all values are 0
            return str(0)
        elif neg_length == 1:
            # Return 0 if in xs, else return the negative number
            return str(0) if zero_found else str(negatives[0])

    # If no negative values, return product of positive
    if neg_length == 0:
        return str(reduce(mul, positives))
    elif neg_length % 2 != 0:
        # Count of negative values is not even, sort and remove smallest absolute value
        negatives.sort()
        negatives.pop()

    # Calculate products of negatives and positives. If list is empty set to 1
    neg_total = reduce(mul, negatives, 1)
    pos_total = reduce(mul, positives, 1)

    return str(neg_total * pos_total)
