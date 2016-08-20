def digit_sum(n):
    list_ = []
    n = str(n)
    
    for item in n:
        item = int(item)
        list_.append(item)
    return sum(list_)
    print sum(list_)