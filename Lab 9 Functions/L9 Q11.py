def create_list(list1, list2):

    return [item for item in list1 if item in list2]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(create_list(list1, list2))  