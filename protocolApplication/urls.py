"""MasterProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.http import HttpResponse
from django.conf import settings

#These are the python functions that are imported from the view.py file from the protocolApplication folder.
from protocolApplication.views import helloworld,AddTask,UpdateTask,RetrieveTask,DeleteTaskDetails, SignUp, Login, CalorieTracker, CalorieDetailRetrieved, spa_view, print_test_results


#This is the URL path to python function mapping. As soon as the URL path is accessed, the python function is called
urlpatterns = [
    #     path('', helloworld),
    #path("admin/", admin.site.urls),
    #path("", lambda request: HttpResponse("health check")),
    path("signup/", SignUp, name='signup'),
    path("", Login, name="login"),
    path("", lambda request: HttpResponse("health check")),
    path("login/", Login, name="login"),
    path('TaskInsert/',AddTask),
    path('TaskUpdate/',UpdateTask),
    path('RetrieveTaskDetails/',RetrieveTask),
    path('DeleteTaskDetail/',DeleteTaskDetails),
    path('CalorieTracker/',CalorieTracker),
    path('RetrieveCalorieDetails/',CalorieDetailRetrieved),
    path('test_results/', print_test_results),
    #path('', spa_view),
    #re_path(r'^.*', spa_view, name='vue SPA'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,
                  document_root=settings.MEDIA_ROOT)
#This is where the image URL is concatenated to the urlpattern to locate the store the image in the database
