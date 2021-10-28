from collections import Counter

input_lst = input("Mời bạn nhập dãy số điểm thi:").split()
sorted_lst = []
for i in range(len(input_lst)):
    sorted_lst.append(int(input_lst[i]))
sorted_lst = sorted(sorted_lst)
print(sorted_lst)
lst_mode = []


def find_mean(lst):
    mean = sum(lst)/len(lst)
    return mean

def find_median(lst):
    i = (len(lst) // 2)
    if len(lst) % 2 == 1: ## nếu dãy số là lẻ  
        median = lst[i-1]
    else:
        median = (lst[i] + lst[i-1])/2
    return median

def find_mode(lst):
    count = Counter(lst)
    all_value = count.values()
    max_value = max (all_value)
    print(max_value)
    
    while len (count):
        value_tup_gen = count.popitem()
        my_set_gen.add(value_tup_gen[1])
        list_dict = list_dict

find_mode(sorted_lst)


