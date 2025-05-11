from django.shortcuts import render, HttpResponse
import requests
import datetime
from django.contrib import messages
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'paris'
        
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d65f3bad686e9406ae09df2a79d42978'
    PARAMS = {'units':'metric'}
    try:
        data = requests.get(url,PARAMS).json()
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        country = data['sys']['country']
        
        day = datetime.date.today()
        context = {'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'country':country,'exception_occurred':True}
        return render(request,'weatherapp/index.html',context)
    except:
        exception_occurred =True
        # data = requests.get(url,PARAMS).json()
        messages.error(request,'entered data is not available to API')
        day = datetime.date.today()
        # country = data['sys']['country']
        context = {'description':'clear sky','icon':'01d','temp':25,'day':day,'exception_occurred':True}
        return render(request,'weatherapp/index.html',context)
        
