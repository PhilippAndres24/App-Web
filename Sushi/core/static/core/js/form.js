document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario);
});


function validarFormulario(evento) {
    evento.preventDefault();
    var usuario = document.getElementById('user').value;
    var password = document.getElementById('pass').value;

    fetchAsync("http://localhost:8091/v1/departamento/gerencia/usuario/findByUsername/" + usuario, { mode: 'no-cors' }).then(function(data) {
        console.log('aqui');
        console.log(data);
        if (data.length === 0) {
            alert('Usuario no existe');
            return;
        }
        if (data.password !== password) {
            alert('Contraseña Incorrecta');
            return;
        }
        if (data.password === password) {
            alert('Bienvenido ' + data.username);
        }
        if (data.type == 0) {
            alert('Redireccionando a Panel de Administración')
            window.location.href = "http://localhost:8000/usuarios";
        }
        if (data.type != 0) {
            alert('Sesión Iniciada Exitosamente')
            window.location.href = "http://localhost:8000/indexlog";
        }
    });
}

async function fetchAsync(url) {
    let response = await fetch(url);
    let data = await response.json();
    return data;
}