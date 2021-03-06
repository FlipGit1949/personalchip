from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),

    path('', views.homePage, name='home'),
    path('project/<str:pk>/', views.projectPage, name='project'),
    path('add-project/', views.addProject, name='add-project'),
    path('edit-project/<str:pk>/', views.editProject, name='edit-project'),
    path('inbox/', views.inboxPage, name='inbox'),
    path('message/<str:pk>/', views.messagePage, name='message'),
    path('add-skill/', views.addSkill, name='add-skill'),
    path('video/', views.index, name='index'),
    path('youtube/', views.youtube, name='youtube'),
]


