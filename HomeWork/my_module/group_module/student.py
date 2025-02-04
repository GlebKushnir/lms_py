from .human import Human


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.first_name, self.last_name, self.age, self.gender, self.record_book) == (other.first_name, other.last_name, other.age, other.gender, other.record_book)
        return False

    def __hash__(self):
        return hash(str(self))
