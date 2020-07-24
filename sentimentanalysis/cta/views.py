from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
import itertools
import json
from . import dest
from . import graph_data

functions = ['All OVER DATA', 'MAJOR CITIES', 'ABOUT US', 'SENTIMENT CHECKER', 'COVID CASES']
paths = ['/','/major_cities', '/about-us', '/live-analysis', '/covid-cases']
def makenav(active):
    navs=[]
    for fun, path in zip(functions, paths):
        if fun == active:
            navs.append(nav(fun,path,active=True))
        else:
            navs.append(nav(fun,path))
    return navs
def createobj(loc):
    obj = graph_data.TryData(loc)
    return obj

def index(request):
    template = loader.get_template('index.html')
    obj=createobj('overall')
    data=obj.getdata()
    overall=obj.overall_data
    context = {
        'data':data,
        'overall':overall,
        'navs':makenav('All OVER DATA')
    }
    return HttpResponse(template.render(context,request))

def major_cities(request):

    Mumbai=dest.Cities('Mumbai','https://res.cloudinary.com/dseemci6h/image/upload/v1594205707/Mumbai_nmtl78.webp',createobj('Mumbai').overall_data)
    Delhi = dest.Cities('Delhi', 'https://res.cloudinary.com/dseemci6h/image/upload/v1594205702/Delhi_hihvem.jpg',createobj('Delhi').overall_data)
    Kolkata = dest.Cities('Banglore', 'https://lp-cms-production.imgix.net/2019-06/9483508eeee2b78a7356a15ed9c337a1-bengaluru-bangalore.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4', createobj('Banglore').overall_data)
    Chennai = dest.Cities('Chennai', 'https://res.cloudinary.com/dseemci6h/image/upload/v1594205702/Chennai_elym5i.jpg', createobj('Chennai').overall_data)
    cities=[Mumbai, Delhi, Kolkata, Chennai]
    return render(request, 'major_cities.html', {'cities':cities, 'navs':makenav('MAJOR CITIES')})

def city(request,city_name):
    template = loader.get_template('cities.html')
    obj = createobj(city_name)

    data = obj.getdata()
    overall = obj.overall_data
    context = {
        'city_name': city_name,
        'data': data,
        'overall': overall,
        'navs': makenav('MAJOR CITIES')
    }
    return HttpResponse(template.render(context, request))

def about_us(request):
    return render(request,'user.html', {'navs':makenav('ABOUT US')})

def live_analysis(request):
    return render(request,'live_analysis.html', {'navs':makenav('SENTIMENT CHECKER')})

def covid_cases(request):
    r = requests.get('https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise')
    data = json.loads(r.text)
    data = json.dumps(data['data'])
    return render(request,'covid-cases.html',{'data':data, 'navs':makenav('COVID CASES')})

class nav:
    def __init__(self,name, path,active=False):
        self.name = name
        self.path = path
        if active:
            self.active="active"
        else:
            self.active=""