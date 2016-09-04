def manipulate_data(list_):
    newlist = []
    new = []
    count = 0
    add = []
    for item in list_:
        if item >= 0:
          count += 1
          newlist.append(count)
        if item < 0:
          add.append(item)
          newlist.append(sum(add))
    return newlist
