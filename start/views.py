from Sender.views import send
from django.shortcuts import redirect, render
from datetime import datetime
import os,json,requests

# Create your views here.
def start(request):
    if request.method == "POST":
        request.session['last_activity'] = str(datetime.now())
        username=request.POST.get('username')
        request.session['username']=username
        request.session['status:on']=True
        path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'usersofchatbot')
        try:
            with open(path+'/{}.json'.format(username)) as feedsjson:
                feeds = json.load(feedsjson)
            feedsjson.close
            # requests.post('https://script.google.com/macros/s/AKfycbyrykMlZdJiSK6pHI9HkQRIjKyxHMiD5j7oNwUIIMrYNq7k30fr/exec',str(feeds))
            
            os.remove(path+'\{}.json'.format(username))
        except OSError as e:
            # print("Failed with:", e.strerror)
            pass
        
        # requests.post('https://script.google.com/macros/s/AKfycbxsxBXbs1xEA0TLouoSAG4QZ4oXnycikuG8NNUl0DwKx5OBLezR/exec',username+' has accessed the Aexbot.')
            
        return redirect(send)
    
    if 'username' in request.session.keys():
        path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'usersofchatbot')
        username=request.session['username']
        
        try:
            with open(path+'/{}.json'.format(username)) as feedsjson:
                feeds = json.load(feedsjson)
            feedsjson.close
            
            # requests.post('https://script.google.com/macros/s/AKfycbyrykMlZdJiSK6pHI9HkQRIjKyxHMiD5j7oNwUIIMrYNq7k30fr/exec',str(feeds))
            os.remove(path+'\{}.json'.format(username))
        except OSError as e:
            # print("Failed with:", e.strerror)
            pass
            
    return render(request,'index.html')