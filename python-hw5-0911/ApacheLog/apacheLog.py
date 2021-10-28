import re
import sys

def readfile_image(filename):
    pattern = "GET (.*\.jpg)"
    data = set()
    with open(filename, encoding='utf-8-sig') as f:
        for line in f:
            # content = f.readline()
            data_find = re.findall(pattern, line, re.MULTILINE)
            if (data_find):
                print(data_find)
                data.add(data_find[0])

    domain = get_domain(filename)
    inc = 1
    print ("Danh sách ảnh trong file: ")
    for path in data:
        print(f"{inc}. {domain}{path}")
        inc +=1
               

def get_domain(filename):
    host_pattern = "\.(\w*(\.[a-z]{2,6}))"
    re_host = re.search(host_pattern, filename)
    if re_host:
        domain = ("http://"+re_host.groups()[0])
    else:
        domain = ""
    return domain


def main():
    if len(sys.argv) != 2:
        print ('usage: ./apacheLog.py file')
        sys.exit(1)
    else:
        filename = sys.argv[1]
        readfile_image(filename)
        sys.exit(1)

if __name__ == '__main__':
    main()





