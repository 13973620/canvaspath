from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, Course, Enrolls, Exams, Exam_grades, Homework, Homework_grades

from django.template.defaulttags import register


# Create your views here.

@login_required
def index(request):
    user = request.user
    if user.role == 'S':
        enrolls = Enrolls.objects.filter(student_email=user.email).all()
        courses = [enroll.course_id for enroll in enrolls]
        grades = Exam_grades.objects.filter(course_id__in=courses, student_email=user.email).all()

        # make a dict {course_id: grade}
        gl = {gra.course_id_id: gra.grade for gra in grades}

        hws = Homework_grades.objects.filter(student_email=user.email, course_id__in=courses).all()

        return render(request, "index.html", locals())
    elif user.role == 'P':
        courses = Course.objects.filter(course_prof=user.email).all()
        enroll_map = {course.course_id: Enrolls.objects.filter(course_id=course).all() for course in courses}


        return render(request, "prof-index.html", locals())
    else:
        students = CustomUser.objects.filter(role='S').all()
        profs = CustomUser.objects.filter(role='P').all()
        courses = Course.objects.all()
        return render(request, "admin.html", locals())


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key) if dictionary.get(key) else ''


@register.filter
def filter_by_key(dictionary, key):
    students = dictionary.get(key)
    print(students)
    return students


@register.filter
def get_grade(email, course):
    return Exam_grades.objects.filter(course_id=course, student_email=email).first().grade


@register.filter
def get_hw_grade(email, course):
    return Homework_grades.objects.filter(course_id=course, student_email=email).first().grade
