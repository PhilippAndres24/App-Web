document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario);
});


function validarFormulario(evento) {
    evento.preventDefault();
    //*   USUARIO    *//
    var usuario1 = "pepito97"
    var contrasena1 = "12345"
    
    //*   ADMIN    *//
    var usuario2 = "colasushi"
    var contrasena2 = "colasushi"

    var usuario = document.getElementById('user').value;
    if (!(usuario === usuario2) || (usuario.length < 7)) {
        alert('Usuario no Existe!');
        return;

    }

    var password = document.getElementById('pass').value;
    if (!(password === contrasena2) || (password.length < 4)) {
        alert('Contraseña Incorrecta!');
        return;
    }
    this.submit();
    alert('Inicio Sesion Con Exito');
}