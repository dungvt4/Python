import re

pattern = "GET (.*\.jpg)"
with open("animal_code.google.com", encoding='utf-8-sig') as f:   
    for line in f:
        content = f.readline()
        #print(content)
        data_find = re.findall(pattern, content, re.MULTILINE)
        print(data_find)

filename = "animal_code.google.com"
host_pattern = "\.(\w*(\.[a-z]{2,6}))"
re_host = re.search(host_pattern, filename)
if re_host:
    domain = ("https://"+re_host.groups()[0])
else:
    domain = ""
print(domain)

