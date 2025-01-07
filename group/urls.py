from django.urls import path
from . import views
urlpatterns = [
    path('group_home/', views.group_home, name='group_home' ),
    path('collection/', views.collection, name='collection'),
    path('members/', views.members, name='members'),
    path('profile/', views.profile, name='profile'),
    path('loan/', views.loan, name='loan'),
    path('report/', views.report, name='report'),
    path('group_loan/', views.group_loan, name='group_loan'),
    path('bank_loan/', views.bank_loan, name='bank_loan'),
    path('sangh_loan/', views.sangh_loan, name='sangh_loan'),
    path('edit_collection/', views.edit_collection, name='edit_collection'),
    path('edit_member_collection/<int:member_id>', views.edit_member_collection, name='edit_member_collection'),
]
