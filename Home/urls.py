from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    # path('about/', views.about),
    # path('service/', views.service),
    # path('midi/',views.midi),
    path ('add/', views.add_student,name = 'add'), 
    path ('update/<int:id>/',views.update_student, name ='update'),
    path ('delete/<int:id>/',views.delete_student, name ='delete')
]
