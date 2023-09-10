import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudProject.settings')

import django

django.setup()

from crudApp.models import *
from faker import Faker
from random import *

faker = Faker()


def studentObjects(n):
    for i in range(n):
        fStudentID = f"I9100{i}"
        fStudentName = faker.name()
        fStudentAge = randint(15, 18)
        fStudentCity = faker.city()
        fStudentState = "Tamilnadu"
        Students.objects.get_or_create(
            studentID=fStudentID,
            studentName=fStudentName,
            studentAge=fStudentAge,
            studentCity=fStudentCity,
            studentState=fStudentState
        )
        mark = randint(34, 99)
        m1 = m2 = m3 = m4 = m5 = mark
        StudentMarks.objects.get_or_create(
            mark1=m1,
            mark2=m2,
            mark3=m3,
            mark4=m4,
            mark5=m5, )
        if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
            result = 'P'
        else:
            result = 'F'
        total = m1 + m2 + m3 + m4 + m5
        if result == 'P':

            if total >= 5*90:
                grade = 'S'
            elif total >= 5*80:
                grade = 'A'
            elif total >= 5*70:
                grade = 'B'
            else:
                grade = 'C'

        else:
            grade = '-'

        StudentGrades.objects.get_or_create(total=total, grade=grade, result=result)

# studentObjects(10)
