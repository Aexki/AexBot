from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('start.urls')),
    path('client/',include('Sender.urls')),
    path('myside/', include('Reciever.urls')),
    path('contact/',include('Contact.urls'))
]


