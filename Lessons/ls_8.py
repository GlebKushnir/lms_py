# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def div(a, b): return a / b

# def select_math_operation(user_choice):
#     match user_choice:
#         case '+':
#             return lambda a, b: a + b
#         case '-':
#             return lambda a, b: a - b
#         case '*':
#             return lambda a, b: a * b
#         case '/':
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid operation")

# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(f"Error: {error}")

# message = lambda: print("Hello, World!")
# message()
# print(message)
# print(lambda: print("Hello, World!"))

# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))

# def calculator(a, b, math_operation) -> None:
#     print(math_operation)
#     print(f"Result: {math_operation(a, b)}")

# calculator(2, 5, lambda n1, n2: n1 + n2)
# calculator(2, 5, lambda n1, n2: n1 / n2)

# button=lambda: print("hello world")

# number = 10

# def test():
#     global number

#     number = 11
#     print(number)

# print(number)
# test()
# print(number)

# def outer():
#     number = 1

#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
    
#     inner()
#     print(number)

# outer()

# number = 10

# def outer():
#     global number
#     number = 1
#     new_number = number

#     def inner():
#         global number
#         new_number = 2
#         my_test = 111
#         number = 2

#         def inner_number_2():
#             global number
#             nonlocal new_number
#             nonlocal my_test
#             new_number = 3
#             print(new_number)
#             print(my_test)
#             number = 3

#         inner_number_2()

#     inner()
#     print(new_number)

# outer()
# print(number)

# def show_info(number, *args, text="no text"):
#     print(number)
#     print(args)
#     print(text)

# show_info(10, 2, 3, 4, 5, 6, 7, 8, 9, text="Hello, World!")

# def show_info(**kwargs):
#     print(kwargs)

# show_info(one=1, two=2, three=3, test="Hello, World!")



# def show_info(num, *args, data="test", **kwargs):
#     print(num)
#     print(args)
#     print(data)
#     print(kwargs)

# show_info(100, 2, "hello", 1234, 4567, data="my_data", number=10, text="Hello, World!")


# def show_info(name, age, hobby):
#     print(f"Name: {name}, Age: {age}, Hobby: {hobby}")

# user_date = ["Vasya", 123, "test"]

# show_info(user_date[0], user_date[1], user_date[2])
# show_info(*user_date)

