#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Quang Le - Techmaster.vn - 09/2021


"""Wordcount exercise

Hàm main() đã được định nghĩa hoàn chỉnh ở dưới. Bạn phải viết hàm get_words()
và get_top_words() mà sẽ được gọi từ main().

1. Với đối số --count, viết hàm get_words(filename) đếm số lần xuất hiện của mỗi từ 
trong file đầu vào và trả list các tuple theo định dạng sau:
[(word1, count1), 
(word2, count2)
...]

Trả ra danh sách trên theo thứ tự từ điển các từ (python sẽ sắp xếp dấu câu đứng trước
các chữ cái nên cũng không thành vấn đề). Lưu tất cả các từ dưới dạng chữ thường,
vì vậy 'The' và 'the' được tính là cùng một từ.

2. Với đối số --topcount, viết hàm get_top_words(filename) tương tự như get_words()
nhưng chỉ trả ra 20 từ thông dụng nhất sắp xếp theo từ thông dụng nhất ở trên cùng.

Tùy chọn: định nghĩa một hàm helper để tránh lặp lại code trong các hàm 
get_words() và get_top_words().

"""

import sys
from collections import Counter
from docx import Document

# +++your code here+++

def get_words(filename):
  row = []
  list_tup = []
  with open(f"{filename}", 'r',encoding='latin1') as file:
    for line in file:
      file.readline()
      row.append(line.rstrip("\n"))
      row.append('')
    list_str = row.split()
    Counter(list_str)
        


def get_top_words(filename):
  pass

###

# This basic command line argument parsing code is provided and
# calls the get_words() and get_top_words() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  ans = []
  if option == '--count':
    ans = get_words(filename)
  elif option == '--topcount':
    ans = get_top_words(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

  # print out the answer
  for item in ans:
    print(item[0], item[1])

if __name__ == '__main__':
  main()
