"""
URL configuration for csepythonweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from home.views import homepage
from home.views import aboutpage
from home.views import contactpage
from programs.views import programspage
from students.views import studentspage
from students.views import studentleadershippage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', aboutpage),
    path('contact/', contactpage),
    path('programs/', programspage),
    path('students/', studentspage),
    path('studentleadership/', studentleadershippage)
]
