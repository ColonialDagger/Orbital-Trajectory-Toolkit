def positive_int(n):
    if int(n) >= 0:
        return int(n)
    else:
        raise ValueError
