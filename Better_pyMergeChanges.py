import re

line_cnt = 0
with open('test.tex', 'r') as f:
    f_string = f.read()

    # for line in f:
    #     line_cnt = line_cnt + 1
    #     # char_cnt = 0
    #     # for char in line:
    #     #     char_cnt = char_cnt + 1
    #     #     if char == "\\":
    #     #         print(line_cnt, char_cnt, repr(char))
    #
    #     print(line_cnt, line.find(r"\deleted["))
print(repr(f_string))

text = 'aaaa(bb()()ccc)dd'
istart = []  # stack of indices of opening parentheses
d = {}

for i, c in enumerate(f_string):
    if c == '{':
         istart.append(i)
    if c == '}':
        try:
            d[istart.pop()] = i
        except IndexError:
            print('Too many closing parentheses')
if istart:  # check if stack is empty afterwards
    print('Too many opening parentheses')
print(d)
print(repr(f_string[16: 696]))

