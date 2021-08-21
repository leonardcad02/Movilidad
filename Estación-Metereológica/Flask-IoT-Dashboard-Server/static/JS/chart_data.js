var apikey = document.getElementById('apikey').value;
var devicename = "MET12012";

// this function get information the device and draw in application
function getdevice(){
    var requests = $.get('/api/'+ apikey +'/deviceinfo/' + devicename);
    
    var tm = requests.done(function (result){
        var today = new Date();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        addData(temperature_chart, time, result[3]);
        addData(humidity_chart, time, result[4]);
        addData(polution_chart, time, result[5]);
        addData(light_chart, time, result[6]);
        addData(noise_chart, time, result[7]);
        addData(pmone_chart, time, result[8]);
        addData(pmtwo_chart, time, result[9]);
        addData(pmten_chart, time, result[10]);
        document.getElementById("card-temperature").innerHTML = result[3];
        document.getElementById("card-humidity").innerHTML = result[4];
        document.getElementById("card-polution").innerHTML = result[5];
        document.getElementById("card-light").innerHTML = result[6];
        document.getElementById("card-noise").innerHTML = result[7];
        document.getElementById("card-pmone").innerHTML = result[8];
        document.getElementById("card-pmtwo").innerHTML = result[9];
        document.getElementById("card-pmten").innerHTML = result[10];
        if (couter >= 15 ){
            removeData(temperature_chart);
            removeData(humidity_chart);
            removeData(polution_chart);
            removeData(light_chart);
            removeData(noise_chart);
            removeData(pmone_chart);
            removeData(pmtwo_chart);
            removeData(pmten_chart);
        }
        couter++;
        setTimeout(getdevice, 5000);       
    
    });
    
}

//temperature chart object created 
var temperature = document.getElementById('temperature');
var temperature_chart = new Chart(temperature, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature vrs Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(244, 67, 54, 0.1)',
            borderColor:'rgba(244, 67, 54, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var humidity = document.getElementById('humidity');
var humidity_chart = new Chart(humidity, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Humidity Vrs Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(33, 150, 243, 0.1)',
            borderColor:'rgba(33, 150, 243, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var polution = document.getElementById('polution');
var polution_chart = new Chart(polution, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Polution vrs Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(0, 150, 136, 0.1)',
            borderColor:'rgba(0, 150, 136, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var light = document.getElementById('light');
var light_chart = new Chart(light, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Light vrs Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(255, 152, 0, 0.1)',
            borderColor:'rgba(255, 152, 0, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var noise = document.getElementById('noise');
var noise_chart = new Chart(noise, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Noise vrs Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(60, 81, 134, 0.1)',
            borderColor:'rgba(60, 81, 134, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var pmone = document.getElementById('pmone');
var pmone_chart = new Chart(pmone, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Air Pollution 1um W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(120, 122, 145, 0.1)',
            borderColor:'rgba(120, 122, 145, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var pmtwo = document.getElementById('pmtwo');
var pmtwo_chart = new Chart(pmtwo, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Air Pollution 2.5um W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(120, 122, 145, 0.1)',
            borderColor:'rgba(120, 122, 145, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var pmten = document.getElementById('pmten');
var pmten_chart = new Chart(pmten, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Air Pollution 10um W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(120, 122, 145, 0.1)',
            borderColor:'rgba(120, 122, 145, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}

var couter = 0; 

getdevice();
