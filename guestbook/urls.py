from django.urls import path
from guestbook import views

urlpatterns = [
    path('',views.home,name='home'),
    path('list',views.list,name='list'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('write', views.write, name='write'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
]