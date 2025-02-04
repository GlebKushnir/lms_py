class GroupLimitException(Exception):
    def __init__(self, message="Группа заполнена. Нельзя добавить больше 10 студентов.\n"):
        self.message = message
        super().__init__(self.message)
