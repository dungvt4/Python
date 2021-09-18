# 1
import datetime
def day_diff(release_date, code_complete_day):
    format_string = "%d/%m/%Y"
    release_date = datetime.datetime.strptime(release_date,format_string)

    format_string = "%Y-%d-%m"
    code_complete_day = datetime.datetime.strptime(code_complete_day,format_string)

    test_day = release_date - code_complete_day
    test_day = test_day.days
    return test_day

# 2
import re
def alpha_num(sentence):
  rslt = []
  lst_str = sentence.split()
  print(lst_str)
  pattern1 = ".*[a-zA-Z]+.*.?[0-9]+.*"
  pattern2 = ".*[0-9]+.*.?[a-zA-Z]+.*"
  for i in range(len(lst_str)):
    sub_str = lst_str[i]
    match1 = re.findall(pattern1,sub_str)
    if match1 and (match1 not in rslt):
      rslt.extend(match1)
    match2 = re.findall(pattern2,sub_str)
    if match2 and (match2 not in rslt):
      rslt.extend(match2)
  return rslt

