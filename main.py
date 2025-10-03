from school import School
from classroom import ClassRoom
from subject import Subject
from person import Person
from teacher import Teacher
from student import Student

# create School 
school = School('Tomader Bidyaloy', 'Chander Desh')

# create class room 
six = ClassRoom('Six')
seven = ClassRoom('Seven')
eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

# add classroom to the school 
school.add_classroom(six)
school.add_classroom(seven)
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding students 
a = Student('Awal', eight)
m = Student('Milu', nine)
s = Student('Samanta', ten)
j = Student('Jannat', six)
asa = Student('Asamoni', seven)

# extra students
n = Student('Nayem', eight)
r = Student('Ritu', nine)
t = Student('Tania', ten)
b = Student('Bithi', six)
z = Student('Zahid', seven)

# Admission of students 
for st in [a, m, s, j, asa, n, r, t, b, z]:
    school.student_admission(st)

# Add teachers 
abul = Teacher('Abul Mia')
babul = Teacher('Babul Khan')
kabul = Teacher('Kabul Hok')
khabul = Teacher('Khabul Mia')

# extra teachers
salma = Teacher('Salma Akter')
jamal = Teacher('Jamal Uddin')

# Adding subjects 
bangla = Subject('Bangla', abul)
english = Subject('English', babul)
math = Subject('Math', kabul)
ict = Subject('ICT', khabul)
science = Subject('Science', salma)
religion = Subject('Religion', jamal)

# Assign subjects to class rooms
six.add_subject(bangla)
six.add_subject(english)
six.add_subject(math)

seven.add_subject(bangla)
seven.add_subject(english)
seven.add_subject(science)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)
eight.add_subject(religion)

nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(ict)

ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)
ten.add_subject(ict)
ten.add_subject(science)
ten.add_subject(religion)



# Print school summary
print(school)
