def remove_duplicates(x):
    list_ = []
    for item in x:
        if item not in list_:
            list_.append(item)
    return list_

print remove_duplicates([1, 2, 1, 3, 4])