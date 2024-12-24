# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

import random

NUMS = random.randint(3, 10)
nums = []
for i in range(NUMS):
    nums.append(random.randint(3, 10))
print(nums)
result = [nums[0], nums[2], nums[-2]]
print(result)