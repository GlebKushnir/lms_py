number = int(input("Please, enter your number\n\t---->\t"))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10

print(n1, n2, n3, n4, sep="\n")

result = n1 + n2 + n3 + n4
print("Result:", result)
