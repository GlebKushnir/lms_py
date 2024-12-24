while True:
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
                total = "\033[91mError\033[0m"
            else:
                total = number1 / number2
                if total == int(total):
                    total = int(total)
        case _:
            print("\033[91mWrong operation, start again!\033[0m")
            continue

    print("Result:", total)

    print("Do you want to continue? (yes/no): ")
    print("1 = Yes")
    print("2 = No")
    user_input = input("Make a choice: ")
    if user_input == "2":
        print("Exit...")
        break
    elif user_input == "1":
        continue
    else:
        print("\033[91mWrong operation, start again!\033[0m")
        break
