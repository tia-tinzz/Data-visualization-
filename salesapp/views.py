from django.shortcuts import render,HttpResponse
from .models import Sale
from .utils import get_plot,get_barplot,get_covidbarplot
#from urllib.request import urlopen
import requests

#import ssl
# Create your views here.
#import matplotlib.pyplot as plt
import json


def covid(request):
    dictionary = json.load(open('file.json', 'r'))
    x = [key for key, value in dictionary.items()]
    y = [value for key, value in dictionary.items()]
    chart=get_barplot(x,y)
   
    return render(request,'covid.html',{'chart':chart})


def home(request):
    qs=Sale.objects.all()
    x=[x.item for x in qs]
    y=[y.price for y in qs]
    chart=get_plot(x,y)
    return render(request,'home.html',{'chart':chart})

def covidapi(request):
    #response=requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population').json()
    dictionary = json.load(open('coviddaily.json', 'r'))
    #result_list = [[int(v) for k,v in d.items()] for d in dictionary]
    '''a=dict(dictionary)
    print(a)
    #x={k for e in dictionary for (k,v) in e.items()}
    #y={v for e in dictionary for (k,v) in e.items()}
    print("helllo")
    print(dictionary.keys())
    print("ffygu")
    for k,v in dictionary.items():
        print()'''
    #labels = []
    #values = []
    x = [k for k,v in dictionary.items()]
    y = [v for k,v in dictionary.items()]
    chart=get_covidbarplot(x,y)
    return render(request,'coviddata.html',{'chart':chart})

def population(request):
    return render(request,'populationjs.html')


