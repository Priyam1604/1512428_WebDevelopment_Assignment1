"""assign1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from gradebook.views import course_list, HomePageView, course_add, course_upd, course_del, sem_list, \
    sem_add, sem_remov, sem_upd, lec_list, lec_upd, lec_remov, \
    class_list, class_add, class_upd, class_delet, listStudents, Update_Stu, \
    Delete_Stu, assignLecturer, list_StuEnroll, Stu_Enroll, del_Stu, \
    create_student_form, create_student, GradeBookSemesterView, gradebook_class, gradebook_student_list, \
    gradebook_grade_student, gradebook_grade_student_form, create_lecturer_form, create_lecturer, \
     file_upload

urlpatterns = [
 path('admin/', admin.site.urls),

   #For home
    path('',HomePageView.as_view(),name="home"),
   #For Course
    path("listcourse/", course_list.as_view(), name="list_course"),
    path("createcourse/", course_add.as_view(), name="create_course"),
    path('updatecourse/<int:pk>', course_upd.as_view(), name="update_course"),
    path('deletecourse/<int:pk>', course_del.as_view(), name="delete_course"),
    #For Semesters
    path("listsemester/", sem_list.as_view(), name="list_semester"),
    path("createsemester/", sem_add.as_view(), name="create_semester"),
    path('updatesemester/<int:pk>', sem_upd.as_view(), name="update_semester"),
    path('deletesemester/<int:pk>', sem_remov.as_view(), name="delete_semester"),

    #For Lecturers
    path("listlecturer/", lec_list.as_view(), name="list_lecturer"),
    path("createlecturer/",create_lecturer,name="create_lecturer"),
    path("createlecturerform",create_lecturer_form,name="create_lecturer_form"),
    path('updatelecturer/<int:pk>', lec_upd.as_view(), name="update_lecturer"),
    path('deletelecturer/<int:pk>', lec_remov.as_view(), name="delete_lecturer"),

   # For Classes
   path("listclasses/", class_list.as_view(), name="list_classes"),
   path("createclasses/", class_add.as_view(), name="create_classes"),
   path('updateclasses/<int:pk>', class_upd.as_view(), name="update_classes"),
   path('deleteclasses/<int:pk>', class_delet.as_view(), name="delete_classes"),
   path('assignlecturer/<int:pk>',assignLecturer.as_view(),name="assign_lecturer"),

    # For Students
    path("liststudents/", listStudents.as_view(), name="list_students"),
    path("createstudents/", create_student, name="create_students"),
    path("createstudentform",create_student_form,name="create_student_form"),
    path('updatestudents/<int:pk>', Update_Stu.as_view(), name="update_students"),
    path('deletestudents/<int:pk>', Delete_Stu.as_view(), name="delete_students"),
    path('uploadfile/',file_upload,name='upload_file'),

    #For enrolmets
    path('liststudent/', list_StuEnroll.as_view(), name="list_student"),
    path('enrolstudent/', Stu_Enroll.as_view(), name="enrol_student"),
    path("removestudent/<int:pk>", del_Stu.as_view(), name="remove_student"),

#For gradebook
    path('gradebook',GradeBookSemesterView.as_view(),name="semesters_gradebook"),
    path('gradebook/<int:pk>/classes', gradebook_class, name='classes_gradebook'),
    path('gradebook/<int:pk>/students', gradebook_student_list, name='student_list_gradebook'),
    path('gradebook/grade_student', gradebook_grade_student, name='grade_student'),
    path('gradebook/grade_student_form/<int:pk>', gradebook_grade_student_form, name='grade_student_form'),


    #login(/users)
    path('members/',include('django.contrib.auth.urls'))

    ]