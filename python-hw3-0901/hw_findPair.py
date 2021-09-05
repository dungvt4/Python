## Bài toán cụ thể
A = [3, 6, 7, 9, 11, 12] 
sum = 18
lst_result = []
for i in range (0,len(A)):
    j = len(A)-1
    while i < j:
        #print(A[i] ,  A[j])
        if (A[i] +  A[j] == sum):
            list_pair = []
            list_pair.extend([A[i],A[j]])
            list_tup = tuple(list_pair)
            lst_result.append(list_tup)
        j -= 1
print("Các cặp số thỏa mãn là: ", lst_result)

## Bài toán tổng quan nhập chuỗi và sum bất kì từ đó tìm ra cặp số thỏa mãn sum
input_lst = input("Nhập dãy số: ").split()
sum = int(input("Nhập số nguyên sum:"))
sorted_lst=[]
for k in range (len(input_lst)): 
    if (input_lst[k] not in sorted_lst):
        sorted_lst.append(input_lst[k])
sorted_lst = sorted(sorted_lst)
lst_result = []
for i in range (0,len(sorted_lst)):
    j = len(sorted_lst)-1
    while i < j:
        #print(A[i] ,  A[j])
        if (int(sorted_lst[i]) +  int(sorted_lst[j]) == sum):
            list_pair = []
            a = int(sorted_lst[i])
            b = int(sorted_lst[j])
            list_pair.extend([a, b])
            list_tup = tuple(list_pair)
            lst_result.append(list_tup)
        j -= 1
print("Danh sách các số sắp xếp theo thứ tự tăng dần: ", sorted_lst)
print("Các cặp số có tổng thỏa mãn", sum," là: ", lst_result)