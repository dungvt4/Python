from collections import Counter

input_lst = input("Mời bạn nhập dãy số điểm thi:").split()
sorted_lst = []
for point in input_lst:
    sorted_lst.append(int(point))
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
    lst_count = count.most_common()
    lst_mode = [(lst_count[0])[0]]
    for i in range (len(lst_count)-1):
        tup = lst_count[i]
        next_tup = lst_count[i+1]
        if tup[1] > next_tup[1]:
            break
        else: lst_mode.append(next_tup[0])
    return lst_mode
            

mean = find_mean(sorted_lst)
median = find_median(sorted_lst)
mode = find_mode(sorted_lst)

print(mean,median,mode)


