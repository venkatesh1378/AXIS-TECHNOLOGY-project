from django.contrib import admin
from .models import Student,stdlogin,admlogin,usertimings

# Register your models here.
admin.site.register(Student)
admin.site.register(stdlogin)
admin.site.register(admlogin)
admin.site.register(usertimings)