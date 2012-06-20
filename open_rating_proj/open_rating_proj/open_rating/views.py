                                                                                                                       
from datetime import date
from datetime import timedelta

import open_rating_algo
import json

from django.template import Context, RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

#page d'accueil                                                                                                                                                         
def index(request):
    country="pays"
    if "country" in request.REQUEST:
        country=request.REQUEST['country']
    note="AAA"
    if "note" in request.REQUEST:
        note=request.REQUEST['note']
    if "code" in request.REQUEST:
        s=request.REQUEST['code']
        country=s.split('_')[0]
        note=s.split('_')[1]

    if request.method=='POST':
        #appel AJAX                                                                                                                                                     
        #va calculer la note sous forme de string, a la SP                                                                                                              
        f=open('./log.txt','w+')
        f.write(str(request.POST))
        #      f.write(str(request.POST['defaut_exterieur']))                                                                                                           
        f.write('\n')
        f.close()
        print request
        note=open_rating_algo.rate(request)
        return HttpResponse(note)

    data=[]
    return render_to_response('index.html',{'data':data,'country':country,'note':note},context_instance=RequestContext(request))

