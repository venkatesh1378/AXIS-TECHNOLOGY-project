from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30)
    emailid=models.EmailField(max_length=40)
    adress=models.CharField(max_length=20)
    def __str__(self):
        return self.name
        


class stdlogin(models.Model):
    name=models.CharField(max_length=100) 
    password=models.CharField(max_length=20)  
    def __str__(self):
        return self.name
class admlogin(models.Model):
    name=models.CharField(max_length=100) 
    password=models.CharField(max_length=20)  
    def __str__(self):
        return self.name 
class usertimings(models.Model):
     InTime=models.CharField(max_length=100)   
     Work=models.CharField(max_length=100)
     OutTime=models.CharField(max_length=100)
     signature=models.CharField(max_length=20)
     def __str__(self):
        return self.Work
