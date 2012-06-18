# algo de notation open_rating
# author : vl@cinequant.com                                                                                                                                             
################                                                                                                                                                        

import json
from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

#prend une note entre 0 et 99 et la transforme en note S&P                                                                                                              

#calcule le seuil de tolerance a la dette                                                                                                                               
# les parametres pris en compte sont                                                                                                                                    
# - niveau de dev : hdi et revenus per capita                                                                                                                           
# - historique de paiement et credibilite eco                                                                                                                           
# - exposition aux risques de taux et de change                                                                                                                         
# - desequilibre macro                                                                                                                                                  

def log(s):
    f=open('./log.txt','a+')
    f.write(str(s))
    f.write('\n')
    f.close()
    return
def tolerance(request):
    try:
        #niveau de dev                                                                                                                                                  
        hdi=float(request.POST['hdi'])
        revenus=float(request.POST['revenus'])
        chomage=float(request.POST['chomage'])

        dev=hdi+revenus/60000-chomage/10
#historique de paiement                                                                                                                                                 
        #defaut_50=request.POST['defaut_50']                                                                                                                            

#        etranger=float(request.POST['etranger'])                                                                                                                       
        #todo                                                                                                                                                           
        historique=1

        #desequilibre macro                                                                                                                                             
        courant=float(request.POST['courant'])
        macro=courant/4

        #risques de taux et change                                                                                                                                      
        #todo                                                                                                                                                           
        risque=1

        #todo : prendre en compte les poids de l'input reg_*                
        poids_risque=1.0
        poids_dev=1.0
        poids_historique=1.0
        poids_macro=0.3
        poids_total=poids_risque+poids_dev+poids_historique+poids_macro
        #calcule une moyenne ponderee                                                                                                                                   

        #calibrer les coefficients                                                                                                                                      
        return float(0.30+1.70*(poids_dev*dev+poids_historique*historique+poids_macro*macro+poids_risque*risque)/(poids_total))
    except Exception,e:
        log (str(e))
        print e
        return -1
#seuil=hdi*200                                                                                                                                                          
    return 0

def DSA(request):
#fait une DSA rapide                                                                                                                                                    
    dette=float(request.POST['dette_PIB'])/100
    interet=float(request.POST['interet'])/100
    inflation=float(request.POST['inflation'])/100
    #calcul selon la formule du FMI                                                                                                                                     
    ratios_dette=[dette]
    for i in range(10):
        annee=min(2016,2012+i)

        deficit=float(request.POST["deficit_"+str(annee)])/100-interet*ratios_dette[-1]

        croissanceR=float(request.POST['croissance_'+str(annee)])/100

        croissanceN=(1+croissanceR)*(1+inflation)-1
        lambda_dsa=float(interet-croissanceN)/(1+croissanceN)
        new_dette=(1+lambda_dsa)*ratios_dette[-1]+deficit
        ratios_dette.append(new_dette)
    log (ratios_dette)
    return ratios_dette

def graphURL(data):
    log ("debut graphURL")
    log (str(data))
    # Set the vertical range from 0 to 100                                                                                                                              
    max_y = 100*max(data)+20
# Chart size of 300x150 pixels and specifying the range for the Y axis                                                                                                  
    log (str(max_y))
    try:
        chart = SimpleLineChart(300, 150, y_range=[0, max_y])
    except Exception,e:
        log(str(e))
    # Add the chart data                                                                                                                                                
    chart.add_data([100*x for x in data])
# Set the line colour to blue                                                                                                                                           
    chart.set_colours(['0000FF'])
# Set the vertical stripes                                                                                                                                              
#    chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)                                                                                            
# Set the horizontal dotted lines                                                                                                                                       
    chart.set_grid(0, 25, 5, 5)
    # The Y axis labels contains 0 to 100 skipping every 25, but remove the                                                                                             
    # first number because it's obvious and gets in the way of the first X                                                                                              
    # label.                                                                                                                                                            
    log ("here")
    left_axis = range(0, int(max_y + 1), 25)
    log ("there")
    left_axis[0] = ''
    log ("therem")
    log ("therem")
    chart.set_axis_labels(Axis.LEFT, left_axis)
# X axis labels                                                                                                                                                         
    log ("there")

    chart.set_axis_labels(Axis.BOTTOM, ['2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    log("fin graphURL")
    return chart.get_url()

#note de 0 a 99                                                                                                                                                         
def rateDec(request):
    log("rateDec")
    sensibilite=100
    data=DSA(request)
    seuil=sensibilite*(float(tolerance(request))-float(max(data)))
    seuil=max(0,seuil)
    seuil=min(99,seuil)
    return int(seuil)

def ratingToSP(note):
    log("ratingToSP")
    noteSP=""
    notesSP=["D","C","CC","CCC-","CCC", "B-","B","B+","BB-", "BB","BB+", "BBB-","BBB","BBB+","A-","A","A+","AA-","AA","AA+","AAA" ];
    i=note*len(notesSP)/100
    noteSP=notesSP[i]
    log ("fin ratingToSP")
    return noteSP

def rate(request):
#point d'entree dans l algo de notation                                                                                                                                 
    log(str(request.POST))
    response=["null","null"]
    params=request.POST
    if params['defaut_exterieur']=="1":
        print "defaut exterieur"
        response=["D","/"]
    else:
        #les valeurs de la dynamique de la dette                                                                                                                        
        DSAData=DSA(request)
        #calcule note de 1 a 100                                                                                                                                        
        noteDec=rateDec(request)
        response=[ratingToSP(noteDec),str(graphURL(DSAData)), tolerance(request)]
    return json.dumps(response)