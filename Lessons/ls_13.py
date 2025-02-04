# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}')

# class Emloyee(Person):
#     def work(self):
#         print(f"{self.name} is working")

# vasya = Emloyee('Vasya', 25)
# vasya.show_info()
# vasya.work()

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}')

#     class Subject(object):
#         def __init__(self, name):
#             self.name = name

#     class Teacher(Person):
#         def __init__(self, name, age, sunject: list[Subject], experience: int])
#         super().__init__(name, age)
#         self.subject = subject
#         self.experience = experience
    
#     class Student(Person):
#             def __init__(self, name, subject: Subject):
#                  super().__init__(name, age)
#                  self.subject = subject
                         
#     class Academy(object):
#              def __init__(self, name, subject: list[Subject], teachers: list[Teacher], students: list[Student]):
#                  self.name = name
#                  self.subject = subject
#                  self.teacher = teachers
#                  self.student = students
            
