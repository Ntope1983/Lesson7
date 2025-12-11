# Create 2 random classes for 2 Lessons using set()
import random

def create_classes(lesson,students):
    students_b=students.copy()
    students_a = set()
    while len(students_b) > (N / 2):
        x = random.choice(list(students_b))
        students_a.add(x)
        students_b.remove(x)
    print(f"Για το μάθημα  {lesson} η τάξη Α χωρίζεται :{students_a}")
    print(f"Για το μάθημα  {lesson}  η τάξη Β χωρίζεται :{students_b}")

N = 20
Students = set()
for i in range(1, N + 1):
    Students.add(i)

create_classes("Μαθηματικά",Students)
create_classes("Γεωγραφία",Students)