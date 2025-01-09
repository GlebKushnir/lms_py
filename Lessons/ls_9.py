# def factorial(number):
#     if number <= 1:
#         return 1
    
#     return number * factorial(number - 1)

# print(factorial(5))

# def my_pow(base, exponent):
    # if exponent <= 1:
    #     return base
    
    # return base * my_pow(base, exponent - 1)

# result = my_pow(2, 3)
# print(result)

# def fib(number):
#     if number == 0 or number == 1:
#         return number
    
#     return fib(number - 1) + fib(number - 2)

# print(fib(4))

# for i in range(10):
#     print(fib(i), end=" ")


# names = ['Alice', 'Bob', 'Charlie', 'David']
# ages = [25, 30, 22, 55]
# zipped_data = zip(names, ages)
# result = list(zipped_data)
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
# final_result = list(result)
# print(final_result)

# numbers = [1, 2, 3, 4, 5]
# squared_root = map(lambda x: x**0.5, numbers)
# result = list(squared_root)
# print(result)

# nums = [n for n in range(10)]
# print(nums)

# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)

# users = {1: 'John', 2: 'Peter', 3: 'Max'}
# names = [name for name in users.values()]
# print(names)

# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)

# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)

# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)

# my_set = {i for i in range(10)}
# print(my_set)


# import random
# from random import *
# from random import randint, choice

# print(random.randint(1, 100))
# print(random.random())
# print(random.choice("qwerty"))
# print(random.randrange(2, 100))
# print(random.randrange(2, 100, 2))
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)
# print(nums)



# import math

# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3))
# print(math.sqrt(9))


# from decimal import *

# numbers = 0.1 + 0.1 + 0.1
# print(numbers)
# numbers = Decimal('0.1')
# numbers = numbers + numbers + numbers
# print(numbers)

# number = Decimal("0.333")
# number = number.quantize(Decimal('1.00'))
# print(number)

# number = Decimal("0.333")
# number = number.quantize(Decimal('1.0000'))
# print(number)

# number = Decimal("12.123456789")
# number = number.quantize(Decimal('1.000'))
# print(number)


# import datetime as dt

# print(dt.datetime.today())
# print(dt.date(2022, 11, 10))
# print(dt.time())
# print(dt.time(10, 13, 15))
# print(dt.time(10, 13))
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}")

# print(dt.datetime)
# my_date = dt.datetime.strptime("2022-11-10", "%Y-%m-%d")
# print(my_date)