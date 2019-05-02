def answer(s):
    # Remove empty spaces
    s = s.replace('-', '')

    # Remove employees who will not cross anybody
    s = s.lstrip('<').rstrip('>')

    if len(s) <= 1:
        # Only 1 or 0 characters in string, no salutes made
        return 0

    moving_right = 0
    salutes = 0

    for employee in s:
        if employee == '<':
            # Employee is moving left, if there are any right-moving employees in his path increase salute count by 2
            if moving_right > 0:
                salutes += 2 * moving_right
        else:
            # Employee is moving right
            moving_right += 1

    return salutes
