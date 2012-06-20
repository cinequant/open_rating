/***************************/
//@Author : Vincent Lepage, Cinequant SAS
//@email : vl@cinequant.com

//for the Popup code :
//@Author: Adrian "yEnS" Mato Gondelle
//@website: www.yensdesign.com
//@email: yensamg@gmail.com
//@license: Feel free to use it, but keep this credits please!					
/***************************/



pays="";
function chargeData()
// put the data in the form after selecting a country
{

    var form=document.getElementById("pays");
    pays=form.options[form.selectedIndex].text;

    document.getElementById("image_pays").innerHTML="<strong>"+ pays +"</strong>"+"<br><img src='static/open-rating/"+pays+".gif' height='250'/>";
    document.getElementById("nom_pays").innerHTML="<strong>"+ pays +"</strong>";

    document.getElementById("note_sp").innerHTML="<strong>"+note[pays][0]+"</strong>";
    document.getElementById("note_fitch").innerHTML="<strong>"+note[pays][1]+"</strong>";
    document.getElementById("note_moody").innerHTML="<strong>"+note[pays][2]+"</strong>";

    document.getElementsByName("dette_PIB")[0].value=macro[pays]['dette_PIB'];
    document.getElementsByName("hdi")[0].value=macro[pays]['hdi'];
    document.getElementsByName("deficit_2011")[0].value=macro[pays]['deficit_PIB'];
    document.getElementsByName("chomage")[0].value=macro[pays]['chomage'];
    document.getElementsByName("croissance_2011")[0].value=macro[pays]['croissance'];
    document.getElementsByName("croissance_2012")[0].value=macro[pays]['croissance_2012'];
    document.getElementsByName("croissance_2013")[0].value=macro[pays]['croissance_2013'];
    document.getElementsByName("croissance_2014")[0].value=macro[pays]['croissance_2014'];
    document.getElementsByName("croissance_2015")[0].value=macro[pays]['croissance_2015'];
    document.getElementsByName("croissance_2016")[0].value=macro[pays]['croissance_2016'];
    $( "#slider_croissance_2012" ).slider( "value" , macro[pays]['croissance_2012']);
    $( "#slider_croissance_2013" ).slider( "value" , macro[pays]['croissance_2013']);
    $( "#slider_croissance_2014" ).slider( "value" , macro[pays]['croissance_2014']);
    $( "#slider_croissance_2015" ).slider( "value" , macro[pays]['croissance_2015']);
    $( "#slider_croissance_2016" ).slider( "value" , macro[pays]['croissance_2016']);

    document.getElementsByName("deficit_2012")[0].value=macro[pays]['deficit_2012'];
    document.getElementsByName("deficit_2013")[0].value=macro[pays]['deficit_2013'];
    document.getElementsByName("deficit_2014")[0].value=macro[pays]['deficit_2014'];
    document.getElementsByName("deficit_2015")[0].value=macro[pays]['deficit_2015'];
    document.getElementsByName("deficit_2016")[0].value=macro[pays]['deficit_2016'];
    $( "#slider_deficit_2012" ).slider( "value" , macro[pays]['deficit_2012']);
    $( "#slider_deficit_2013" ).slider( "value" , macro[pays]['deficit_2013']);
    $( "#slider_deficit_2014" ).slider( "value" , macro[pays]['deficit_2014']);
    $( "#slider_deficit_2015" ).slider( "value" , macro[pays]['deficit_2015']);
    $( "#slider_deficit_2016" ).slider( "value" , macro[pays]['deficit_2016']);

    document.getElementsByName("revenus")[0].value=macro[pays]['revenus'];
    document.getElementsByName("courant")[0].value=macro[pays]['bop'];
    document.getElementsByName("defaut_exterieur")[0].value=macro[pays]['defaut_exterieur'];
    document.getElementsByName("inflation")[0].value=macro[pays]['inflation'];
    document.getElementsByName("interet")[0].value=macro[pays]['interet'];
}


// systeme de slide
var slides=[];
var slides_expert=["#slide1","#slide2","#slide3","#slide4","#slide5","#slide6","#slide7","#slide8"];
var slides_debutant=["#slide1","#slide2","#slide3","#slide4_debutant","#slide7","#slide8_debutant"];
var navs_expert=["nav_intro_expert","nav_1_expert","nav_2_expert","nav_3_expert","nav_4_expert","nav_5_expert","nav_6_expert","nav_7_expert"];
var navs_debutant=["nav_intro_debutant","nav_1_debutant","nav_2_debutant","nav_3_debutant","nav_4_debutant","nav_5_debutant","nav_5_debutant","nav_5_debutant"];
var current=0;

function slideIn(element) {
    element.style.left=2000;
}

function next() {
    document.getElementById(navs_expert[current]).className=""; 
    document.getElementById(navs_expert[current+1]).className="selected"; 
    document.getElementById(navs_debutant[current]).className=""; 
    document.getElementById(navs_debutant[current+1]).className="selected"; 
    
    $(slides[current+1]).css('display',"block");
    //	$(slides[current+1]).css('left',"850"); 
    
    //	$( slides[current]).animate({left:"-100%"},5000, function() {                                             
    //       $( slides[current] ).hide();                                                                                           
    //      current=current+1;                                                                                                     
    //  } );                                                                                                                    
    //	$( slides[current+1]).animate({left:"0%"},5000, function() {});	
    jQuery("button").attr('disabled', true);
    
    $(".button_previous").off('click');

    $( slides[current]).hide("slide", { direction: "left" }, 1500, function() {
	$( slides[current] ).hide();	
	current=current+1;    		
	jQuery("button").attr('disabled', false);
	$(".button_previous").click(function(){
            previous();
        });

    } );
    $( slides[current+1]).effect("slide", { direction: "right" }, 1500 );
  };

function previous() {
    document.getElementById(navs_expert[current]).className=""; 
    document.getElementById(navs_expert[current-1]).className="selected"; 
    document.getElementById(navs_debutant[current]).className=""; 
    document.getElementById(navs_debutant[current-1]).className="selected"; 
    jQuery("button").attr('disabled', true);
    $(".button_previous").off('click');

    $( slides[current]).hide("slide", { direction: "right" }, 1500, function() {
    	$( slides[current] ).hide();	
	current=current-1;    	
	jQuery("button").attr('disabled', false);	
	$(".button_previous").click(function(){
            previous();
        });
    } );
    $(slides[current-1]).show("slide", { direction: "left" }, 1500 );
};


// systeme popup

//0 means disabled; 1 means enabled;
var popupStatus = 0;
var popupStatusCredit=0;

function loadPopupCredit(){
    //loads popup only if it is disabled                                                                                                                                
    if(popupStatusCredit==0){
        $("#backgroundPopup").css({
            "opacity": "0.7"
        });
        $("#backgroundPopup").fadeIn("slow");
        $("#popupCredit").fadeIn("slow");
        popupStatusCredit = 1;
    }
}


//loading popup with jQuery magic!
function loadPopup(){
    //loads popup only if it is disabled
    if(popupStatus==0){
	$("#backgroundPopup").css({
		"opacity": "0.7"
		    });
	$("#backgroundPopup").fadeIn("slow");
	$("#popupContact").fadeIn("slow");
	popupStatus = 1;
	var timer = null;
	var messages = ["D","C","CC","CCC-","CCC", "B-","B","B+","BB-", "BB","BB+", "BBB-","BBB","BBB+","A-","A","A+","AA-","AA","AA+","AAA"];
	var positions=["340px","327px","314px","301px","288px","275px","262px","249px","236px","223px","210px","197px","184px","171px","158px","145px","132px","119px","106px","93px","80px"];
	var message = "";

	//	$("#note").show("slide", { direction: "up" , distance: 300}, 2000 );

	timer = setInterval(function() {
		var part = messages.shift();
		var pos = positions.shift();
		document.getElementById("note").style.top=pos;

		if (!part) return clearInterval(timer);   
		if (part==noteMax) {
		    /*derniere execution quand on atteint la bonne note*/
		    document.getElementById("note").innerHTML =part;
		    document.getElementById("note").style.color="#EE0000";
	
		    document.getElementById("dsa").src=urlDSA;
		    $("#dsaDiv").fadeIn(3000);

		    document.getElementById("note_sp_final").innerHTML =note[pays][0]+"(pour S&P)";
	  	    document.getElementById("note_sp_final").style.top=positions[messages.indexOf(note[pays][0])];

		    $("#note_sp_final").fadeIn(3000);
		    window.setTimeout('document.getElementById("note").style.color="#444444"',80);
		    return clearInterval(timer);
		}
		var message=part;
		document.getElementById("note").innerHTML =part; 
		document.getElementById("note").style.color="#00EE00";
		window.setTimeout('document.getElementById("note").style.color="#444444"',80);
	    }, 300);	
    }
}


//disabling popup with jQuery magic!
function disablePopup(){
    //disables popup only if it is enabled
    if(popupStatus==1){
	$("#backgroundPopup").fadeOut("slow");
	$("#popupContact").fadeOut("slow");
	popupStatus = 0;
    }
    if(popupStatusCredit==1){
        $("#backgroundPopup").fadeOut("slow");
        $("#popupCredit").fadeOut("slow");
        popupStatusCredit = 0;
    }

}

// lancement au demarrage de la page
$(document).ready(function(){
	//  centerFenetre();
	$("div[title]").tooltip();

 $("#button_pays_existant").click(function(){
		$("#carte_identite").fadeIn("slow");
                $("#button_generic_next").fadeIn("fast");
	    });

 $(".button_next").click(function(){
     if (slides.indexOf(slides[current])==slides.length-2) {
	 $("#button_generic_next").fadeOut("fast");
     }
     next();    
 });
 $("#button_debutant").click(function(){
	 $("#nav_debutant").fadeIn("slow");
	 slides=slides_debutant;
	 next();
	    });
 $("#button_expert").click(function(){
	 $("#nav_expert").fadeIn("slow");
	 slides=slides_expert;
	 next();
     });

 $(".button_previous").click(function(){
		previous();
	    });

 // notation en AJAX
 noteMax="";
 urlDSA="";
	
	/*<![CDATA[ code from http://www.micahcarrick.com/ajax-form-submission-django.html */
 jQuery(function() {
		var form = jQuery("#ratingForm");
		form.submit(function(e) {		e.preventDefault();
		    });
     });
	//LOADING POPUP
	//Click the button event!
	$("#info_credibilite").click(function(){
		alert('credibilite');
		loadPopupCredibilite();
	    });	
	//CLOSING POPUP
	//Click the x event!
	$("#popupContactClose").click(function(){
		disablePopup(); 
	    });

	$("#popupCreditClose").click(function(){
		disablePopup(); 
	    });

	//Click out event!
	$("#backgroundPopup").click(function(){
		disablePopup();
	    });
	//Press Escape event!
	$(document).keypress(function(e){
		if(e.keyCode==27 && popupStatus==1){
		    disablePopup();
		}
		if(e.keyCode==27 && popupStatusCredit==1){
		    disablePopup();
		}		
	    });	
    });