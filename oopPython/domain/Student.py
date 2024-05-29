from domain.User import User


class Student(User):
    program = None

    def __init__(self, id_user, name, mail, password, program):
        super().__init__(id_user, name, mail, password)
        self._program = program

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, program):
        self.program = program

    def create_user(self):
        super().create_user()
        self.program = input("Programa: ")
        self.students[self.id_user] = self.name, self.mail, self.password, self.program

    def list_students(self):
        for i in self.students.items():
            print(i)