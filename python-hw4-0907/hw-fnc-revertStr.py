#=======================Code kiểu thông thường===========================
def reverseStr(s):
    f_sen = []
    word = s.split()
    for o in word[::-1]:
        f_sen.append(reverseChar(o))
    return " ".join(f_sen)

def reverseChar(w):
    new_w = []
    for char in w:
        if ord(char) in range(65, 91):
            char = char.lower()
        elif ord(char) in range(97, 123):
            char = char.upper()
        new_w.append(char)   
    # new_w = [char.lower() if ord(char) in range(65, 91) else char.upper() for char in w]
    return ''.join(new_w)



sen = "Chicken The For Coming Is Fox The !!#$%$^%$"
print(reverseStr(sen))

sen2 = "tHE fOX iS cOMING fOR tHE cHICKEN"
print(reverseStr(sen2))


#===================code kiểu comprehension============================

def reverseStr2(s):
    word = s.split()
    return " ".join([reverseChar(o) for o in word[::-1]])  ## viết theo list comprehension - rút gọn 3 dòng comment

def reverseChar2(w):
    new_w = [char.lower() if ord(char) in range(65, 91) else char.upper() for char in w]
    return ''.join(new_w)


print("Kết quả của code comprehension:")
sen3 = "Chicken The For Coming Is Fox The "
print(reverseStr2(sen3))
sen4 = "tHE fOX iS cOMING fOR tHE cHICKEN @#$"
print(reverseStr2(sen4))

