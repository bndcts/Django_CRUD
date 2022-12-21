from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.UserView.as_view(), name='user_list'),
    path('user/<int:pk>', views.UserView.as_view(), name='user_view'),
    path('user/new', views.UserCreate.as_view(), name='user_new'),
    path('user/view/<int:pk>', views.UserView.as_view(), name='user_view'),
    path('user/edit/<int:pk>', views.UserUpdate.as_view(), name='user_edit'),
    path('user/delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
]