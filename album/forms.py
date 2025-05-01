from django import forms
from .models import Subject, Student, Class
from django.contrib.auth.models import User

class CustomLoginForm(forms.Form):
    type='password'
    username = forms.CharField(
        required=True,max_length=50,widget=forms.TextInput(attrs={
        'placeholder':'Логiн',
        }))
    password = forms.CharField(
        required=True,widget=forms.PasswordInput(attrs={
            'placeholder':'Пароль',
        }))
    
    
class CustomRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,required=True,widget=forms.TextInput(attrs={
        'placeholder':'Логiн',
        }))
    email = forms.CharField(
        required=True,widget=forms.EmailInput(attrs={
            'placeholder': 'Електронна пошта'
        }))
    password = forms.CharField(
        required=True,widget=forms.PasswordInput(attrs={
            'placeholder':'Пароль:'
        }))
    password2 = forms.CharField(
        required=True,label = 'Confirm password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пiдтвердити пароль'
        }))
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають")
        return password2
    
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Аккаунт з таким логiном чи поштою вже є")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Аккаунт з таким логiном чи поштою вже є")
        return email

class SubjectForm(forms.Form):
    name = forms.CharField(
        label="Назва предмета:",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву предмета:',
            'autofocus': 'autofocus',
        }),
        help_text="Введіть унікальну назву предмета"
    )
    count_teachers = forms.IntegerField(
        label="Кількість вчителiв",
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть кількість вчителiв'
        }),
        help_text="Введіть кількість вчителiв для предмета(необовязково)"
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if Subject.objects.filter(name=name).exists():
            raise forms.ValidationError("Предмет з такою назвою вже є")
        return name


class TeacherForm(forms.Form):
    name = forms.CharField(
        label="Імя вчителя",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть імя вчителя:',
            'autofocus': 'autofocus',
        }),
        help_text="Введіть імя вчителя"
    )
    surname = forms.CharField(
        label="Прізвище вчителя",
        max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть прізвище вчителя:'
        }),
        help_text="Введіть прізвище вчителя"
    )
    subjects_count = forms.IntegerField(
        label="Кількість предметів",
        required=True,
        initial=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть кількість предметів:'
        }),
        help_text="Укажіть кількість предметів які веде вчитель"
    )
    subject = forms.ModelChoiceField(
        label="Предмет",
        queryset=Subject.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        help_text="Оберіть предмет який веде вчитель (необовязково)"
    )


class StudentForm(forms.Form):
    name = forms.CharField(
        label="Імя студента",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть імя студента:',
            'autofocus': 'autofocus'
        }),
        help_text="Введіть імя студента"
    )
    surname = forms.CharField(
        label="Прізвище студента",
        max_length=40,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть прізвище студента:'
        }),
        help_text="Введіть прізвище студента"
    )
    mail = forms.EmailField(
        label="Email",
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть пошту студента:'
        }),
        help_text="Введіть унікальну пошту студента"
    )
    birthday = forms.DateField(
        label="Дата народження",
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Оберіть дату народження:'
        }),
        help_text="Оберіть дату народження студента"
    )
    clas_id = forms.ModelChoiceField(
        label="Клас",
        queryset=Class.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        help_text="Оберіть клас в якому вчиться студент"
    )

    def clean_mail(self):
        mail = self.cleaned_data['mail']
        if Student.objects.filter(mail=mail).exists():
            raise forms.ValidationError("Студент з такою поштою вже є")
        return mail


class ClassForm(forms.Form):
    name = forms.CharField(
        label="Назва класу",
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву класу:',
            'autofocus': 'autofocus',
        }),
        help_text="Введіть унікальну назву класу"
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if Class.objects.filter(name=name).exists():
            raise forms.ValidationError("Клас з такою назвою вже є")
        return name