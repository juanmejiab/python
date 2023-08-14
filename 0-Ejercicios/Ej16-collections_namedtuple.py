from collections import namedtuple

students_amount = int(input())
Student = namedtuple('Student', input().split())
total_marks = 0

for _ in range(students_amount):
    s = Student._make(input().split())
    total_marks += int(s.MARKS)

print('{:.2f}'.format(total_marks / students_amount))
