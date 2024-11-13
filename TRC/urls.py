"""
URL configuration for TRC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app_TRC import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tralist/', views.trancion_list),
    path('signin/', views.sign_in),
    path('login/', views.log_in),
    path('getall/', views.get_trancions),
    path('savetrc/', views.save_trancions),
    path('report/', views.report_Trancions),
    path('del/', views.delet_trnacions),
    path('filtertrc/', views.filter_trancions)
]   

