def purify(n):
    list_ = []
    for item in n:
        if item % 2 == 0:
            list_.append(item)
    return list_