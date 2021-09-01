
$("#loginForm").on("submit" ,function(e){
    e.preventDefault();
    console.log("ESTOY INTENTANDO LOGEAR");
    var datica = $("#loginForm :input").serializeArray();
    console.log(datica);
    $.ajax({
        type: "POST",
        url: $("#loginForm").attr("action"),
        data: {
            csrfmiddlewaretoken:datica[0].value,
            username: datica[1].value,
            password: datica[2].value,
        },
        dataType: "html",
        beforeSend: function(response){   
           console.log("reealizando crud docente..");
       },
       success: function (response) {
           if(response == "correcto"){
               console.log("CORRECTO");
               window.open("/administracion","_self"); 
             }
       },
       error: function (response){
           console.log(response)
       },
   }); 
});