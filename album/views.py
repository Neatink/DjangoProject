from django.views.generic import ListView, DetailView, TemplateView, DeleteView, FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Subject, Student, Teacher, Class
from .forms import SubjectForm, TeacherForm, StudentForm, ClassForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomLoginForm,CustomRegisterForm


class CustomLoginView(FormView):
    template_name = 'login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Невірний логін або пароль")
            return self.form_invalid(form)


class profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
        
class CustomRegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None,"Аккаунт з таким логiном чи поштою вже є")
        return super().form_invalid(form)
    

class home(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    
class teachers(LoginRequiredMixin,ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'


class students(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'students.html'
    context_object_name = 'students'


class subjects(LoginRequiredMixin,ListView):
    model = Subject
    template_name = 'subjects.html'
    context_object_name = 'subjects'


class classes(LoginRequiredMixin,ListView):
    model = Class
    template_name = 'classes.html'
    context_object_name = 'classes'


class details_subjects(LoginRequiredMixin,DetailView):
    model = Subject
    template_name = 'details_subjects.html'
    context_object_name = 'subject'


class details_teachers(LoginRequiredMixin,DetailView):
    model = Teacher
    template_name = 'details_teachers.html'
    context_object_name = 'teachers'


class details_classes(LoginRequiredMixin,DetailView):
    model = Class
    template_name = 'details_classes.html'
    context_object_name = 'classes'


class details_students(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'details_students.html'
    context_object_name = 'students'


class delete_subject(LoginRequiredMixin,DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class delete_teachers(LoginRequiredMixin,DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class delete_students(LoginRequiredMixin,DeleteView):
    model = Student
    success_url = reverse_lazy('students')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class delete_classes(LoginRequiredMixin,DeleteView):
    model = Class
    success_url = reverse_lazy('classes')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class add_subject(LoginRequiredMixin,FormView):
    template_name = 'add_subject.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects')

    def form_valid(self, form):
        Subject.objects.create(
            name=form.cleaned_data['name'],
            count_teachers=form.cleaned_data['count_teachers']
        )
        return super().form_valid(form)


class add_teachers(LoginRequiredMixin,FormView):
    template_name = 'add_teacher.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers')

    def form_valid(self, form):
        Teacher.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            subjects_count=form.cleaned_data['subjects_count'],
            subject=form.cleaned_data['subject']
        )
        return super().form_valid(form)


class add_students(LoginRequiredMixin,FormView):
    template_name = 'add_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        Student.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            mail=form.cleaned_data['mail'],
            birthday=form.cleaned_data['birthday'],
            clas=form.cleaned_data['clas_id']
        )
        return super().form_valid(form)


class add_classes(LoginRequiredMixin,FormView):
    template_name = 'add_classes.html'
    form_class = ClassForm
    success_url = reverse_lazy('classes')

    def form_valid(self, form):
        Class.objects.create(
            name=form.cleaned_data['name']
        )
        return super().form_valid(form)


class edit_subject(LoginRequiredMixin,FormView):
    template_name = 'edit_subject.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects')

    def get_initial(self):
        subject = Subject.objects.get(pk=self.kwargs['pk'])
        return {
            'name': subject.name,
            'count_teachers': subject.count_teachers
        }

    def form_valid(self, form):
        subject = Subject.objects.get(pk=self.kwargs['pk'])
        subject.name = form.cleaned_data['name']
        subject.count_teachers = form.cleaned_data['count_teachers']
        subject.save()
        return super().form_valid(form)


class edit_teachers(LoginRequiredMixin,FormView):
    template_name = 'edit_teacher.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers')

    def get_initial(self):
        teacher = Teacher.objects.get(pk=self.kwargs['pk'])
        return {
            'name': teacher.name,
            'surname': teacher.surname,
            'subjects_count': teacher.subjects_count,
            'subject': teacher.subject
        }

    def form_valid(self, form):
        teacher = Teacher.objects.get(pk=self.kwargs['pk'])
        teacher.name = form.cleaned_data['name']
        teacher.surname = form.cleaned_data['surname']
        teacher.subjects_count = form.cleaned_data['subjects_count']
        teacher.subject = form.cleaned_data['subject']
        teacher.save()
        return super().form_valid(form)


class edit_students(LoginRequiredMixin,FormView):
    template_name = 'edit_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('students')

    def get_initial(self):
        student = Student.objects.get(pk=self.kwargs['pk'])
        return {
            'name': student.name,
            'surname': student.surname,
            'mail': student.mail,
            'birthday': student.birthday,
            'clas_id': student.clas
            }

    def form_valid(self, form):
        student = Student.objects.get(pk=self.kwargs['pk'])
        student.name = form.cleaned_data['name']
        student.surname = form.cleaned_data['surname']
        student.mail = form.cleaned_data['mail']
        student.birthday = form.cleaned_data['birthday']
        student.clas = form.cleaned_data['clas_id']
        student.save()
        return super().form_valid(form)


class edit_classes(LoginRequiredMixin,FormView):
    template_name = 'edit_classes.html'
    form_class = ClassForm
    success_url = reverse_lazy('classes')

    def get_initial(self):
        class_name = Class.objects.get(pk=self.kwargs['pk'])
        return {
            'name': class_name.name
        }

    def form_valid(self, form):
        class_name = Class.objects.get(pk=self.kwargs['pk'])
        class_name.name = form.cleaned_data['name']
        class_name.save()
        return super().form_valid(form)