from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.name
    
class Exam_Result(models.Model):
    student = models.ForeignKey(Student,on_delete = models.CASCADE, null = True)
    
    percentage = models.FloatField()
    grade = models.CharField(max_length = 10)
    
    def __str__ (self):
        return self.student.name