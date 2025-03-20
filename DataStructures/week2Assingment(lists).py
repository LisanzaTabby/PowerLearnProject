#empty List Creation
my_list = []
# append list elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# insert 15 in the second position
my_list.insert(1, 15)
# Extending my list with the another list  [50, 60, 70].
my_list.extend([50,60,70])
# Removing the last element from my list
my_list.pop(7)
# Sorting my_list in asc_order
my_list.sort()
# finding and printing the index value for 30 from my_list
index = my_list.index(30)
print(index)
print(my_list)