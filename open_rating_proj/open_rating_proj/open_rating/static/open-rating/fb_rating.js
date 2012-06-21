  // Load the SDK Asynchronously
  (function(d){
  var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
  if (d.getElementById(id)) {return;}
  js = d.createElement('script'); js.id = id; js.async = true;
  js.src = "//connect.facebook.net/en_US/all.js";
  ref.parentNode.insertBefore(js, ref);
  }(document));
  
  // Init the SDK upon load
  window.fbAsyncInit = function() {
  FB.init({
  appId      : '437498466268409', // App ID
  status     : true, // check login status
  cookie     : true, // enable cookies to allow the server to access the session
  xfbml      : true  // parse XFBML
  });

  // listen for and handle auth.statusChange events
  FB.Event.subscribe('auth.statusChange', function(response) {
  if (response.authResponse) {
  // user has auth'd your app and is logged into Facebook
  } else {
  // user has not auth'd your app, or is not logged into Facebook
  document.getElementById('auth-loggedin').style.display = 'none';
  }
  });
  
        // respond to clicks on the login and logout links
        document.getElementById('sendbuttonFB').addEventListener('click', function(){
          FB.login(function(response) {
              noteAndDisplayAndPush();             
              });
           });

        // respond to clicks on the button to rate without posting on facebook
        document.getElementById('sendbutton').addEventListener('click', function(){
                       noteAndDisplay();             
           });
 // respond to clicks on the login and logout links
        document.getElementById('sendbuttonFB_debutant').addEventListener('click', function(){
          FB.login(function(response) {
              noteAndDisplayAndPush();             
              });
           });

        // respond to clicks on the button to rate without posting on facebook
        document.getElementById('sendbutton_debutant').addEventListener('click', function(){
                       noteAndDisplay();             
           });        
};

function noteAndDisplayAndPush(){
// call the rating webservice and load popup
      jQuery("#sendbutton").attr('disabled', true);
      jQuery("#sendbuttonFB").attr('disabled', true);
      var form = jQuery("#ratingForm");
      jQuery.post(
          form.attr('action') + ' #ajaxwrapper',
          form.serializeArray(),
          function(response) {
               //alert('reponse ajax');
               responseArray=eval(response);
               //alert (responseArray);
               noteMax=responseArray[0];    
               urlDSA=responseArray[1];
               jQuery("#sendbutton").attr('disabled', false);
               jQuery("#sendbuttonFB").attr('disabled', false);
               postRate();
               loadPopup();
               }
          );
       };

function noteAndDisplay(){
// call the rating webservice and load popup
      jQuery("#sendbutton").attr('disabled', true);
      jQuery("#sendbuttonFB").attr('disabled', true);
      var form = jQuery("#ratingForm");
      jQuery.post(
          form.attr('action') + ' #ajaxwrapper',
          form.serializeArray(),
          function(response) {
               //alert('reponse ajax');
               responseArray=eval(response);
               //alert (responseArray);
               noteMax=responseArray[0];    
               urlDSA=responseArray[1];
               jQuery("#sendbutton").attr('disabled', false);
               jQuery("#sendbuttonFB").attr('disabled', false);
               loadPopup();
               }
          );
       };

function postRate(){
//push to FB la note
  var acc_tok='';
  var url_pays='http://www.cinequant.com/open-rating?country='+pays+"&note="+noteMax;
  alert(url_pays);
  FB.api(
        '/me/openrating:rate',
        'post',
        { access_token:acc_tok,
  country: url_pays,  
  }, function(response) {
           if (!response || response.error) {
              alert('Error push FB');
           } else {
              alert('pushing rate on FB was successful! Action ID: ' + response.id);
           }
        });
  }