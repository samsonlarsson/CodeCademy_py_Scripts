def median(n):
    n = sorted(n)
    b = len(n)
    if b % 2 == 0:
        return (n[len(n)/2] + n[(len(n)/2) - 1]) / 2.0
    else:
        return n[(len(n)-1)/2]
print median([4, 3, 2, 1, 5])