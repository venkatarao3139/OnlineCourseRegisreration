from django.shortcuts import render,redirect
from django.contrib import messages
from Application.models import StudentRegister,ScheduleNewClass,EnroleCoueses
from django.views.generic import UpdateView,DeleteView,ListView,CreateView,View
def homepage(request):
    return render(request,"home_page.html")

def FAQs(request):
    return render(request,"facs.html")

def contact(request):
    return render(request,"contact.html")

def adminpage(request):
    return render(request,"admin_page.html")

def studentpage(request):
    return render(request,"student_page.html")

def admin_home_page(request):
    return render(request,"admin_home_page.html")

def adminhomepage(request):
        user = request.POST.get("us")
        pswrd = request.POST.get("ps")
        if user=="venkat" and pswrd=="venky3139":
            return redirect('admin_home_page')
        else:
            return render(request,'admin_page.html',{"data":"INVALID ADMIN DETAILS"})

def register_page(request):
    return render(request,"student_register.html")

def Student_login(request):
    return render(request,"Student_login.html")

def savestdent(request):
    name = request.POST.get("t1")
    cont = request.POST.get("t2")
    email = request.POST.get("t3")
    usr = request.POST.get("t4")
    psr = request.POST.get("t5")
    StudentRegister(Name=name,contact=cont,email=email,user=usr,pas=psr).save()
    messages.success(request," Student Data is Saved")
    return redirect('register')

def newcource(request):
    return render(request,"newc_ource.html")

def svaecourse(request):
    name = request.POST.get("c1")
    fclty = request.POST.get("c2")
    edate = request.POST.get("c3")
    etime = request.POST.get("c4")
    fee = request.POST.get("c5")
    dur = request.POST.get("c6")
    ScheduleNewClass(cname=name,Faculty=fclty,Date=edate,Time=etime,Fee=fee,Duration=dur).save()
    messages.success(request,"New course is Saved ")
    return redirect('newcource')

def courseslist(request):
    coureses = ScheduleNewClass.objects.all()
    return render(request,"list_of_courses.html",{"data":coureses})

def studentlogin_home(request):
    id = request.POST.get("use")
    word = request.POST.get("psw")
    std = StudentRegister.objects.get(user=id, pas=word)
    try:
        if id == std.user and word == std.pas:
            return render(request,"student_home_page.html",{"data":std})
    except StudentRegister.DoesNotExist:
            messages.error(request,"INVALID STUDENT DETAILS")
            return redirect('Studentlogin')
def student_home(request):
    return render(request,"student_home_page.html")
#===================class based views====================
class Updatecourse(UpdateView):
    template_name = "update_course.html"
    model = ScheduleNewClass
    fields = "__all__"
    success_url = "/courseslist/"

class Remove_course(DeleteView):
    template_name = "Delete_course.html"
    model = ScheduleNewClass
    fields = "__all__"
    success_url = "/courseslist/"

def student_list(request):
    stl = StudentRegister.objects.all()
    return render(request,"studentlist.html",{"sdata":stl})

class course_enroll(CreateView):
    template_name = "course_enroll.html"
    model = EnroleCoueses
    fields = "__all__"
    success_url = "/course_enroll_list/"

class course_enroll_list(ListView):
    template_name = "enroled_list.html"
    model = EnroleCoueses

class update_enrole(UpdateView):
    template_name = "update_enrole_list.html"
    model = EnroleCoueses
    fields = "__all__"
    success_url = "/course_enroll_list/"


class delete_enrole(DeleteView):
    template_name = 'Delete_enrole_list.html'
    model = EnroleCoueses
    fields = "__all__"
    success_url = "/course_enroll_list/"


