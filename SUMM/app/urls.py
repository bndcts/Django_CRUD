from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('add/', views.add_user, name='add-user'),
    path('all/', views.view_users, name='view_users'),
    path('update/<int:pk>/', views.update_users, name='update-users'),
    path('user/<int:pk>/delete/', views.delete_users, name="delete-users")
]