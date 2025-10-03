from person import Person
from school import School

class Student(Person):

    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom=classroom
        self.__id=None
        self.marks={} # {'eng':80, 'bang':90}
        self.subject_grade={} # {'eng':'A+', 'bang':'A+'}
        self.grade=None

    def calculate_final_grade(self):
        sum=0
        for grade in self.subject_grade.values():
            point=School.grade_to_value(grade)
            sum+=point

        gpa=sum/len(self.subject_grade)
        self.grade=School.value_to_grade(gpa)

        

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id=id
    