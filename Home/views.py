from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student
from .forms import StudentCreationForm, UpdateStudentForm
# Create your views here.




def index (request):
    students = Student.objects.all()
    cont={
        'students':students
    }
    return render(request,'Home/index.html',cont)  


# def add_student (request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         roll = request.POST.get('roll')
#         city = request.POST.get('city')
#         student = Student(name=name,roll=roll,city=city)
#         student.save()
#         return HttpResponse("Student Added Successfully")
#     else :
#         return render(request,'Home/add_student.html')


def add_student(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'Home/add_student.html',{'form':form})  
    
# def update_student(request,id):
#     student = Student.objects.get(pk=id)

#     """
#         select * from Student where id = %id
#     """
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         roll = request.POST.get('roll')
#         city = request.POST.get('city')
#         student.name = name
#         student.roll = roll
#         student.city = city
#         student.save()
#         return HttpResponse("Student Updated Successfully")
#     else :
#         return render(request,'Home/add_student.html',{'student':student})  

def update_student(request,id):
    student = Student.objects.get(pk=id)
    form = UpdateStudentForm(instance=student,)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'Home/update.html',{'form':form})   
    
    
def delete_student(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('index')  
    
# def about(request):
    
#     owner={
#         "name": "Sanjay Damai",
#         "age" : "21",
#         "salary": "0.00001"
#     }
     
    
#     return render(request,'Home/about.html',owner)

# def service(request):
    
#     bundeshliga ={
#         "club":"Bayern",
#         "players":23,
#     }
#     laliga ={
#         "club":"Barca",
#         "players":23
#     }
#     epl ={
#         "club":"Manu",
#         "players":23
#     }
#     team={
#         "bundeshliga":bundeshliga,
#         "laliga":laliga,
#         "epl":epl
#     }
    
#     return render(request,'Home/service.html',team)

# def midi(request):
#     return HttpResponse("Midi is Sanjay")