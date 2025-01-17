#$ V1
# try:
#     my_file = open("hello.txt", "w")
#     try:
#         my_file.write("hello")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)

# ## V2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("test1")

# import pickle

# FILENAME = "notes.dat"

# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "6488493939"]
# ]

# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file) # сериализация

# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file) # десериализация
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")


# import os

# os.mkdir("test_folder") # создать папку

# os.rmdir("test_folder") # удалить папку

# file_name = "users.csv"
# if os.path.exists(file_name):
#     os.remove(file_name) # удалить файл

# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("Hello, World!")

# with open("../../../test.txt", "w") as myfile:
#     myfile.write("Hello, World!")



# class Car:
#     def __init__(self, name):
#         self.name = name

#     def show_info(self):
#         print(f"My car: {self.name}")

# bmw = Car("BMW X5")
# toyota = Car("Toyota Camry")
# print(type(bmw))

# bmw.show_info()
# toyota.show_info()


# class Test:
#     someTest = "Hello World"

#     def __init__(self, input_text="demo_text"):
#         self.text = input_text

#     @staticmethod
#     def show():
#         print("this is test class")
    
#     def demo_func(self):
#         print(f"this is demo func with value: {self.text}")

# my_test1 = Test("test text 1")
# my_test1.show()

# my_test2 = Test("test text 2")
# my_test2.show()
# my_test2.demo.func()

# Test.show()
# Test.demo_func()

# print(Test.someTest)
# print(my_test2.text)


