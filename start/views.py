from Sender.views import send
from django.shortcuts import redirect, render
import json
import os
from datetime import datetime

# Create your views here.
def start(request):
    if request.method == "POST":
        request.session['last_activity'] = str(datetime.now())
        username=request.POST.get('username')
        request.session['username']=username
        request.session['status:on']=True
        
        return redirect(send)
    
    return render(request,'index.html')