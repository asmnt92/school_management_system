from person import Person

class Teacher(Person):

    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass

    def evaluate_exam(self):
        pass