input_string = input()

if len(input_string) % 2 == 0:
    first_part_of_string = input_string[0:len(input_string)//2]
    second_part_of_string = input_string[len(input_string)//2:]
else:
    first_part_of_string = input_string[0:len(input_string)//2+1]
    second_part_of_string = input_string[len(input_string)//2:]

if first_part_of_string == second_part_of_string[::-1]:
    print('The entered string is palindrome.', end='')
else:
    print('The entered string is not palindrome.', end='')
