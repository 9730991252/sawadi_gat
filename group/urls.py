from django.urls import path
from . import views
urlpatterns = [
    path('group_home/', views.group_home, name='group_home' ),
    path('collection/', views.collection, name='collection'),
    path('members/', views.members, name='members'),
    path('profile/', views.profile, name='profile'),
    path('loan/', views.loan, name='loan'),
    path('report/', views.report, name='report'),

]
