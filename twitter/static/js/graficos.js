


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
            //
            $.ajax({
              url: '/json/menciones', //url de la acción symfony
              dataType: 'text', 
              success: function(data) //Si se ejecuta correctamente
              {
                var datos = $.parseJSON(data);
                window.myRadar = new Chart(document.getElementById("menciones").getContext("2d")).Doughnut(datos,{responsive: true});
              },
              error: function(data)
              {
                console.log("error");
              }
            });
            $.ajax({
              url: '/json/favoritos', //url de la acción symfony
              dataType: 'text', 
              success: function(data) //Si se ejecuta correctamente
              {
                var datos = $.parseJSON(data);
                
                window.myRadar = new Chart(document.getElementById("favoritos").getContext("2d")).Bar(datos, {responsive: true});
              },
              error: function(data)
              {
                console.log("error");
              }
            });
            
            window.myRadar = new Chart(document.getElementById("otros").getContext("2d")).Radar(radarChartData, {
              responsive: true
            });
          }
