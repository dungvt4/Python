##unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}
my_dict = dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)
my_set = {}
my_set = set()
def unique_value_dict (my_dict):
    while len (my_dict):
        value_tup = my_dict.popitem()
        my_set.add(value_tup[1])
        my_dict = my_dict
unique_value_dict (my_dict)
print(my_set)


##Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.
list_dict = [
    {"V":"S001"}, 
    {"V": "S002"}, 
    {"VI": "S001"}, 
    {"VI": "S005"}, 
    {"VII":"S005"}, 
    {"V":"S009"},
    {"VIII":"S007"}
]
my_set2 = {}
my_set2 = set()
for i in range(len(list_dict)):
    sep_dict = list_dict[i]
    #print(type(sep_dict))
    while len (sep_dict):
      value_tup2 = sep_dict.popitem()
      my_set2.add(value_tup2[1])
      sep_dict = sep_dict
print(my_set2)



## tổng quan truyền vào các list dictionary khác nhau
def unique_value_dict (list_dict):
  if type(list_dict) == list:
    for i in range(len(list_dict)):
      sep_dict_gen = list_dict[i]
      while len (sep_dict_gen):
        value_tup_gen = sep_dict_gen.popitem()
        my_set_gen.add(value_tup_gen[1])
        sep_dict_gen = sep_dict_gen
  elif type(list_dict) == dict:
    while len (list_dict):
        value_tup_gen = list_dict.popitem()
        my_set_gen.add(value_tup_gen[1])
        list_dict = list_dict

list_dict_gen = dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)
my_set_gen = {}
my_set_gen = set()
unique_value_dict (list_dict_gen)
print(my_set_gen)




