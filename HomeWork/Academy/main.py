from group import Group
from student import Student
from group_limit_exception import GroupLimitException
import os

def main():
    st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
    st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
    st3 = Student("Male", 22, "Vasya", "Deegree", "AN146")
    st4 = Student("Female", 23, "Donna", "Pablisko", "AN147")
    st5 = Student("Male", 24, "Mike", "Tyson", "AN148")
    st6 = Student("Female", 21, "Taylor", "Swift", "AN149")
    st7 = Student("Male", 26, "Andrea", "Cho", "AN150")
    st8 = Student("Female", 27, "Vu", "Hong", "AN151")
    st9 = Student("Male", 28, "Don", "Green", "AN152")
    st10 = Student("Female", 29, "Nina", "Blue", "AN153")
    st11 = Student("Male", 31, "Paul", "Rassel", "AN154")

    gr = Group("PD1")
    students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

    output_file_path = os.path.join(os.path.dirname(__file__), "group.txt")
    with open(output_file_path, "w", encoding="utf-8") as file:
        for student in students:
            try:
                gr.add_student(student)
                file.write(
                    f"Студент {student.first_name} {student.last_name} добавлен в группу.\n"
                )
            except GroupLimitException as error:
                file.write(f"{error}\n")

        file.write(str(gr))

    print(gr)

if __name__ == "__main__":
    main()
