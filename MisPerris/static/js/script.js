//========== Script Propio de Mis Perris ==========//

function valida_datos() {
    if (document.fdatos.email.value.length==0)
    {
        alert("Tiene que escribir su correo electronico");
        document.fdatos.email.focus();
        return 0;
    }

    if (document.fdatos.rut.value.length==0)
    {
        alert("Tiene que escribir su rut");
        document.fdatos.rut.focus();
        return 0;
    }

    if (document.fdatos.nombre.value.length==0)
    {
        alert("Tiene que escribir su nombre completo");
        document.fdatos.nombre.focus();
        return 0;
    }

    telefono = document.fdatos.telefono.value;
    telefono = validarnumero(telefono);
    document.fdatos.telefono.value=telefono;

    if (telefono=="")
    {
        alert("Debe ingresar un telefono valido");
        document.fdatos.telefono.focus();
        return 0;
    }
    else
    {
        if (telefono<0)
        {
            alert("Debe ser celular");
            document.fdatos.telefono.focus();
            return 0;
        }
    }

    if (document.fdatos.fnac.value.length==0)
    {
        alert("Tiene que digitar una fecha valida");
        document.fdatos.fnac.focus();
        return 0;
    }

    if (document.fdatos.region.selectedIndex==0)
    {
        alert("Debe seleccionar una region");
        document.fdatos.region.focus();
        return 0;
    }

    if (document.fdatos.ciudad.selectedIndex==0)
    {
        alert("Debe seleccionar una ciudad");
        document.fdatos.ciudad.focus();
        return 0;
    }

    if (document.fdatos.vivienda.selectedIndex==0)
    {
        alert("Debe seleccionar una vivienda");
        document.fdatos.vivienda.focus();
        return 0;
    }

    alert("Muchas gracias por enviar el formulario");
    document.fdatos.submit();
}

function validarnumero(valor){
    valor = parseInt(valor);
    if (isNaN(valor))
    {
        return "";
    }
    else
    {
        return valor;
    }
}