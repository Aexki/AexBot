from django.shortcuts import render
from Sender.models import Message

# Create your views here.

def recieve(request):
    if request.method=="POST":
        name="Aexki"
        message=request.POST['message']
        newmessage=Message(name=name, message=message, type='myside')
        newmessage.save()
      
    all_messages=Message.objects.all()
    
    context={
        "all_messages":all_messages
    } 
    
    return render(request,'myside.html', context)