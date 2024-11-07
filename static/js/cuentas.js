document.addEventListener('DOMContentLoaded', function() {
    const listaPrincipal = document.getElementById('lista-principal');
    const listaSecundaria = document.getElementById('lista-secundaria');

    // Función para cargar cuentas desde el servidor
    function cargarCuentas(tipo) {
        fetch('/obtener-cuentas/')  // Asegúrate de que esta URL sea correcta
            .then(response => response.json())
            .then(data => {
                console.log('Cuentas obtenidas:', data);
                // Limpiar la lista secundaria
                listaSecundaria.innerHTML = '';
                listaSecundaria.innerHTML += '<option value="" disabled selected>Selecciona una cuenta</option>'; // Opción por defecto

                // Agregar cuentas a la lista secundaria según el tipo seleccionado
                if (tipo in data) {
                    data[tipo].forEach(cuenta => {
                        const option = document.createElement('option');
                        option.value = cuenta.codigo;  // Usa el código de la cuenta
                        option.textContent = `${cuenta.codigo} - ${cuenta.nombre}`; // Muestra el código y el nombre
                        listaSecundaria.appendChild(option);
                    });
                } else {
                    console.warn(`No se encontraron cuentas para el tipo: ${tipo}`);
                }
            })
            .catch(error => console.error('Error al cargar las cuentas:', error));
    }

    // Al cambiar la lista principal, carga las cuentas correspondientes
    listaPrincipal.addEventListener('change', function() {
        const tipoSeleccionado = listaPrincipal.value; // Obtener el valor seleccionado en lista principal
        cargarCuentas(tipoSeleccionado); // Cargar cuentas según el tipo seleccionado
    });

    // Cargar cuentas al iniciar la página si hay una opción seleccionada
    const tipoInicial = listaPrincipal.value; // Obtener el valor actualmente seleccionado
    if (tipoInicial) {
        cargarCuentas(tipoInicial); // Cargar cuentas iniciales
    }
});