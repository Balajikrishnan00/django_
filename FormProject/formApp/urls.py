from django.contrib import admin
from django.urls import path
from  formApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome),
    path('form/',views.empDetailView)
]