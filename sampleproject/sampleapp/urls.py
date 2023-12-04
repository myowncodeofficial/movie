from django.urls import path

from sampleapp import views

# name space - to avoid name conflict
app_name = 'sampleapp'

urlpatterns = [
    path('', views.fun1, name='fun'),
    path('movies/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add_details, name='add_details'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]