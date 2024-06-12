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
from django.conf import settings
from django.http import HttpResponse
from protocolApplication.views import helloworld,AddTask,UpdateTask,RetrieveTask,DeleteTaskDetails, SignUp, Login, CalorieTracker, CalorieDetailRetrieved, spa_view, print_test_results
from django.conf.urls.static import static

urlpatterns = [
#     path('', helloworld),
    path("admin/", admin.site.urls),
    path('health', include('protocolApplication.urls')),
    #path("health", lambda request: HttpResponse("health check")),
    path("signup/", SignUp, name='signup'),
    path("", Login, name="login"),
    path("login/", Login, name="login"),
    path('TaskInsert/',AddTask),
    path('TaskUpdate/',UpdateTask),
    path('RetrieveTaskDetails/',RetrieveTask),
    path('DeleteTaskDetail/',DeleteTaskDetails),
    path('CalorieTracker/',CalorieTracker),
    path('RetrieveCalorieDetails/',CalorieDetailRetrieved),
    #path('test_results/', print_test_results),
    #path('/', spa_view),
    #re_path(r'^.*', spa_view, name='vue SPA')
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

