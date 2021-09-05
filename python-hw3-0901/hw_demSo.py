# my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
# my_dict = {}
# for i in range (len(my_list)):
#     key = my_list[i]
#     value = 0
#     j = 0
#     while j < len(my_list):
#         if my_list[j] == key:
#             value += 1
#         j += 1
#     my_dict[key] = value
# print(my_dict)


my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
my_empty_dict = {}
for i in range (len(my_list)):
    key = my_list[i]
    value = 1
    if (key in my_empty_dict):
        value = my_empty_dict[key]
        value +=1
    my_empty_dict[key] = value
print(my_empty_dict)

