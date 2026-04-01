from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.get_blogs),
    path('create/', views.create_blog),
    path('blogs/<int:id>/', views.get_single_blog),
    path('update/<int:id>/', views.update_blog),
    path('delete/<int:id>/', views.delete_blog),

]
