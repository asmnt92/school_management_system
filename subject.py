from school import School
class Subject:
    
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher # teacher object
        self.max_marks=100
        self.pass_mark=33


    def exam(self,students): # student list
        
        for student in students:
            mark=self.teacher.evaluate_exam() # 1 - 100 marking hbe
            student.marks[self.name]=mark
            student.subject_grade[self.name]=School.calculate_grade(mark)

