from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import urlparse,urlencode
import ipaddress
import re
from . import abbf,urlfeatures,predict
from .models import website
# Create your views here.

#converting the list to dataframe
feature_names = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 'Label']


def home(request):
    return render(request,'home.html')

def find(request):
    url = request.GET['url']
    print(url)
    out = urlfeatures.featureExtraction(url,0) 
    websiteobj = website.objects.filter(url=out[0])
    print(out[0])
    print(websiteobj)
    if websiteobj:
        print(websiteobj[0].status )
        if websiteobj[0].status:
            return render(request,'notsafe.html')
        else:
            return render(request,'safe.html')
    #url = 'http://u1047531.cp.regruhosting.ru/acces-inges'
    
    out.remove(out[0])
    print(out)
    p = predict.prediction(out)
    print(type(p))
    if p == 0:
        return render(request,'safe.html')
    else:
        return render(request,'notsafe.html')
    return HttpResponse(out)




 