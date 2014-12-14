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
            window.myRadar = new Chart(document.getElementById("menciones").getContext("2d")).Doughnut(
              [{
                  value: 300,
                  color:"#F7464A",
                  highlight: "#FF5A5E",
                  label: "Red"
              },
              {
                  value: 50,
                  color: "#46BFBD",
                  highlight: "#5AD3D1",
                  label: "Green"
              },
              {
                  value: 100,
                  color: "#FDB45C",
                  highlight: "#FFC870",
                  label: "Yellow"
              }]
              , {
              responsive: true
            });
            window.myRadar = new Chart(document.getElementById("favoritos").getContext("2d")).Bar(radarChartData, {
              responsive: true 
            });
            window.myRadar = new Chart(document.getElementById("otros").getContext("2d")).Radar(radarChartData, {
              responsive: true
            });
          }