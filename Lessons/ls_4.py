# i = 0

# while i < 5:
#     print(i, end=" ")
#     i += 1

# import time

# i = 12
# while True:
#     print(i)
#     i += 2
#     time.sleep(1)

# while True:
#     raiting = int(input("Enter your raiting from 1 to 3: "))

#     if raiting == 0:
#         print("Exit...")
#         break

#     if raiting < 1 or raiting > 3:
#         print("Invalid Raiting")
#         continue

#     match raiting:
#         case 1:
#             print("Bad raiting")
#         case 2:
#             print("Normal raiting")
#         case 3:
#             print("Excellent raiting")

# for i in range(5):
#     print(i, end=" ")

# for value in 1, 4, "blabla", True, 1.5, "hey":
#     print(value)

# import random

# # print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []

# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))

# print(numbers)

import random
import string


DATA_FOR_PASSWORD = string.digits + string.punctuation + string.ascii_letters
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 16


while True:
    new_password = []

    password_length = int(input("Ender password length (from {MIN_PASSWORD_LEN} to {MAX_PASSWORD_LEN}): "))

    if password_length < MIN_PASSWORD_LEN or password_length > MAX_PASSWORD_LEN:
        print(f"Password must be between {MIN_PASSWORD_LEN} and {MAX_PASSWORD_LEN}")
        for i in range(8):
            new_password.append(random.choice(DATA_FOR_PASSWORD))

        result_password = "".join(new_password)
        print(result_password)

    else:
        print("Password")
