list1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 8, 6, ]

list1.append("???")
print(list1)

list1.insert(2,"GG")
print(list1)

list2 = ["不合适吧","GG"]
list1.extend(list2)
print(list1)