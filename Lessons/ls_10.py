# def additional_logic(func):
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Some logic 2")
#     return wrapper

# @additional_logic
# def hello():
#     print("Hello world")

# hello()


# import time

# current_working_status = True
# current_seconds= 1

# def delay(seconds=0, is_working=True):
#     def decorator(func):
#         if not is_working:
#             return func

#         def wrapper(*args, **kwargs):
#             print(f"Waiting for {seconds} seconds...")
#             time.sleep(seconds)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# @delay(current_seconds, current_working_status)
# def hello():
#     print("Hello")

# hello()


# add = lambda num1: lambda num2: num1 + num2

# configured_add = add(3)

# for i in range(1, 10):
# print(configured_add(i))

# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1

# generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# # for i in generator:
# #     print(1)

