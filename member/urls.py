from django.urls import path
from . import views
urlpatterns = [
    path('member_home/', views.member_home, name='member_home'),
    path('profile/', views.profile, name='profile'),
    path('member_report/', views.member_report, name='member_report'),
]