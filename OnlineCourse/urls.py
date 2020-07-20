"""OnlineCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Application import views

urlpatterns = [
    #================== main admin url==============
    path('admin/', admin.site.urls),
    # ================ Admin and Course urls ====================================
    path('',views.homepage,name='home'),
    path('FAQs/',views.FAQs,name='FAQs'),
    path('contact/',views.contact,name='contact'),
    path('admin1/',views.adminpage,name='admin1'),
    path('adminpage/',views.adminhomepage,name='adminpage'),
    path('admin_home_page/', views.admin_home_page, name='admin_home_page'),
    path('newcource/',views.newcource,name='newcource'),
    path('svaecourse/',views.svaecourse,name='svaecourse'),
    path('courseslist/',views.courseslist,name='courseslist'),
    path('updatet<int:pk>/',views.Updatecourse.as_view(),name='update'),
    path('remove<int:pk>/',views.Remove_course.as_view(),name='remove'),
    # ================ student urls =============================================
    path('student/', views.studentpage, name='student'),
    path('register/',views.register_page,name='register'),
    path('savestdent/', views.savestdent, name='savestdent'),
    path('Studentlogin/', views.Student_login, name='Studentlogin'),
    path('studentloginhome/',views.studentlogin_home,name='studentloginhome'),
    path('student_home/', views.student_home, name='student_home'),
    path('students_list/',views.student_list,name='students_list'),
    #======================= Course enrollment urls ==================================
    path('course_enroll/',views.course_enroll.as_view(),name='course_enroll'),
    path('course_enroll_list/',views.course_enroll_list.as_view(),name='course_enroll_list'),
    path('update_enrole<int:pk>/',views.update_enrole.as_view(),name='update_enrole'),
    path('delete_enrole<int:pk>/',views.delete_enrole.as_view(),name='delete_enrole')
]