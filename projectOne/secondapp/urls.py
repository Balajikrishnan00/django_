from django.contrib import admin
from django.urls import include, path
from secondapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('secondf1/',views.sfun1)
]