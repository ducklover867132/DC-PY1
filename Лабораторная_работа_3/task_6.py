list_num = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
high = max(list_num)
list_num[list_num.index(max(list_num))] = list_num[-1]
list_num[-1] = high
print(list_num)
