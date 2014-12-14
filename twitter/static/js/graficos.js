xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      var jsonRespuesta = JSON.parse(responseText);
    //document.getElementById("json").innerHTML=xmlhttp.responseText;
    console.log(jsonRespuesta);
    /*window.myRadar = new Chart(document.getElementById("menciones").getContext("2d")).Doughnut(
              jsonRespuesta, {
              responsive: true
            });
    }*/
  }


var radarChartData = {
            labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
            datasets: [
              {
                label: "My First dataset",
                fillColor: "rgba(230,165,0,0.5)",
                strokeColor: "rgba(230,165,0,.8)",
                pointColor: "rgba(250,110,0,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [65,59,90,81,56,55,40]
              }
            ]
          };

          window.onload = function(){
            //xmlhttp.open("GET","/json/menciones",true);
            //xmlhttp.send();
            window.myRadar = new Chart(document.getElementById("favoritos").getContext("2d")).Bar(radarChartData, {
              responsive: true 
            });
            window.myRadar = new Chart(document.getElementById("otros").getContext("2d")).Radar(radarChartData, {
              responsive: true
            });
          }
