from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.UserView.as_view(), name='user_list')
    path('user/<int:pk>', views.UserView.as_view(), name='user_view')
    path('user/new', views.userCreate.as_view(), name='user_new'),
    path('user/view/<int:pk>', views.userView.as_view(), name='user_view'),
    path('user/edit/<int:pk>', views.userUpdate.as_view(), name='user_edit'),
    path('user/delete/<int:pk>', views.userDelete.as_view(), name='user_delete'),
]