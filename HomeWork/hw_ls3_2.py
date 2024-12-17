numbers = [1, 16, 19, 2, 22, 33, 5, 99]
if len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    numbers.pop()
print("Result_1:", numbers)

numbers = [4]
if len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    numbers.pop()
print("Result_2:", numbers)

numbers = []
if len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    numbers.pop()
print("Result_3:", numbers)

numbers = [1, 16, 19, 2, 33, 5]
if len(numbers) > 1:
    numbers.insert(0, numbers[-1])
    numbers.pop()
print("Result_4:", numbers)
