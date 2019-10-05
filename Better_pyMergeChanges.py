import re

line_cnt = 0
with open('test.tex', 'r') as f:
    f_string = f.read()
print(repr(f_string))

    # for line in f:
    #     line_cnt = line_cnt + 1
    #     # char_cnt = 0
    #     # for char in line:
    #     #     char_cnt = char_cnt + 1
    #     #     if char == "\\":
    #     #         print(line_cnt, char_cnt, repr(char))
    #
    #     print(line_cnt, line.find(r"\deleted["))

