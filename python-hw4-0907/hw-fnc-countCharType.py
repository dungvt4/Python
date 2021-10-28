# ASCII = "".join(chr(x) for x in range(33, 128))
# print(ASCII)


s = input("Mời bạn nhập chuỗi kí tự:")
print(type(s))
rslt_dict = {"LETTERS":0, "CASE": {"UPPER CASE":0, "LOWER CASE":0}, "DIGITS":0}
dict_case = {"UPPER CASE":0, "LOWER CASE":0}

#=========================Hàm dùng bất kì built-in nào=========================
def count_char_type(s):
    upper_case = 0
    lower_case = 0
    digit = 0
    for i in range(len(s)):
        s_int = ord(s[i])
        if s_int in range(65, 91):
            upper_case += 1
        elif s_int in range(97, 123):
            lower_case += 1
        elif s_int in range(48, 58):
            digit += 1
    letter = upper_case + lower_case
    rslt_dict["LETTERS"] = letter
    rslt_dict["DIGITS"] = digit
    dict_case["UPPER CASE"] = upper_case
    dict_case["LOWER CASE"] = lower_case
    rslt_dict["CASE"] = dict_case
    return rslt_dict

count_char_type(s)
rslt_dict


#=========================Hàm chỉ dùng 1 hàm built-in=========================
def count_char_type2(s):
    upper_case = 0
    lower_case = 0
    digit = 0
    for x in s:
        s_int = ord(x)
        if s_int in range(65, 91):
            upper_case += 1
        elif s_int in range(97, 123):
            lower_case += 1
        elif s_int in range(48, 58):
            digit += 1
    letter = upper_case + lower_case
    rslt_dict["LETTERS"] = letter
    rslt_dict["DIGITS"] = digit
    dict_case["UPPER CASE"] = upper_case
    dict_case["LOWER CASE"] = lower_case
    rslt_dict["CASE"] = dict_case
    return rslt_dict

count_char_type2(s)
rslt_dict