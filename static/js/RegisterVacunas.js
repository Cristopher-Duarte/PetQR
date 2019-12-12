
function hola(){
    
    v=[]

    var csrftoken= $("[name=csrfmiddlewaretoken]").val();
    select=document.getElementById("derecha");
    NuR= document.getElementById("numeroregistro_id").value
    NuR_Date={'NumeroRegistro': NuR}
    v.push(NuR_Date)
	for(var i=0;i<select.length;i++)
	{
        console.log(select.options[i].value)
        v.push(select.options[i].value)
	
	}
    

   fetch("Register/", {
       method: "post",
       headers:{
           'acept':'application/json',
           'Content-Type': 'application/json',
           "X-CSRFToken": csrftoken
       },
       body: JSON.stringify(v)
   })
   .then( (Response)=>{
       console.log(v)

   });
}

document.getElementById("boton").addEventListener("click", hola)


function Mover(valor){
    if (valor === 1) {
        var array = document.getElementById("izquierda");
        var arrayDos = document.getElementById("derecha");
        var seleccionar = array.selectedIndex;
        var seleccionarDos = arrayDos.options.length;
        if (seleccionar !=1) {
            var mover = array.options[seleccionar];
            arrayDos.options[seleccionarDos] = new Option(mover.text, mover.value);
            array.options[seleccionar] = null;
        }

    }else if(valor === 2){

            var array = document.getElementById("derecha");
            var arrayDos = document.getElementById("izquierda");
            var seleccionar = array.selectedIndex;
            var seleccionarDos = arrayDos.options.length;
            if (seleccionar !=1) {
                var mover = array.options[seleccionar];
                arrayDos.options[seleccionarDos] = new Option(mover.text, mover.value);
                array.options[seleccionar] = null;
            }
    }
}

