from person import Person

class Student(Person):

    def __init__(self, name):
        super().__init__(name)
        self.classroom=None
        self.marks=None
        self.grade=None

    def calculate_final_grade(self):
        pass

    @property
    def id(self):
        pass