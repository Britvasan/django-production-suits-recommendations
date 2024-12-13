from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('clientlogin/', views.clientlogin, name='clientlogin'),
    path('logout/', views.logout_view, name='logout_view'),
    path('index/', views.index, name='index'),
    path('result/', views.result_view, name='result'),
    path('client_list/', views.client_list, name='client_list'),
    path('update_status/<int:client_id>/', views.update_status, name='update_status'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
]


