import re

def find_curly_brackets(input_string):
    istart = []  # stack of indices of opening brackets
    d = {}  # prepared dictionary
    skip = False
    for i, c in enumerate(input_string):
        if skip:
            skip = False
            continue
        if c == '\\': # Ignore character after backslashes
            skip = True
        if c == '{':
            istart.append(i)
        if c == '}':
            try:
                d[istart.pop()] = i
            except IndexError:
                print('Too many closing parentheses')
    if istart:  # check if stack is empty afterwards
        print('Too many opening parentheses')

    return d


def find_square_brackets(input_string):
    istart = []  # stack of indices of opening brackets
    d = {}  # prepared dictionary
    skip = False
    for i, c in enumerate(input_string):
        if skip:
            skip = False
            continue
        if c == '\\': # Ignore character after backslashes
            skip = True
        if c == '[':
            istart.append(i)
        if c == ']':
            try:
                d[istart.pop()] = i
            except IndexError:
                print('Too many closing parentheses')
    if istart:  # check if stack is empty afterwards
        print('Too many opening parentheses')

    return d


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
# print(repr(f_string))
#
# d_curly_bracket = find_curly_brackets(f_string)
#
# print("Curly bracket")
# print(d_curly_bracket)
#
# d_square_bracket = find_square_brackets(f_string)
#
# print("Square bracket")
# print(d_square_bracket)

print()
edit_found = True
while edit_found:
    edit_found = False
    if not f_string.find('\\deleted') == -1:
        edit_found = True
        d_curly_bracket = find_curly_brackets(f_string)
        d_square_bracket = find_square_brackets(f_string)
        flag_index = f_string.find('\\deleted')
        left_square_bracket = flag_index + 8
        right_square_bracket = d_square_bracket[left_square_bracket]
        left_curly_bracket = right_square_bracket + 1
        right_curly_bracket = d_curly_bracket[left_curly_bracket]
        f_string = f_string[:flag_index] + f_string[right_curly_bracket + 1:]

with open('test_merge.tex', 'w') as f_out:
    f_out.write(f_string)
