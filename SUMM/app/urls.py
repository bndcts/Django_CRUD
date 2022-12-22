from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('users/add/', views.add_user, name='add-user'),
    path('users/all/', views.view_users, name='view-users'),
    path('users/update/<int:pk>/', views.update_users, name='update-users'),
    path('users/delete/<int:pk>/', views.delete_users, name="delete-users"),
    path('translations/add/', views.add_translation, name='add-translation'),
    path('translations/all/', views.view_translations, name='view-translations'),
    path('translations/update/<int:pk>/', views.update_translations, name='update-translations'),
    path('translations/delete/<int:pk>/', views.delete_translations, name="delete-translations")
]