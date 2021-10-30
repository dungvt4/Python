
def sortList(lis):
    return sorted(lis, key = lambda e:(e[2], e[1], e[0]))

todo_list = [(1, 2, 5), (9, 1, 2), (6, 5, 4), (6, 4, 4), (3, 5, 4) , (3, 2, 3), (10, 2, 1)]  
print(sortList(todo_list))