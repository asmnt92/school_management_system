from person import Person
import random
class Teacher(Person):

    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass

    def evaluate_exam(self):
        return random.randint(1,100)