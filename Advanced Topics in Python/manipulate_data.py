def manipulate_data(list_):
	newlist_ = []
	for item in list_:
		if item >= 0:
			count += 1
			newlist_.append(count)
		else:
			add = sum(item)
			newlist_.append(add)
	return newlist_
