def positive_int(n):
    if int(all(n)) >= 0:
        return int(n)
    else:
        raise ValueError
