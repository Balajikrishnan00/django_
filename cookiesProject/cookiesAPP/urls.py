from django.contrib import admin
from django.urls import path,include
from cookiesAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/',views.sessionID_count_View)

]