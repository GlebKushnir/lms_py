# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

nums = int(input("Enter your number: "))

while nums > 9:
    n_nums = str(nums)
    nums = 1
    for char in n_nums:
        nums *= int(char)

print(nums)