def paired_brackets_or_not(input_str):
    stack = []
    if not input_str:
        return True
    else:
        for char in input_str:
            if char in ["{", "[", "(", "\\"]:
                stack.append(char)
            else:
                if not stack:
                    return False
                newest_char = stack.pop()
                if newest_char == "{":
                    if char != "}":
                        return False
                    if '[' in stack or '(' in stack:
                        return False
                if newest_char == '[':
                    if char != ']':
                        return False
                    if '(' in stack:
                        return False
                if newest_char == '(':
                    if char != ')':
                        return False
                if newest_char == '\\':
                    if char != '/':
                        return False
        if stack:
            return False
        return True

while True:
    try:
        print(paired_brackets_or_not(input()))
    except:
        break
