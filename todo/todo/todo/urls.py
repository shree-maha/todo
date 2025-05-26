from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete')
]