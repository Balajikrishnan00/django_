from django.contrib import admin
from django.urls import path,include
from CRUDApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crudview/',views.studentlistView)
    
]