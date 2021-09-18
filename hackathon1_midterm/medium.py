def anagram_number(number):
    num_str = str(number)
    #print(num_str)
    reverse_num = num_str[::-1]
    #print(reverse_num)
    if int(reverse_num) == int(num_str):
        return True
    else:
        return False 


def roman_to_int(s):
    dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum = 0
    for i in range(len(s)):
        if i == 0:
            sum = sum + dict[s[i]]
        else:
            if s[i]=='M':
                sum=sum+1000
                if s[i-1]=='C':
                    sum=sum-200      
            elif s[i]=='D':
                sum=sum+500
                if s[i-1]=='C':
                    sum=sum-200
            elif s[i]=='C':
                sum=sum+100
                if s[i-1]=='X':
                    sum=sum-20
            elif s[i]=='L':
                sum=sum+50
                if s[i-1]=='X':
                    sum=sum-20
            elif s[i]=='X':
                sum=sum+10
                if s[i-1]=='I':
                    sum=sum-2
            elif s[i]=='V':
                sum=sum+5
                if s[i-1]=='I':
                    sum=sum-2
            elif s[i]=='I':
                sum=sum+1
    return (sum)
