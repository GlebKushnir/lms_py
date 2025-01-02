# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

ALL_LETTERS = string.ascii_letters
SEPARATOR = "-"

user_input = input("Enter letters in format 'a-c': ").strip()

if len(user_input) == 3 and user_input[1] == SEPARATOR:
    first_letter = user_input[0]
    second_letter = user_input[2]

    if first_letter.isalpha() and second_letter.isalpha():
        start_index = ALL_LETTERS.index(first_letter)
        end_index = ALL_LETTERS.index(second_letter)

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        result = ALL_LETTERS[start_index:end_index + 1]
        print(result)
    else:
        print("Error: Both characters must be letters.")
else:
    print("Error: Input must be in the format 'a-c'.")
