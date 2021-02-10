from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.welcome,name='first_page'),
    path('home/', views.home,name='home'),
    path('tasks/',views.tasks,name='tasks'),
    path('matrix/',views.matrix,name='matrix'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/',views.test,name='test'),
    path('matrix/',views.matrix,name='matrix'),
    path('accounts/register/',views.register,name='register'),
    path('accounts/login/', views.login, name = 'login'),
]

'''
Automatically includes:

accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']

'''