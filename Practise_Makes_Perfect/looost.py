def manipulate_data(mylist):
	new_list = []
	count = 0
	sum = 0
	if type (mylist) == list:
		for number in mylist:
			if number > 0:
				count += 1
			if number < 0:
				sum += number
		new_list.append(count)
		new_list.append(sum)
		return new_list
	else:
		return "Only lists allowed"


test = [4, -2, 6, -1]
print manipulate_data(test)