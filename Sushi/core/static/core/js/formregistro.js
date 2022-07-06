document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario);
});


function validarFormulario(evento) {
    evento.preventDefault();

    var usuario = document.getElementById('user').value;
    if (usuario.length < 6) {
        alert('Debes ingresar un usuario de almenos 6 caracteres.');
        return;
    }
    var password = document.getElementById('pass').value;
    if (password.length < 4) {
        alert('Debes ingresar contraseña de almenos 4-8 caracteres ');
        return;
    }
    var email = document.getElementById('email').value;
    if (email.length < 6) {
        alert('Debes ingresar un email "valido xx@xx.com"');
        return;
    }
    var telefono = document.getElementById('telefono').value;
    if (telefono.length == 8) {
        alert('Debes ingresar un numero valido sin considerar "+569"');
        return;
    }
 
    var confirmcontr = document.getElementById('confirmcontr').value;
    if (!(confirmcontr == password) && (confirmcontr.length < 7))  {
        alert('Las contraseñas deben ser identicas y debe ser de almenos 4-8 caracteres');
        return;
    }
    this.submit();
    alert('Se ha registrado con exito.');

}