// static/js/obtener_montos.js

// static/js/obtener_montos.js

document.addEventListener('DOMContentLoaded', function() {
    fetch('/obtener_montos_json/')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Aquí puedes manejar los datos recibidos y actualizar la interfaz de usuario según sea necesario
            const catalogoCuentas = data.catalogo_cuentas;
            const totalDebe = data.total_debe;
            const totalHaber = data.total_haber;
            const totalSaldoDeudor = data.total_saldo_deudor;
            const totalSaldoAcreedor = data.total_saldo_acreedor;

            // Actualizar la tabla con los datos recibidos
            const tableBody = document.getElementById('tabla-cuentas-body');
            catalogoCuentas.forEach(cuenta => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${cuenta.nombreDeCuenta}</td>
                    <td>$ ${cuenta.debe.toFixed(2)}</td>
                    <td>$ ${cuenta.haber.toFixed(2)}</td>
                    <td>$ ${cuenta.saldo_deudor.toFixed(2)}</td>
                    <td>$ ${cuenta.saldo_acreedor.toFixed(2)}</td>
                `;
                tableBody.appendChild(row);
            });

            // Actualizar los totales
            document.getElementById('total-debe').textContent = `$ ${totalDebe.toFixed(2)}`;
            document.getElementById('total-haber').textContent = `$ ${totalHaber.toFixed(2)}`;
            document.getElementById('total-saldo-deudor').textContent = `$ ${totalSaldoDeudor.toFixed(2)}`;
            document.getElementById('total-saldo-acreedor').textContent = `$ ${totalSaldoAcreedor.toFixed(2)}`;
        })
        .catch(error => console.error('Error:', error));
});