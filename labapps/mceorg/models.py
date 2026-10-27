from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
 topic = models.CharField(max_length=100, default='') # Added default value for topic
 languages_used = models.CharField(max_length=100, default='')
 duration = models.IntegerField(default=0)
 def str (self):
  return self.topic