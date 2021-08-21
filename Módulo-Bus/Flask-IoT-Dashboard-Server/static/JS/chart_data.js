var apikey = document.getElementById('apikey').value;
var devicename = "BUS12012";

// this function get information the device and draw in application
function getdevice(){
    var requests = $.get('/api/'+ apikey +'/deviceinfo/' + devicename);
    
    var tm = requests.done(function (result){
        
        document.getElementById("card-latitud").innerHTML = result[3];
        document.getElementById("card-longitud").innerHTML = result[4];
        document.getElementById("card-altitud").innerHTML = result[5];
        document.getElementById("card-speed").innerHTML = result[6];
        document.getElementById("card-pone").innerHTML = result[7];
        document.getElementById("card-ptwo").innerHTML = result[8];
        document.getElementById("card-pthree").innerHTML = result[9];
        document.getElementById("card-pfour").innerHTML = result[10];       
        setTimeout(getdevice, 2000);      
    
    });
    
}


getdevice();
