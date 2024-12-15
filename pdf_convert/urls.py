from django.urls import path
from . import views
urlpatterns = [
    path('pdf_report_create/', views.pdf_report_create, name='pdf_report_create'),
    ]