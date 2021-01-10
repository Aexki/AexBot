from django.shortcuts import render,redirect
import os
import json
from datetime import datetime,date
from chatbot.chatbot import get_response,predict_class
import requests

def process_request(request):
    dote = request.session['last_activity']
    # print("Last Activity :"+str(dote))
    last_activity = datetime.strptime(dote, '%Y-%m-%d %H:%M:%S.%f')
    now = datetime.now()
    if (now - last_activity).seconds > 60:
        # print("Session Expired!")
        
        path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'usersofchatbot')
        username=request.session['username']
        # print("Deleting : "+path+'\{}.json'.format(username))
        
        try:
            with open(path+'/{}.json'.format(username)) as feedsjson:
                feeds = json.load(feedsjson)
            feedsjson.close
                
            if request.session['status:on']:
                print("Session Ended")
                requests.post('https://script.google.com/macros/s/AKfycbyrykMlZdJiSK6pHI9HkQRIjKyxHMiD5j7oNwUIIMrYNq7k30fr/exec',str(feeds))
                print('data: '+str(feeds))
                
                os.remove(path+'\{}.json'.format(username))
                request.session['status:on']=False
            
            # print("Deleted Successfully...")
        except OSError as e:
            print("Failed with:", e.strerror)
            
        return 0


# Create your views here.
def send(request):
    username=request.session['username']
    path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'usersofchatbot')
    res=process_request(request)
    
    #initializing a json file for new user
    if os.path.isfile(path+'/{}.json'.format(username)) == 0: 
        fileopener=open(path+'/{}.json'.format(username),'w')
        fileopener.close
        
        with open(path+'/{}.json'.format(username), mode='w') as f:
            f.write(json.dumps({"username":username,"Messages":[]}, indent=2))
        f.close
    
    if request.method=="POST":
        request.session['last_activity']=str(datetime.now())
        name=request.session['username']
        message=request.POST['message']
        
        #using the chatbot to store data in json file
        ints = predict_class(message)
        path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chatbot')
        intents = json.loads(open(path+'\intents.json').read())
        
        path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'usersofchatbot')
        with open(path+'/{}.json'.format(username)) as feedsjson:
            feeds = json.load(feedsjson)
            
        feeds["Messages"].append({"Name":name, "Message":message, "Type":'client', "DateTime": datetime.now().strftime("%H:%M:%S ")+"   |   "+date.today().strftime("%B %d, %Y")})
        feeds["Messages"].append({"Name":"Chatbot", "Message":get_response(ints, intents), "Type":'myside', "DateTime": str(datetime.now())})
        
        with open(path+'/{}.json'.format(username), mode='w') as f:
            f.write(json.dumps(feeds, indent=2))
        
    #reading data for template    
    with open(path+'/{}.json'.format(username)) as feedsjson:
        feeds = json.load(feedsjson)
    
    
    if res!=0:
        return render(request, 'client.html', feeds)
    else:
        return redirect('/')
    
