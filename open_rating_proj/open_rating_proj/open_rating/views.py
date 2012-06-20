from datetime import date
from datetime import timedelta
from openRatingForm import openRatingForm
import openRatingAlgo
import json

from django.template import Context, RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

import MySQLdb

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
        note=openRatingAlgo.rate(request)
        return HttpResponse(note)
        
    else:
        form=openRatingForm()
    data=[]
    return render(request,'openRating/index.html',{'form':form, 'data':data,'country':country,'note':note})

def facebook(request):
    t=loader.get_template('openRating/facebook_login.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
