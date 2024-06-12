from django.db import models
from django.core import validators
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Submit
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     available = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.title

class User(AbstractUser):

  username = models.CharField(max_length=50, unique=True)

  firstName = models.CharField(
                    max_length = 50
                )
  lastName = models.CharField(
           max_length = 50
       )

  user_email = models.EmailField(max_length = 254, null=True, blank=True)

  def __str__(self):
      return self.username

  def to_dict(self):
      return {
         'username': self.username,
      }

class TaskDetail(models.Model):
   id = models.BigAutoField(primary_key=True)
   name = models.TextField()
   date = models.DateField(auto_now=False)
   startTime = models.TimeField(auto_now=False)
   amountOfTime = models.TimeField(auto_now=False)
   descriptionOfTheTask = models.TextField()
   image = models.ImageField(upload_to='images/')
   owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))

   def __str__(self):
       return f"({self.name})({self.date})({self.startTime})({self.amountOfTime})({self.descriptionOfTheTask})"

   def to_dict(self):
       return{
           'id': self.id,
           'name': self.name,
           'date':self.date,
           'startTime':self.startTime,
           'amountOfTime':self.amountOfTime,
           'descriptionOfTheTask':self.descriptionOfTheTask,
           'image': "http://localhost:8000/" + self.image.url,
       }

# class TaskDetailStartTime(models.Model):
#    startTime = models.TimeField(auto_now=False)
#    taskdate = models.ForeignKey(TaskDetailDate, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))
#
#    def __str__(self):
#        return f"({self.startTime})"
#
# class TaskDetailAmountOfTime(models.Model):
#    amountOfTime = models.TimeField(auto_now=False)
#    taskstarttime = models.ForeignKey(TaskDetailStartTime, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))
#
#    def __str__(self):
#        return f"({self.amountOfTime})"
#
# class TaskDetailDescriptionOfTheTask(models.Model):
#    descriptionOfTheTask = models.TextField()
#    taskamountoftime = models.ForeignKey(TaskDetailAmountOfTime, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))
#    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))
#
#    #def __str__(self):
#        #return f"({self.date}) ({self.startTime}) ({amountOfTime}) ({self.descriptionOfTheTask})"
#    def __str__(self):
#        return f"({self.descriptionOfTheTask})"

class CalorieDetail(models.Model):
   amountOfCalories = models.IntegerField()
   currentDate = models.DateTimeField(auto_now_add=True)
   owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))

   def __str__(self):
       return f"({self.amountOfCalories}) ({self.currentDate}) ({self.owner})"

   def to_dict(self):
       return{
           'amountofcalories': self.amountOfCalories,
           'currentdate': self.currentDate
       }