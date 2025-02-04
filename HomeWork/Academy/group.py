from group_limit_exception import GroupLimitException


class Group:
    def __init__(self, number, students_limit=10):
        self.number = number
        self.group = set()
        self.students_limit = students_limit

    def add_student(self, student):
        if len(self.group) == self.students_limit:
            raise GroupLimitException() # 
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"
