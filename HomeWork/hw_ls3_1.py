###            FINAL VERSION
number1 = float(input("Enter first number: "))
if number1 == int(number1):
    number1 = int(number1)
print("Choose a maths operation according to 1/2/3/4: ")
print("1 - +")
print("2 - -")
print("3 - *")
print("4 - /")
action = input("Enter your number: ")
number2 = float(input("Enter second number: "))
if number2 == int(number2):
    number2 = int(number2)

match action:
    case "1":
        total = number1 + number2
    case "2":
        total = number1 - number2
    case "3":
        total = number1 * number2
    case "4":
        if number2 == 0:
            total = "Error"
        else:
            total = number1 / number2
            if total == int(total):
                total = int(total)
    case _:
        total = "Wrong operation, start again!"
print("Result:", total)


###            ADDITIONAL VERSION / IGNORE
# number1 = int(input("Enter first number: "))
# print("Choose a maths operation according to 1/2/3/4: ")
# print("1 - +")
# print("2 - -")
# print("3 - *")
# print("4 - /")
# action = input("Enter your number: ")
# number2 = int(input("Enter second number: "))

# match action:
#     case "1":
#         total = number1 + number2
#     case "2":
#         total = number1 - number2
#     case "3":
#         total = number1 * number2
#     case "4":
#         if number2 == 0:
#             total = "Error"
#         else:
#             total = number1 // number2
#     case _:
#         total = "Wrong operation, start again!"
# print("Result:", total)


###    ADDITIONAL VERSION 2/ IGNORE
# number1 = float(input("Enter first number: "))
# if number1.is_integer():
#     number1 = int(number1)
# action = input("Select a maths operation '+' '-' '*' '/': ")
# number2 = float(input("Enter second number: "))
# if number2.is_integer():
#     number2 = int(number2)

# if action == '+':
#     total = number1 + number2
# elif action == '-':
#     total = number1 - number2
# elif action == '*':
#     total = number1 * number2
# elif action == '/':
#     if number2 == 0:
#         total = "Eroor"
#     else:
#         total = number1 / number2
# else:
#     total = "Wrong operation, start again!"
# print("Result:", total)
