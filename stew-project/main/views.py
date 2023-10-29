from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from .forms import CourseForm
from .models import Course, Enrollment

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def faq(request):
    return render(request, 'main/faq.html')

@login_required
def courses(request):
    is_teacher = False
    if (request.user.status != 'student'):
        is_teacher = True
    enrolled_courses = Course.objects.filter(students=request.user)
    taught_courses = Course.objects.filter(instructor=request.user)
    
    return render(request, 'main/courses.html', {'is_teacher':is_teacher, 'enrolled_courses':enrolled_courses, 'taught_courses':taught_courses})

@login_required
def logoutaccount(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def loginaccount(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'GET':
        return render(request, 'main/loginaccount.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginaccount.html', {'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('courses')

def signupaccount(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'GET':
        return render(request, 'main/signupaccount.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user_status = 'student'
                if (request.POST['my_role'] == 'instructor'):
                    user_status = 'teacher'
                
                user = CustomUser.objects.create_user(
                    request.POST['username'], 
                    password=request.POST['password1'], 
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    status=user_status)
                user.save()
                login(request, user)
                return redirect('courses')
            except IntegrityError:
                return render(request, 'main/signupaccount.html', {'error':'That username has already been taken. Please choose a new username.'})
                
        else:
            # The passwords did not match
            return render(request, 'main/signupaccount.html', {'error':'Passwords did not match'})
        
@login_required
def createcourse(request):
    if request.method == 'GET':
        return render(request, 'main/createcourse.html', {'form':CourseForm()})
    else:
        try:
            form = CourseForm(request.POST)
            new_course = form.save(commit=False)
            new_course.instructor = request.user
            new_course.save()
            return redirect('courses')
        except ValueError:
            if (len(request.POST['join_code']) <= 100 and len(request.POST['name']) <= 100):
                return render(request, 'main/createcourse.html', {'form':CourseForm(), 'error':'That Course Code is taken. Please choose another.'})
            else:
                return render(request, 'main/createcourse.html', {'form':CourseForm(), 'error':'Bad data entered. Please try again.'})

@login_required
def coursehome(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    tas = course.tas.all
    #Need the .all because the ManyToMany is not iterable
    
    if (course.tas.filter(pk=request.user.id)):
        print('User is a TA')
    else:
        print('User is not a TA')
    
    if (course.students.filter(pk=request.user.id)):
        print('User is a student')
    else:
        print('User is not a student')
        
    if (course.instructor.id == request.user.id):
        print('User is the instructor')
    else:
        print('User is not the instructor')
    
    if request.method == 'GET':
        return render(request, 'main/coursehome.html', {'course':course, 'tas':tas})

@login_required
def userprofile(request, user_pk):
    userprofile = get_object_or_404(CustomUser, pk=user_pk)
    
    if request.method == 'GET':
        return render(request, 'main/userprofile.html', {'userprofile':userprofile})
    
@login_required
def joincourse(request):
    if request.method == 'GET':
        return render(request, 'main/joincourse.html')
    else:
        try:
            enroll = Enrollment(course=get_object_or_404(Course, join_code=request.POST['join_code']), student=request.user)
            enroll.save()
            return redirect('courses')
        except:
            return render(request, 'main/joincourse.html', {'error':'That Course cannot be found.'})

            