


$('#contact').on("submit" , function(e){
    e.preventDefault();
    request();
});


function request(){

    var inputs = $("#contact :input").serializeArray();
    console.log(inputs);
    $.ajax({
        type: "POST",
        url: $("#contact").attr("action"),
        data: {
            csrfmiddlewaretoken:inputs[0].value,
            name: inputs[1].value, 
            email: inputs[2].value,
            message: inputs[3].value,
        },
        dataType: "html",
        beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
            // antes de enviar la peticion
            console.log(" esperando...");
        },
        success: function (response) {
            if(response == "success"){
                new swal("Correcto!", "El mensaje se envió con exito", "success");
            }
            console.log(response);
            console.log("verdad");
        },
        error: function (response) {
            
            console.log("error")
        }
    });
}