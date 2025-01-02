# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

nums = int(input("Enter the number of seconds: "))

days = nums // 86400
rem_nums = nums % 86400
hours = rem_nums // 3600
rem_nums %= 3600
minutes = rem_nums // 60
nums = rem_nums % 60

if days == 1:
    day_str = f"{days} день"
elif 2 <= days <= 4:
    day_str = f"{days} дня"
else:
    day_str = f"{days} дней"

result = f"{day_str}, {hours:02}:{minutes:02}:{nums:02}"
print(result)
