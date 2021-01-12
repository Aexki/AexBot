from django.shortcuts import render
import requests

# Create your views here.
def contact(request):
    if request.method=="POST":
        data={'name':request.POST['name']
        ,'email':request.POST['email']
        ,'number':request.POST['number']
        ,'message':request.POST['message']}
        requests.post("https://script.google.com/macros/s/AKfycbzC3DBg05YYkklLc6njLhMywHkWrfYDl3RoKOE9EmjUemwRlW-FJ53M/exec", str(data))
        
    return render(request,'contact.html')