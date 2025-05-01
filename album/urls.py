from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('students/', views.students.as_view(), name='students'),
    path('teachers/', views.teachers.as_view(), name='teachers'),
    path('subjects/', views.subjects.as_view(), name='subjects'),
    path('classes/', views.classes.as_view(), name='classes'),
    path('subjects/details_subjects/<int:pk>', views.details_subjects.as_view(), name='details_subjects'),
    path('teachers/details_teachers/<int:pk>', views.details_teachers.as_view(), name='details_teachers'),
    path('students/details_students/<int:pk>', views.details_students.as_view(), name='details_students'),
    path('classes/details_classes/<int:pk>', views.details_classes.as_view(), name='details_classes'),
    path('home/', views.home.as_view(), name='home'),
    path('subjects/add/', views.add_subject.as_view(), name='add_subject'),
    path('teachers/add/', views.add_teachers.as_view(), name='add_teachers'),
    path('students/add/', views.add_students.as_view(), name='add_students'),
    path('classes/add/', views.add_classes.as_view(), name='add_classes'),
    path('subjects/edit/<int:pk>', views.edit_subject.as_view(), name='edit_subject'),
    path('teachers/edit/<int:pk>', views.edit_teachers.as_view(), name='edit_teachers'),
    path('students/edit/<int:pk>', views.edit_students.as_view(), name='edit_students'),
    path('classes/edit/<int:pk>', views.edit_classes.as_view(), name='edit_classes'),
    path('subjects/delete/<int:pk>', views.delete_subject.as_view(), name='delete_subject'),
    path('teachers/delete/<int:pk>', views.delete_teachers.as_view(), name='delete_teachers'),
    path('students/delete/<int:pk>', views.delete_students.as_view(), name='delete_students'),
    path('classes/delete/<int:pk>', views.delete_classes.as_view(), name='delete_classes'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',subject_template_name='texts/1.txt',html_email_template_name='texts/2.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
