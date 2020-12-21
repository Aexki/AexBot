from django.urls import path,include
from . import views

urlpatterns = [
    # path('/client', views.send, name="send"),
    path('', views.send, name="send")
]

