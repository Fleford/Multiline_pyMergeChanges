
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
        return None

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
        return None

    return d


with open('test.tex', 'r') as f:
    f_string = f.read()

# Start applying changes
edit_found = True
while edit_found:
    edit_found = False

    # Apply first \deleted found
    if not f_string.find('\\deleted') == -1:
        edit_found = True
        d_curly_bracket = find_curly_brackets(f_string)
        d_square_bracket = find_square_brackets(f_string)
        deleted_start_index = f_string.find('\\deleted')
        left_square_bracket = deleted_start_index + 8
        right_square_bracket = d_square_bracket[left_square_bracket]
        left_curly_bracket = right_square_bracket + 1
        right_curly_bracket = d_curly_bracket[left_curly_bracket]
        print(f_string[deleted_start_index:right_curly_bracket + 1])
        print()
        f_string = f_string[:deleted_start_index] + f_string[right_curly_bracket + 1:]

    # Apply first \added found
    if not f_string.find('\\added') == -1:
        edit_found = True
        d_curly_bracket = find_curly_brackets(f_string)
        d_square_bracket = find_square_brackets(f_string)
        added_start_index = f_string.find('\\added')
        left_square_bracket = added_start_index + 6
        right_square_bracket = d_square_bracket[left_square_bracket]
        left_curly_bracket = right_square_bracket + 1
        right_curly_bracket = d_curly_bracket[left_curly_bracket]
        print(f_string[added_start_index:right_curly_bracket + 1])
        print()
        f_string = f_string[:added_start_index] + f_string[left_curly_bracket + 1:right_curly_bracket] + \
            f_string[right_curly_bracket + 1:]

    # Apply first \replaced found
    if not f_string.find('\\replaced') == -1:
        edit_found = True
        d_curly_bracket = find_curly_brackets(f_string)
        d_square_bracket = find_square_brackets(f_string)
        added_start_index = f_string.find('\\replaced')
        left_square_bracket = added_start_index + 9
        right_square_bracket = d_square_bracket[left_square_bracket]
        first_left_curly_bracket = right_square_bracket + 1
        first_right_curly_bracket = d_curly_bracket[first_left_curly_bracket]
        second_left_curly_bracket = first_right_curly_bracket + 1
        second_right_curly_bracket = d_curly_bracket[second_left_curly_bracket]
        print(f_string[added_start_index:first_right_curly_bracket + 1])
        print()
        f_string = f_string[:added_start_index] + f_string[first_left_curly_bracket + 1:first_right_curly_bracket] + \
            f_string[second_right_curly_bracket + 1:]

# Save revised version
with open('test_merge.tex', 'w') as f_out:
    f_out.write(f_string)
