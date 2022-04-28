from django.shortcuts import render, HttpResponse, redirect
from django.contrib.sessions.models import Session
from .models import Teachers
from .models import Assignment
from django.contrib import messages
from .models import StudyMaterials
from .models import Classes
from .models import Exams
from .models import Photos
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def course_grid_2(request):
    return render(request, 'course-grid-2.html')

def course_grid_3(request):
    return render(request, 'course-grid-3.html')

def course_grid_4(request):
    return render(request, 'course-grid-4.html')

def teachers(request):
    return render(request, 'teachers.html')

def sign_in(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        pswd=request.POST.get('pswd')
        if Teachers.objects.filter(uname=username,pswd=pswd).exists():
            b=Teachers.objects.get(uname=username,pswd=pswd)
            request.session['username']=b.uname
            request.session['uid']=b.id
            c=request.session['uid']
            d=Teachers.objects.get(id=c)
            return render(request, 'teachers_official.html', {'prof':d})
        else:
            return HttpResponse('Invalid Username or Password')

def teachers_official(request):
    c=request.session['uid']
    d=Teachers.objects.get(id=c)
    return render(request, 'teachers_official.html', {'prof':d})
    

# def sign_out(request):
#     for s in Session.objects.all():
#         data=s.get_decoded()
#         if data.get('_auth_user_id', None) == 'uid':
#             s.delete()
#             return render(request, 'teachers.html')

def view_profile(request):
    c=request.session['uid']
    d=Teachers.objects.get(id=c)
    return render(request, 'teacher_profile.html', {'prof':d})

def profile_update(request):
    if request.method=="POST":
        e=request.session["uid"]
        f=Teachers.objects.get(id=e)
        f.name = request.POST.get("name")
        f.email = request.POST.get("email")
        f.phno = request.POST.get("phno")
        f.pswd = request.POST.get("pswd")
        f.cpswd = request.POST.get("cpswd")
        if request.POST['pswd'] != request.POST['cpswd']:
            messages.error(request, "Passwords isn't matches")
            return HttpResponse("Passwords isn't matches")
        f.save()
        c=request.session['uid']
        d=Teachers.objects.get(id=c)
        return render(request, 'teacher_profile.html', {'prof':d})

def assignment_save(request):
    if request.method=='POST':
        a=Assignment()
        a.sem=request.POST.get('sem')
        a.course=request.POST.get('course')
        a.topic=request.POST.get('ass_topic')
        a.sub_date=request.POST.get('sub_date')
        a.save()
        return HttpResponse('Assignment created successfully')

def materials_save(request):
    if request.method=='POST':
        a=StudyMaterials()
        a.sem=request.POST.get('sem')
        a.course=request.POST.get('course')
        a.material=request.POST.get('material')
        a.save()
        return HttpResponse('Material uploaded successfully')

def class_save(request):
    if request.method=='POST':
        a=Classes()
        a.sem=request.POST.get('sem')
        a.course=request.POST.get('course')
        a.class_link=request.POST.get('class_link')
        a.date=request.POST.get('date')
        a.start_time=request.POST.get('start_time')
        a.end_time=request.POST.get('end_time')
        a.save()
        return HttpResponse('Class link uploaded successfully')

def qp_save(request):
    if request.method=='POST':
        a=Exams()
        a.sem=request.POST.get('sem')
        a.course=request.POST.get('course')
        a.date=request.POST.get('date')
        a.start_time=request.POST.get('start_time')
        a.end_time=request.POST.get('end_time')
        a.qp=request.POST.get('qp')
        a.save()
        return HttpResponse('Exam infos and question paper uploaded successfully')

def photo_save(request):
    a=Photos()
    a.title=request.POST.get('title')
    a.photo=request.POST.get('photo')
    a.descr=request.POST.get('descr')
    a.save()
    return HttpResponse('Photo uploaded successfully')


def sign_out(request):
    del request.session['uid']
    del request.session['username']
    return render(request, 'teachers.html')