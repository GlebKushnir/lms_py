# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

nums = [0, 1, 7, 2, 4, 8]
if not nums:
    print("Result:", 0)
else:
    numbers = nums[0::2]
    result = sum(numbers) * nums[-1]
    print("Result:", result)
