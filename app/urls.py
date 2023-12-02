from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="inicio_app"),
    path('get_user', views.get_user,name="get_user_app"),
]