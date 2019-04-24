# coding:utf-8
# life is short, you need Python！


import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'canvas_path.settings')

django.setup()
import csv
from users.models import CustomUser, Course, Sections, Homework_grades, Enrolls, Exam_grades, Department
from django.contrib.auth.hashers import make_password


def loadUser(row):
    if CustomUser.objects.filter(email=row[1]).count() == 0:
        CustomUser.objects.create(first_name=row[0], username=row[1], email=row[1], role='S', age=row[2],
                                  zipcode=row[3], gender=row[5], password=make_password(row[8]), street=row[9])
        print("user: " + row[1])
    else:
        CustomUser.objects.filter(email=row[1]).update(first_name=row[0], username=row[1], role='S', age=row[2],
                                                       zipcode=row[3], gender=row[5], password=make_password(row[8]),
                                                       street=row[9])


def loadSection(row):

    if Sections.objects.filter(sec_no2=row[15], section_type=row[14]).count() == 0:
        Sections.objects.create(sec_no2=row[15], section_type=row[14], limit=row[16])
        print("Sections: " + row[15])
    if Sections.objects.filter(sec_no2=row[27], section_type=row[26]).count() == 0:
        Sections.objects.create(sec_no2=row[27], section_type=row[26], limit=row[28])
        print("Sections: " + row[27])
    if Sections.objects.filter(sec_no2=row[39], section_type=row[38]).count() == 0:
        Sections.objects.create(sec_no2=row[39], section_type=row[38], limit=row[40])
        print("Sections: " + row[39])


def loadCourse(row):
    # =============== course1
    Course.objects.update_or_create(course_id=row[11],
                                    defaults={'course_name': row[12], 'course_description': row[13],
                                              'section': Sections.objects.filter(sec_no2=row[15],
                                                                                 section_type=row[14]).first()})
    # 'grade': row[22]
    Enrolls.objects.update_or_create(course_id_id=row[11], student_email_id=row[1],
                                     defaults={'section_no': Sections.objects.filter(sec_no2=row[15],
                                                                                     section_type=row[14]).first()})

    # =========== course2
    Course.objects.update_or_create(course_id=row[23],
                                    defaults={'course_name': row[24], 'course_description': row[25],
                                              'section': Sections.objects.filter(sec_no2=row[27],
                                                                                 section_type=row[26]).first()})
    # grade=row[34]
    print("course: " + row[23])
    Enrolls.objects.update_or_create(course_id_id=row[23], student_email_id=row[1],
                                     defaults={'section_no': Sections.objects.filter(sec_no2=row[27],
                                                                                     section_type=row[26]).first()})

    # ======== course3
    Course.objects.update_or_create(course_id=row[35],
                                    defaults={'course_name': row[36], 'course_description': row[37],
                                              'section': Sections.objects.filter(sec_no2=row[39],
                                                                                 section_type=row[38]).first()})
    # grade=row[46]
    print("course: " + row[35])
    Enrolls.objects.update_or_create(course_id_id=row[35], student_email_id=row[1],
                                     defaults={'section_no': Sections.objects.filter(sec_no2=row[39],
                                                                                     section_type=row[38]).first()})


def loadHW(row):
    # hw 1
    if Homework_grades.objects.filter(course_id=row[11], student_email=row[1]).count() == 0:
        Homework_grades.objects.create(course_id_id=row[11], student_email_id=row[1], hw_details=row[18],
                                       grade=row[19])
        print("Homework_grades: " + row[11])
    else:
        Homework_grades.objects.filter(course_id=row[11], student_email=row[1]).update(hw_details=row[18],
                                                                                       grade=row[19])

    # hw 2
    if Homework_grades.objects.filter(course_id=row[23], student_email=row[1]).count() == 0:
        Homework_grades.objects.create(course_id_id=row[23], student_email_id=row[1], hw_details=row[30],
                                       grade=row[31])
        print("Homework_grades: " + row[23])
    else:
        Homework_grades.objects.filter(course_id=row[23], student_email=row[1]).update(hw_details=row[30],
                                                                                       grade=row[31])
    # hw 3
    if Homework_grades.objects.filter(course_id=row[35], student_email=row[1]).count() == 0:
        Homework_grades.objects.create(course_id_id=row[35], student_email_id=row[1], hw_details=row[42],
                                       grade=row[43])
        print("Homework_grades: " + row[35])
    else:
        Homework_grades.objects.filter(course_id=row[35], student_email=row[1]).update(hw_details=row[42],
                                                                                       grade=row[43])


def loadExam(row):
    Exam_grades.objects.update_or_create(course_id_id=row[11], student_email_id=row[1], defaults={'grade': row[22]})
    Exam_grades.objects.update_or_create(course_id_id=row[23], student_email_id=row[1], defaults={'grade': row[34]})
    Exam_grades.objects.update_or_create(course_id_id=row[35], student_email_id=row[1], defaults={'grade': row[46]})
    print(row[11] + " grade: " + row[22])
    print(row[23] + " grade: " + row[34])
    print(row[35] + " grade: " + row[46])


#########==================== load 1_Students.csv

with open('../static/1_Students.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

##  change 40 to len(rows) - 1, will load all rows of 1_Students.csv
for row in rows[1:40]:
    loadUser(row)
    loadSection(row)
    loadCourse(row)
    loadHW(row)
    loadExam(row)

print(rows[0])


#load Professors.csv

def loadProf(row):
    Department.objects.update_or_create(dept_name=row[5], defaults={'dept_detail': row[7]})
    CustomUser.objects.update_or_create(username=row[1], email=row[1],
                                        defaults={'first_name': row[0], 'role': 'P', 'age': row[3],
                                                  'gender': row[4], 'password': make_password(row[2]),
                                                  'department_id': row[5],
                                                  'office_address': row[6], 'title': row[8]})
    Course.objects.update_or_create(course_id=row[10], defaults={'course_prof_id': row[1]})


