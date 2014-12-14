
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
            $.ajax({
              url: '/json/seguidores', //url de la acción symfony
              dataType: 'text', 
              success: function(data) //Si se ejecuta correctamente
              {
                var datos = $.parseJSON(data);
                
                window.myRadar = new Chart(document.getElementById("otros").getContext("2d")).Radar(datos, {responsive: true});
              },
              error: function(data)
              {
                console.log("error");
              }
            });
          }
