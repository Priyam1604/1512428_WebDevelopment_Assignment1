
from msilib.schema import ListView


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage

from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


from gradebook.forms import coursForm_add, courseForm_upd, semForm_add, semForm_upd, lecForm_add, \
    lecForm_upd, classForm_upd, classForm_add, stuFoorm_add, stuForm_upd, lecForm_assign, \
    stuForm_Enroll
from gradebook.models import Course, Semester, Lecturer, Class, Student, StudentEnrollment

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home - GradeBook'
        return context

class course_list(ListView):
    model = Course
    template_name = 'Courses/list_courses.html'


class course_add(CreateView):
    model = Course
    form_class = coursForm_add
    template_name = "Courses/newCourAdd.html"


class course_upd(UpdateView):
    model = Course
    form_class = courseForm_upd
    template_name = "Courses/course_upd.html "


class course_del(DeleteView):
    model = Course
    template_name = 'Courses/courseRem.html'
    success_url = reverse_lazy('list_course')



class sem_list(ListView):
    model = Semester
    template_name = 'Semester/semList.html'


class sem_add(CreateView):
    model = Semester
    form_class = semForm_add
    template_name = "Semester/semCreateNew.html"


class sem_upd(UpdateView):
    model = Semester
    form_class = semForm_upd
    template_name = "Semester/sem_upd.html "


class sem_remov(DeleteView):
    model = Semester
    template_name = 'Semester/sem_remov.html'
    success_url = reverse_lazy('list_semester')


class lec_list(ListView):
    model = Lecturer
    template_name = 'Lecturer/lectulist.html'



@login_required
def create_lecturer(request):
    staffID = request.POST.get('staffID')
    first_Name = request.POST.get('first_Name')
    last_Name = request.POST.get('last_Name')
    email = request.POST.get('email')
    course = request.POST.get('course')
    dateOfBirth= request.POST.get('dateOfBirth')

    message = ''
    try:
        user = User.objects.create_user(username=first_Name.lower())
        user.set_password(first_Name.lower())
        user.first_name = first_Name
        user.last_name = last_Name
        user.email = email
        lecturer_group = Group.objects.get(name='Lecturer')
        user.groups.add(lecturer_group)
        user.save()
        lecturer = Lecturer(user=user, course=course, staffID=staffID, first_Name=first_Name, last_Name=last_Name,
                            email=email,
                            dateOfBirth=dateOfBirth)
        lecturer.save()
        message = 'Lecturer ' + first_Name + ' ' + last_Name + ' created!'
    except Exception as e:

        message = 'Lecturer creation failed!' + str(e)

    context = {'message': message}
    return render(request, 'Lecturer/addLec.html', context)

@login_required
def create_lecturer_form(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'Lecturer/addLecForm.html', context)



class lec_upd(UpdateView):
    model = Lecturer
    form_class = lecForm_upd
    template_name = "Lecturer/changeLecDetails.html "


class lec_remov(DeleteView):
    model = Lecturer
    template_name = 'Lecturer/removeLecForm.html'
    success_url = reverse_lazy('list_lecturer')

class class_list(ListView):
    model = Class
    template_name = 'Classes/classList.html'


class class_add(CreateView):
    model = Class
    form_class = classForm_add
    template_name = "Classes/newClassCreate.html"


class class_upd(UpdateView):
    model = Class
    form_class = classForm_upd
    template_name = "Classes/class_upd.html "


class class_delet(DeleteView):
    model = Class
    template_name = 'Classes/class_rem.html'
    success_url = reverse_lazy('list_classes')

class assignLecturer(UpdateView):
    model = Class
    form_class = lecForm_assign
    template_name = 'Classes/lec_Allocate.html'


class listStudents(ListView):
        model = Student
        template_name = 'Students/stuList.html'


@login_required
def create_student(request):
    studentID = request.POST.get('studentID')
    first_Name = request.POST.get('first_Name')
    last_Name = request.POST.get('last_Name')
    email = request.POST.get('email')
    dateOfBirth = request.POST.get('dateOfBirth')

    message = ''
    try:
        user = User.objects.create_user(username=first_Name.lower())
        user.set_password(first_Name.lower())
        user.first_name = first_Name
        user.last_name = last_Name
        user.email = email
        student_group = Group.objects.get(name='Student')
        user.groups.add(student_group)
        user.save()
        student = Student(user=user, studentID=studentID, first_Name=first_Name, last_Name=last_Name, email=email,
                          dateOfBirth=dateOfBirth)
        student.save()
        message = 'Student ' + first_Name + ' ' + last_Name + ' created!'
    except Exception as e :

        message = 'Student creation failed!' + str(e) + first_Name.lower()

    context = {'message': message}
    return render(request, 'Students/stu_Add.html', context)


@login_required
def create_student_form(request):
    return render(request, 'Students/newstuForm_create.html', None)



class Update_Stu(UpdateView):
        model = Student
        form_class = stuForm_upd
        template_name = "Students/stu_upd.html "

class Delete_Stu(DeleteView):
        model = Student
        template_name = 'Students/stu_remov.html'
        success_url = reverse_lazy('list_students')


class list_StuEnroll(ListView):
    model = StudentEnrollment
    template_name = 'Students/enrolment/studntList.html'


class Stu_Enroll(CreateView):
    model = StudentEnrollment
    form_class = stuForm_Enroll
    template_name = 'Students/enrolment/newStuEnroll.html'

class del_Stu(DeleteView):
    model = StudentEnrollment
    template_name = 'Students/enrolment/studntRemov.html'
    success_url = reverse_lazy('list_student')

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        import pandas as pd
        excel_data= pd.read_excel(myfile)
        data = pd.DataFrame(excel_data)
        ids = data["ID"].tolist()
        firstnames = data["Firstname"].tolist()
        lastnames= data["Lastname"].tolist()
        emails = data["Email"].tolist()
        dobs= data["DOB"].tolist()
        courses = data["Course"].tolist()
        classes = data["Class"].tolist()
        i =0
        while i < len(ids):
            id = ids[i]
            firstname = firstnames[i]
            lastname = lastnames[i]
            email = emails[i]
            dob = dobs[i]
            course = courses[i]
            classes = classes[i]
            enrolTime = timezone.now()

            user = User.objects.create_user(username=firstname.lower())
            user.set_password(firstname.lower())
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)
            user.save()
            student = Student(user=user, studentID=id, first_Name=firstname, last_Name=lastname, email=email,
                              dateOfBirth=dob)
            # class1 = Class.objects.get(number=classs)
            student.save()
            # studentEnrolment = StudentEnrollment(student_id=student,class_id=class1,enrollTime=enrolTime)
            # studentEnrolment.save

            i= i+1


        return render(request, 'Students/uploadFileForm.html', {
            'uploaded_file_url':uploaded_file_url
        })
    return render(request, 'Students/uploadFileForm.html', None)



class GradeBookSemesterView(ListView):
    model = Semester
    template_name = 'gradebook/Listofsemes.html'

@login_required
def gradebook_class(request, pk):
    classes = Class.objects.filter(semester_id=pk)
    studentEnrolment = StudentEnrollment.objects.all()
    context = {
        "classes": classes,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/Listofclasses.html', context)


@login_required
def gradebook_student_list(request, pk):
    studentEnrolment = StudentEnrollment.objects.filter(class_id_id=pk)
    current_class = Class.objects.get(id=pk)
    context = {
        "semester_id": current_class.semester.id,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/studEnrll.html', context)


@login_required
def gradebook_grade_student(request):
    id = request.POST.get("id")
    grade = request.POST.get("grade")
    try:
        studentEnrolment = StudentEnrollment.objects.get(id=id)
        studentEnrolment.grade = grade
        studentEnrolment.gradeTime = timezone.now()
        studentEnrolment.save()
        senderemail= 'singhh59@myunitec.ac.nz'
        send_mail('Class Grade Notification', 'Your grade has been published! \nPlease check in gradebook :).',
                   senderemail, [studentEnrolment.student_id.email], fail_silently=False)
        message = "Student " + studentEnrolment.student_id.first_Name + " graded successfully!"
    except Exception as e:
        message = "Could not grade " + studentEnrolment.student_id.first_Name + "!" + str(e)

    context = {
        "message": message,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/studentGrades.html', context)


@login_required
def gradebook_grade_student_form(request, pk):
    studentEnrolment = StudentEnrollment.objects.get(id=pk)
    context = {"studentEnrolment": studentEnrolment}
    return render(request, 'gradebook/studentGradelist.html', context)
