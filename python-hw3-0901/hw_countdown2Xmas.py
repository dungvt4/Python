import time
import datetime 
curr_time = datetime.datetime.now()
Xmas_str = "2021-12-24 00:00:00"
format_string = "%Y-%m-%d %H:%M:%S"
Xmas = datetime.datetime.strptime(Xmas_str,format_string)
print(curr_time)
print(Xmas)
t = int(input("Nhập số giây muốn count down: "))
def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end ="\r")
        time.sleep(1)
        t -= 1
while curr_time < Xmas: 
    #print (curr_time)
    remain = Xmas - curr_time
    print("Countdown to Xmas 2021: ",remain )
    curr_time = datetime.datetime.now()
    countdown(t)