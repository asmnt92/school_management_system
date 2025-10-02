class ClassRoom:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.subjects=[]

    def add_student(self,student):
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def  take_semester_final(self): 
        pass

    def get_top_students(self): 
        pass
