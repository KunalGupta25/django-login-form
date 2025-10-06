from django.urls import path
from . import views

urlpatterns = [
    path('doctor/create/', views.doctor_blog_create, name='doctor_blog_create'),
    path('doctor/', views.doctor_blog_list, name='doctor_blog_list'),
    path('patient/', views.patient_blog_list, name='patient_blog_list'),
    path('view/<int:pk>/', views.blog_detail, name='blog_detail'),
]
