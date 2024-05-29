class Course:
    id_course = None
    course_name = None
    teacher = None

    def __init__(self, id_course, course_name, teacher):
        self._id_course = id_course
        self._course_name = course_name
        self._teacher = teacher

    @property
    def id_course(self):
        return self.id_course

    @id_course.setter
    def id_course(self, id_course):
        self.id_course = id_course

    @property
    def course_name(self):
        return self.course_name

    @course_name.setter
    def course_name(self, course_name):
        self.course_name = course_name

    @property
    def teacher(self):
        return self.teacher

    @teacher.setter
    def teacher(self, teacher):
        self.teacher = teacher

    courses = {}
    def create_course(self, teacher):
        self._id_course = int(input("Id curso: "))
        self._course_name = input("Curso: ")
        id_teacher = int(input("Id del profe: "))
        self._teacher = teacher.user[id_teacher]
        self.courses[self.id_course] = self._course_name, self._teacher

    def list_courses(self):
        for i in self.courses.items():
            print(i)