list = [1, 2, 3]
print("Original list:", list)

list.extend([4, 5, 6])
print("extend():", list)

list.append(7)
print("append():", list)

list.insert(2, 8)
print("insert():", list)

list.remove(3)
print("remove():", list)

list.clear()
print("clear():", list)

list = [3, 1, 2, 4, 5]
list.sort()
print("sort():", list)

list.reverse()
print("reverse():", list)

list_copy = list.copy()
print("copy():", list_copy)