from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #The UserAdmin module is imported from the contrib.auth.admin django library. It's used to give permission to the administrator to access the changes in the database.
from protocolApplication.models import User,TaskDetail,CalorieDetail

# Register your models here.
admin.site.register(User, UserAdmin)
# admin.site.register(TaskDetailDate)
# admin.site.register(TaskDetailStartTime)
# admin.site.register(TaskDetailAmountOfTime)
# admin.site.register(TaskDetailDescriptionOfTheTask)
# admin.site.register(CalorieDetail)

@admin.register(TaskDetail)
class TaskDetail(admin.ModelAdmin):
   list_display = ['id', 'name', 'date', 'startTime', 'amountOfTime', 'descriptionOfTheTask', 'image', 'owner']

@admin.register(CalorieDetail)
class CalorieDetail(admin.ModelAdmin):
   list_display = ['amountOfCalories', 'currentDate', 'owner']

# @admin.register(TaskDetailStartTime)
# class TaskDetailStartTime(admin.ModelAdmin):
#    list_display = ['startTime']
#
# @admin.register(TaskDetailAmountOfTime)
# class TaskDetailAmountOfTime(admin.ModelAdmin):
#    list_display = ['amountOfTime']
#
# @admin.register(TaskDetailDescriptionOfTheTask)
# class TaskDetailDescriptionOfTheTask(admin.ModelAdmin):
#    list_display = ['descriptionOfTheTask']


