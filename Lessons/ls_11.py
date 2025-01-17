# import random


# def generate_random_list(list_len, start_value=1, end_value=100):

# def bubble_sort(nums):
#     swapped = True

#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1], nums[i]
#                 swapped = True

# bubble_sort(my_sort)

# def selection_sort(nums):
#     for i in range(len(nums)):
#         lowest_value_index = 1
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums(lowest_value_index):
#                 lowest_value_index = j
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > item_to_insert:
#             j -= 1
#         nums[j + 1] = item_to_insert

# my_list = generate_random_list(5)
# print(my_list)
# # selection_sort(my_list)
# insertion_sort(my_list)
# print(my_list)

import re

# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))

# result = re.search(r'world', 'hello world hello')
# print(result.start())
# print(result.end())

# result = re.findall(r'he', 'hello world hello')
# print(result)

# result = re.split(r'l', 'hello world hello')
# print(result)

# result = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)

result = re.findall(r'.', "It is a long established fact that a reader")
print(result)
