from django.urls import path
from guestbook import views

urlpatterns = [
    path('',views.list,name='list'),
    path('write', views.write, name='write'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
]