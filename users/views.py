from django.shortcuts import render, redirect
from .forms import LoginForm, CourseForm, UserForm
from django.contrib.auth import login as slogin, authenticate, logout as slogout
from .models import CustomUser, Course, Enrolls, Sections, Exam_grades, Homework_grades
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict


# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = "please check forms！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                slogin(request, user)
                print(user.username + " login success!")
                return redirect('/index')
            else:
                message = "loging error"
                return render(request, 'login.html', locals())
        return render(request, 'login.html', locals())
    else:
        login_form = LoginForm()
        return render(request, 'login.html', locals())


def logout(request):
    slogout(request)
    return redirect('login')


def manage_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_id = course_form.cleaned_data['course']
            name = course_form.cleaned_data['name']
            description = course_form.cleaned_data['dec']
            sec_no = course_form.cleaned_data['sec_no']
            sec_type = course_form.cleaned_data['sec_type']
            course = Course.objects.get(course_id=course_id)
            if course:
                Course.objects.filter(course_id=course_id).update(course_name=name, course_description=description,
                                                                  section=Sections.objects.filter(sec_no2=sec_no,
                                                                                                  section_type=sec_type).first())
            else:
                Course.objects.create(course_id=course_id, course_name=name, course_description=description,
                                      section=Sections.objects.filter(sec_no2=sec_no,
                                                                      section_type=sec_type).first())
    elif request.method == 'GET':
        course_id = request.GET.get('delete_id', None)
        if course_id:
            print(course_id)
            # Course.objects.filter(course_id=course_id).delete()
    redirect('index')


def manage_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            role = user_form.cleaned_data['role']
            name = user_form.cleaned_data['name']
            u = CustomUser.objects.filter(username=username).all().values()
            if u:
                CustomUser.objects.filter(username=username).update(email=email, password=password, role=role,
                                                                    first_name=name)
            else:
                CustomUser.objects.create(username=username, email=email, password=password, role=role, first_name=name)


def enroll_student(request):
    if request.method == 'GET':
        email = request.GET.get('student_email', None)
        course_id = request.GET.get('course', None)
        sec_no = Course.objects.filter(course_id=course_id).first().section
        if Enrolls.objects.filter(student_email_id=email, course_id_id=course_id).count() == 0:
            en = Enrolls.objects.create(student_email=CustomUser.objects.filter(email=email).first(),
                                        course_id_id=course_id,
                                        section_no=sec_no)
            res = model_to_dict(en)
        else:
            res = {'res': 'already enrolled'}
        return JsonResponse(res)


def assign_prof(request):
    if request.method == 'GET':
        email = request.GET.get('prof_email', None)
        course_id = request.GET.get('course', None)
        # sec_no = Sections.objects.filter(course_id=course_id).all()
        cour = Course.objects.filter(course_id=course_id).update(course_prof=email)
        res = model_to_dict(cour)
        return JsonResponse(res)


def grade_change(request):
    if request.method == 'POST':
        email_c = request.POST.get('name', None)
        email, c_id = email_c.split('_')
        value = request.POST.get('value', None)

        Exam_grades.objects.filter(course_id=c_id, student_email=email).update(grade=value)
        print('Exam_grades update to ' + value)
        return HttpResponse('ok')


def hw_change(request):
    if request.method == 'POST':
        email_c = request.POST.get('name', None)
        email, c_id = email_c.split('_')
        value = request.POST.get('value', None)

        Homework_grades.objects.filter(course_id=c_id, student_email=email).update(grade=value)
        print('Homework_grades update to' + value)
        return HttpResponse('ok')


def create_hw(request):
    if request.method == 'GET':
        email = request.GET.get('prof_email', None)
        course_id = request.GET.get('course', None)

        print('create_hw ' + value)
        return HttpResponse('ok')



def create_exam(request):
    if request.method == 'GET':
        email = request.GET.get('prof_email', None)
        course_id = request.GET.get('course', None)

        print('create_exam ' + value)
        return HttpResponse('ok')


def create_hw_grade(request):
    pass


def create_exam_grade(request):
    pass
