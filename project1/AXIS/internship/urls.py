from internship import views
from django.urls import path
urlpatterns = [
    path('home/', views.Home,name='Home'),
    path('register/',views.Registration,name='Registration'),
    path('login/',views.login,name='login'),
    path('admin/',views.admin,name='admin'),
    path('adminuser/',views.viewusers,name='viewusers'),
    path('userhome/',views.userhomepage,name='userhome'),
    path('usertimings/',views.adminuser,name='usertimings')]
