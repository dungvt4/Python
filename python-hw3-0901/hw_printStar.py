n = int (input ("Mời bạn nhập số dòng muốn in:"))
if (n <= 0) :
    print("n phải là số nguyên dương")
else: # in tam giác vuông đầu tiên
    for i in range(1,n):
        j = (n-i)*2-1
        print (" "*(j) + " *"*i)
    print("*"+ " *"*(n-1))
    print("\n")

    # in tam giác đối xứng
    for i in range(1,n): #in tam giác vuông ở trên
        j = (n-i)*2-1
        print (" "*(j) + " *"*i)
    print("*" + " *"*(2 * n -1))
    for k in range(n-1, 0, -1): # in tam giác vuông ở dưới
        print(" "* 2*n + "* "*k)
    print("\n")

    #in hình tam giác rỗng đối xứng
    print("*")
    for i in range(2,n):
        j = 2 * (i-2)
        print ("*" + " "*j + " *")
    print("*" + " *"*(2 * n -1))
    for i in range (n-1, 1, -1):             # in tam giác rỗng ở dưới
        j = 2 * (i-2)                        # số khoảng trắng ở giữa 1 dòng
        k = 4*n - j - 4                      # số khoảng trắng ở đầu dòng
        print (" "*k + "* " + " "*j + "*")
    print(" "*(n*4 - 2) + "*" )
    print("\n")

