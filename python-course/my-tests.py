# def sortNumsAscending(list):
# 	data_list = list
# 	new_list = []
# 	while data_list:
# 		minimum = data_list[0]
# 		for x in data_list:
# 			if x < minimum:
# 				minimum = x
# 		new_list.append(minimum)
# 		data_list.remove(minimum)
# 	return new_list

# print(sortNumsAscending([4,2,6,9,12,1,5]))

# def sortNumsAscendingAlt(list):
#     return sorted(list)

# print(sortNumsAscendingAlt([45,23,6,78,4,2]))

def month_name(num):
	switcher = {
		1: "January",
		2: "February",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10: "October",
		11: "November",
		12: "December"
	}
	print(switcher.get(num, "invalid month"))

month_name(15)