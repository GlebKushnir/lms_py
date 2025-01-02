import keyword
import string

valid_list = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper__value',
            'Get_value', 'get_Value', 'getValue', '3m', 'm3', 'assert', 'assert_exception']

for v1_variable in valid_list:
    if len(v1_variable) > 0:
        if v1_variable in keyword.kwlist:
            print(f"Error! Found {v1_variable} is keyword!")
        elif v1_variable.find("__") != -1:
            is_correct = False
            print(f"Error! Found double '_' in {v1_variable} variable name!")
        elif not v1_variable[0].isnumeric() and v1_variable.islower() and v1_variable.find(" ") == -1:
            is_correct = True
            for symbol in string.punctuation.replace("_", ""):
                if symbol in v1_variable:
                    is_correct = False
                    print(f"Error! Found {v1_variable} is variable name!")
                    break

            if is_correct:
                print(f"Variable {v1_variable} is correct!")
        else:
            print(f"Error! Found {v1_variable} in variable name!")
    else:
        print("Incorrect variable length!")
