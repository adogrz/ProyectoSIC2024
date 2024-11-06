// Función para actualizar el campo UUCP con la suma de totalProduct y totalProduct2
function updateUUCP() {
    const totalProduct = parseFloat(document.getElementById("totalProduct").textContent) || 0;
    const totalProduct2 = parseFloat(document.getElementById("totalProduct2").textContent) || 0;
    const uucpTotal = totalProduct + totalProduct2;
    document.getElementById("PA").textContent = totalProduct;
    document.getElementById("PCU").textContent = totalProduct2;
    document.getElementById("uucp").textContent = uucpTotal;
   
}

// Funciones para manejar la tabla 1-Casos de uso sin ajuste
function saveTableData1() {
    const rows = Array.from(document.querySelectorAll("#actorsTable1 tbody tr")).map(row => {
        return {
            casoUso: row.cells[0].textContent,
            complejidad: row.cells[1].querySelector("select").value,
            peso: row.cells[2].querySelector("select").value,
            cantidad: row.cells[3].querySelector("input[type='number']").value,
            producto: row.cells[4].querySelector("input[type='number']").value
        };
    });
    localStorage.setItem("tableData1", JSON.stringify(rows));
}
// Funciones para manejar la tabla 1-Casos de uso sin ajuste
function loadTableData1() {
    const rowsData = JSON.parse(localStorage.getItem("tableData1")) || [];
    const tableBody = document.querySelector("#actorsTable1 tbody");
    tableBody.innerHTML = "";

    rowsData.forEach(data => {
        const newRow = tableBody.insertRow();

        const cellCaso = newRow.insertCell();
        cellCaso.contentEditable = "true";
        cellCaso.textContent = data.casoUso;
        cellCaso.oninput = saveTableData1;

        const cellComplejidad = newRow.insertCell();
        const selectComplejidad = document.createElement("select");
        ["Selecciona","Simple", "Medio", "Complejo"].forEach(optionText => {
            const option = document.createElement("option");
            option.value = optionText;
            option.text = optionText;
            if (optionText === data.complejidad) option.selected = true;
            selectComplejidad.appendChild(option);
        });
        selectComplejidad.onchange = () => {
            calculateProduct(selectComplejidad);
            saveTableData1();
        };
        cellComplejidad.appendChild(selectComplejidad);

        const cellPeso = newRow.insertCell();
        const selectPeso = document.createElement("select");
        ["Selecciona","5", "10", "15"].forEach(optionText => {
            const option = document.createElement("option");
            option.value = optionText;
            option.text = optionText;
            if (optionText === data.peso) option.selected = true;
            selectPeso.appendChild(option);
        });
        selectPeso.onchange = () => {
            calculateProduct(selectPeso);
            saveTableData1();
        };
        cellPeso.appendChild(selectPeso);

        const cellCantidad = newRow.insertCell();
        const inputCantidad = document.createElement("input");
        inputCantidad.type = "number";
        inputCantidad.value = data.cantidad;
        inputCantidad.oninput = () => {
            calculateProduct(inputCantidad);
            saveTableData1();
        };
        cellCantidad.appendChild(inputCantidad);

        const cellProducto = newRow.insertCell();
        const inputProducto = document.createElement("input");
        inputProducto.type = "number";
        inputProducto.value = data.producto;
        inputProducto.readOnly = true;
        cellProducto.appendChild(inputProducto);
    });
    calculateTotal();
}
// Funciones para manejar la tabla 1-Casos de uso sin ajuste
function addRow1() {
    const tableBody = document.querySelector("#actorsTable1 tbody");
    const newRow = tableBody.insertRow();

    const cellCaso = newRow.insertCell();
    cellCaso.contentEditable = "true";
    cellCaso.oninput = saveTableData1;

    const cellComplejidad = newRow.insertCell();
    const selectComplejidad = document.createElement("select");
    ["Selecciona","Simple", "Medio", "Complejo"].forEach(optionText => {
        const option = document.createElement("option");
        option.value = optionText;
        option.text = optionText;
        selectComplejidad.appendChild(option);
    });
    selectComplejidad.onchange = () => {
        calculateProduct(selectComplejidad);
        saveTableData1();
    };
    cellComplejidad.appendChild(selectComplejidad);

    const cellPeso = newRow.insertCell();
    const selectPeso = document.createElement("select");
    ["Selecciona","5", "10", "15"].forEach(optionText => {
        const option = document.createElement("option");
        option.value = optionText;
        option.text = optionText;
        selectPeso.appendChild(option);
    });
    selectPeso.onchange = () => {
        calculateProduct(selectPeso);
        saveTableData1();
    };
    cellPeso.appendChild(selectPeso);

    const cellCantidad = newRow.insertCell();
    const inputCantidad = document.createElement("input");
    inputCantidad.type = "number";
    inputCantidad.oninput = () => {
        calculateProduct(inputCantidad);
        saveTableData1();
    };
    cellCantidad.appendChild(inputCantidad);

    const cellProducto = newRow.insertCell();
    const inputProducto = document.createElement("input");
    inputProducto.type = "number";
    inputProducto.readOnly = true;
    cellProducto.appendChild(inputProducto);

    saveTableData1();
}
// Función para eliminar la última fila de la tabla 1
function deleteLastRow1() {
    const tableBody = document.querySelector("#actorsTable1 tbody");
    if (tableBody.rows.length > 0) {
        tableBody.deleteRow(tableBody.rows.length - 1); // Eliminar la última fila
        calculateTotal(); // Recalcular el total
        saveTableData1(); // Guardar el estado actualizado en localStorage
    }
}
function calculateProduct(element) {
    const row = element.closest('tr');
    const peso = parseFloat(row.cells[2].querySelector("select").value) || 0;
    const cantidad = parseFloat(row.cells[3].querySelector("input").value) || 0;
    const producto = peso * cantidad;
    row.cells[4].querySelector("input").value = producto;
    calculateTotal();
    saveTableData1();
}
function calculateTotal() {
    const tableBody = document.querySelector("#actorsTable1 tbody");
    let total = 0;
    Array.from(tableBody.rows).forEach(row => {
        total += parseFloat(row.cells[4].querySelector("input").value) || 0;
    });
    document.getElementById("totalProduct").textContent = total;
    updateUUCP();
}
// Funciones para la tabla 2
function saveTableData2() {
    const rows = Array.from(document.querySelectorAll("#actorsTable2 tbody tr")).map(row => {
        return {
            actores: row.cells[0].textContent,
            tipoActor: row.cells[1].querySelector("select").value,
            peso: row.cells[2].querySelector("select").value,
            cantidad: row.cells[3].querySelector("input[type='number']").value,
            producto: row.cells[4].querySelector("input[type='number']").value
        };
    });
    localStorage.setItem("tableData2", JSON.stringify(rows));
}
function loadTableData2() {
    const rowsData = JSON.parse(localStorage.getItem("tableData2")) || [];
    const tableBody = document.querySelector("#actorsTable2 tbody");
    tableBody.innerHTML = "";

    rowsData.forEach(data => {
        const newRow = tableBody.insertRow();

        const cellActores = newRow.insertCell();
        cellActores.contentEditable = "true";
        cellActores.textContent = data.actores;
        cellActores.oninput = saveTableData2;

        const cellTipoActor = newRow.insertCell();
        const selectTipoActor = document.createElement("select");
        ["Selecciona","Simple", "Medio", "Complejo"].forEach(optionText => {
            const option = document.createElement("option");
            option.value = optionText;
            option.text = optionText;
            if (optionText === data.tipoActor) option.selected = true;
            selectTipoActor.appendChild(option);
        });
        selectTipoActor.onchange = () => {
            calculateProduct2(selectTipoActor);
            saveTableData2();
        };
        cellTipoActor.appendChild(selectTipoActor);

        const cellPeso = newRow.insertCell();
        const selectPeso = document.createElement("select");
        ["Selecciona",1, 2, 3].forEach(optionValue => {
            const option = document.createElement("option");
            option.value = optionValue;
            option.text = optionValue;
            if (optionValue === parseInt(data.peso)) option.selected = true;
            selectPeso.appendChild(option);
        });
        selectPeso.onchange = () => {
            calculateProduct2(selectPeso);
            saveTableData2();
        };
        cellPeso.appendChild(selectPeso);

        const cellCantidad = newRow.insertCell();
        const inputCantidad = document.createElement("input");
        inputCantidad.type = "number";
        inputCantidad.value = data.cantidad;
        inputCantidad.oninput = () => {
            calculateProduct2(inputCantidad);
            saveTableData2();
        };
        cellCantidad.appendChild(inputCantidad);

        const cellProducto = newRow.insertCell();
        const inputProducto = document.createElement("input");
        inputProducto.type = "number";
        inputProducto.value = data.producto;
        inputProducto.readOnly = true;
        cellProducto.appendChild(inputProducto);
    });
    calculateTotal2();
}
function addRow2() {
    const tableBody = document.querySelector("#actorsTable2 tbody");
    const newRow = tableBody.insertRow();

    const cellActores = newRow.insertCell();
    cellActores.contentEditable = "true";
    cellActores.oninput = saveTableData2;

    const cellTipoActor = newRow.insertCell();
    const selectTipoActor = document.createElement("select");
    ["Selecciona","Simple", "Medio", "Complejo"].forEach(optionText => {
        const option = document.createElement("option");
        option.value = optionText;
        option.text = optionText;
        selectTipoActor.appendChild(option);
    });
    selectTipoActor.onchange = () => {
        calculateProduct2(selectTipoActor);
        saveTableData2();
    };
    cellTipoActor.appendChild(selectTipoActor);

    const cellPeso = newRow.insertCell();
    const selectPeso = document.createElement("select");
    ["Selecciona",1, 2, 3].forEach(optionValue => {
        const option = document.createElement("option");
        option.value = optionValue;
        option.text = optionValue;
        selectPeso.appendChild(option);
    });
    selectPeso.onchange = () => {
        calculateProduct2(selectPeso);
        saveTableData2();
    };
    cellPeso.appendChild(selectPeso);

    const cellCantidad = newRow.insertCell();
    const inputCantidad = document.createElement("input");
    inputCantidad.type = "number";
    inputCantidad.oninput = () => {
        calculateProduct2(inputCantidad);
        saveTableData2();
    };
    cellCantidad.appendChild(inputCantidad);

    const cellProducto = newRow.insertCell();
    const inputProducto = document.createElement("input");
    inputProducto.type = "number";
    inputProducto.readOnly = true;
    cellProducto.appendChild(inputProducto);

    saveTableData2();
}
// Función para eliminar la última fila de la tabla 2
function deleteLastRow2() {
    const tableBody = document.querySelector("#actorsTable2 tbody");
    if (tableBody.rows.length > 0) {
        tableBody.deleteRow(tableBody.rows.length - 1); // Eliminar la última fila
        calculateTotal2(); // Recalcular el total
        saveTableData2(); // Guardar el estado actualizado en localStorage
    }
}
function calculateProduct2(element) {
    const row = element.closest('tr');
    const peso = parseFloat(row.cells[2].querySelector("select").value) || 0;
    const cantidad = parseFloat(row.cells[3].querySelector("input").value) || 0;
    const producto = peso * cantidad;
    row.cells[4].querySelector("input").value = producto;
    calculateTotal2();
    saveTableData2();
}
function calculateTotal2() {
    const tableBody = document.querySelector("#actorsTable2 tbody");
    let total = 0;
    Array.from(tableBody.rows).forEach(row => {
        total += parseFloat(row.cells[4].querySelector("input").value) || 0;
    });
    document.getElementById("totalProduct2").textContent = total;
    updateUUCP();
}
//Tabla 3 Factores técnicos 
// Array con multiplicadores específicos para cada evaluación
const multiplicationFactors = [2, 2, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 1, 1, 1];
// Función para calcular el impacto
function calculateImpact(index, selectedValue) {
    const multiplier = multiplicationFactors[index - 1];
    const impact = selectedValue * multiplier;

    // Actualizar la celda de impacto con el resultado calculado
    document.getElementById(`ImT${index}`).textContent = impact.toFixed(2);

    // Guardar el impacto individual en localStorage
    localStorage.setItem(`ImpactT${index}`, impact);

    // Actualizar la suma total de impactos
    updateTotalImpact();

    // Calcular el TCF
    calcularTCF();

    return impact;
}
// Función para calcular y mostrar la suma de todos los impactos
function updateTotalImpact() {
    let totalImpact = 0;

    // Sumar los valores de cada impacto desde el DOM
    for (let i = 1; i <= 13; i++) {
        const impactValue = parseFloat(document.getElementById(`ImT${i}`).textContent) || 0;
        totalImpact += impactValue;
    }
    // Mostrar el total en el campo 'totalTF'
    document.getElementById("totalTF").textContent = totalImpact.toFixed(2);

    // Guardar el total en localStorage
    localStorage.setItem("totalTF", totalImpact.toFixed(2));
    // Calcular el TCF
    calcularTCF();  
}
// Función para cargar los datos guardados y aplicar el cálculo
function loadSavedData() {
    for (let i = 1; i <= 13; i++) {
        const select = document.getElementById(`selectEvaT${i}`);
        const savedValue = localStorage.getItem(`EvaT${i}`);
        const savedImpact = localStorage.getItem(`ImpactT${i}`);

        if (savedValue !== null) {
            select.value = savedValue;
            document.getElementById(`ImT${i}`).textContent = parseFloat(savedImpact).toFixed(2);
        }
    }

    // Cargar el valor total guardado en 'totalTF'
    const savedTotal = localStorage.getItem("totalTF");
    if (savedTotal !== null) {
        document.getElementById("totalTF").textContent = savedTotal;
    }
}

// Cargar datos en la tabla 3
function loadTableData3() {
    for (let i = 1; i <= 13; i++) {
        const evaluationCell = document.getElementById(`EvaT${i}`);
        
        // Crear un select para las evaluaciones
        const select = document.createElement('select');
        select.id = `selectEvaT${i}`;
        select.innerHTML = `
            <option value="">Selecciona</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        `;

        // Evento para calcular y guardar el impacto al cambiar el valor
        select.addEventListener('change', function() {
            const selectedValue = parseInt(this.value);
            if (!isNaN(selectedValue)) {
                calculateImpact(i, selectedValue);
                localStorage.setItem(`EvaT${i}`, selectedValue); // Guardar el valor en localStorage
            } else {
                document.getElementById(`ImT${i}`).textContent = '';
                localStorage.removeItem(`EvaT${i}`);
                localStorage.removeItem(`ImpactT${i}`);
                updateTotalImpact(); // Recalcular el total si se borra un valor
            }
        });

        // Insertar el select en la celda de evaluación
        evaluationCell.appendChild(select);
    }
    // Cargar los datos guardados después de crear los selectores
    loadSavedData();
}
//calcular el tcf
function calcularTCF() {
    const totalTF = parseFloat(document.getElementById("totalTF").textContent) || 0;
    const tcf = 0.6 + (totalTF * 0.01);
    document.getElementById("tcf").textContent = tcf.toFixed(3);
    console.log(tcf);
    console.log(totalTF);
}

//Tabla 4 Factores ambientales
// Array con factores ambientales
const environmentFactors = [1.5, 0.5, 1, 0.5, 1, 2, -1, -1];
// Función para calcular el impacto
function calculateImpactEf(index, selectedValue) {
    const multiplier = environmentFactors[index - 1];
    const impact = selectedValue * multiplier;

    // Actualizar la celda de impacto con el resultado calculado
    document.getElementById(`ImEf${index}`).textContent = impact.toFixed(2);

    // Actualizar la suma total de impactos
    updateTotalImpactEf();
}

// Función para calcular y mostrar la suma de todos los impactos
function updateTotalImpactEf() {
    let totalImpact = 0;

    // Sumar los valores de cada impacto desde el DOM
    for (let i = 1; i <= environmentFactors.length; i++) {
        const impactValue = parseFloat(document.getElementById(`ImEf${i}`).textContent) || 0;
        totalImpact += impactValue;
    }

    // Mostrar el total en el campo 'totalEf'
    document.getElementById("totalEf").textContent = totalImpact.toFixed(2);

    // Calcular y mostrar el EF
    calcularEF(totalImpact);
}

// Función para calcular y mostrar el EF
function calcularEF(totalImpact) {
    const ef = 1.4 + (-0.03 * totalImpact);
    document.getElementById("totalEF").textContent = ef.toFixed(3);
}

// Función para cargar los datos en la tabla de factores ambientales
function loadTableData4() {
    for (let i = 1; i <= environmentFactors.length; i++) {
        const evaluationCell = document.getElementById(`EvaEf${i}`);
        
        // Crear un select para las evaluaciones
        const select = document.createElement('select');
        select.id = `selectEvaEf${i}`;
        select.innerHTML = `
            <option value="">Selecciona</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        `;

        // Recuperar y establecer el valor guardado en localStorage
        const savedValue = localStorage.getItem(`EvaEf${i}`);
        if (savedValue) {
            select.value = savedValue; // Establecer el valor guardado
            calculateImpactEf(i, parseInt(savedValue)); // Calcular impacto
        }

        // Evento para calcular el impacto al cambiar el valor
        select.addEventListener('change', function() {
            const selectedValue = parseInt(this.value);
            localStorage.setItem(`EvaEf${i}`, this.value); // Guardar el valor en localStorage
            if (!isNaN(selectedValue)) {
                calculateImpactEf(i, selectedValue); // Llamar a la función para calcular el impacto
            } else {
                document.getElementById(`ImEf${i}`).textContent = ''; // Limpiar el impacto si no se selecciona un valor
                updateTotalImpactEf(); // Recalcular el total si se borra un valor
            }
        });

        // Insertar el select en la celda de evaluación
        evaluationCell.appendChild(select);
    }
}
//Funcion para calcular el UCP
function calcularUCP() {
    const UUCP = parseFloat(document.getElementById("uucp").textContent) || 0;
    const TCF = parseFloat(document.getElementById("tcf").textContent) || 0;
    const EF = parseFloat(document.getElementById("totalEF").textContent) || 0;
    const UCP = UUCP * TCF * EF;
    document.getElementById("ttuucp").textContent = UUCP;
    document.getElementById("tttcf").textContent = TCF;
    document.getElementById("ttef").textContent = EF;
    document.getElementById("ttucp").textContent = UCP.toFixed(3);
}
// Función para cargar el selector de CF y el valor almacenado
function loadCFSelector() {
    const cfCell = document.getElementById("ttCF");

    // Crear un select para CF
    const selectCF = document.createElement('select');
    selectCF.id = 'selectCF';
    selectCF.innerHTML = `
        <option value="">Selecciona</option>
        <option value="20">20</option>
        <option value="28">28</option>
        <option value="36">36</option>
    `;

    // Recuperar valor de CF desde localStorage si existe
    const savedCF = localStorage.getItem("selectedCF");
    if (savedCF) {
        selectCF.value = savedCF;
    }

    // Evento para calcular E y guardar valor de CF al cambiar el valor de CF
    selectCF.addEventListener('change', function() {
        const selectedValue = selectCF.value;
        localStorage.setItem("selectedCF", selectedValue); // Guardar en localStorage
        calcularEsfuerzo(); // Calcular esfuerzo cada vez que cambia el valor
    });

    // Insertar el select en la celda de CF
    cfCell.appendChild(selectCF);
}

// Función para calcular el esfuerzo E
function calcularEsfuerzo() {
    const cfValue = parseInt(document.getElementById("selectCF").value) || 0;
    const ucpValue = parseFloat(document.getElementById("ttucp").textContent) || 0;
    const esfuerzoE = cfValue * ucpValue;

    // Actualizar la celda de esfuerzo E
    document.getElementById("tttUCP").textContent = ucpValue.toFixed(3);
    document.getElementById("ttE").textContent = esfuerzoE.toFixed(3);

    // Guardar esfuerzoE en localStorage
    localStorage.setItem("esfuerzoE", esfuerzoE.toFixed(3));

    // Calcular totales
    calcularTotalesEsfuerzo(esfuerzoE);
}

// Función para calcular totales de esfuerzo
function calcularTotalesEsfuerzo(esfuerzoE) {
    const totalHoras = esfuerzoE;
    const totalSemanas = totalHoras / 168;
    const totalMeses = totalSemanas / 4.345;
    document.getElementById("tth").textContent = totalHoras.toFixed(3);
    document.getElementById("tts").textContent = totalSemanas.toFixed(2);
    document.getElementById("ttm").textContent = totalMeses.toFixed(2);

    // Guardar valores en localStorage
    localStorage.setItem("totalHoras", totalHoras.toFixed(3));
    localStorage.setItem("totalSemanas", totalSemanas.toFixed(2));
    localStorage.setItem("totalMeses", totalMeses.toFixed(2));
}

// Función para cargar datos desde localStorage al iniciar
function loadStoredData() {
    // Cargar esfuerzoE
    const storedEsfuerzoE = localStorage.getItem("esfuerzoE");
    if (storedEsfuerzoE) {
        document.getElementById("ttE").textContent = storedEsfuerzoE;
    }

    // Cargar totales si existen
    const storedTotalHoras = localStorage.getItem("totalHoras");
    const storedTotalSemanas = localStorage.getItem("totalSemanas");
    const storedTotalMeses = localStorage.getItem("totalMeses");

    if (storedTotalHoras) document.getElementById("tth").textContent = storedTotalHoras;
    if (storedTotalSemanas) document.getElementById("tts").textContent = storedTotalSemanas;
    if (storedTotalMeses) document.getElementById("ttm").textContent = storedTotalMeses;
}

// Función para inicializar la tabla y el campo de entrada en em
function loadHorasPersonaTable() {
    const emCell = document.getElementById("em");

    // Crear un input numérico para Empleados Asignados
    const emInput = document.createElement('input');
    emInput.type = 'number';
    emInput.id = 'inputEm';
    emInput.style = 'width: 100%; text-align: center;';
    emInput.value = localStorage.getItem("emValue") || ""; // Cargar valor guardado en localStorage

    // Evento para calcular Total de Horas por Persona al cambiar Empleados Asignados
    emInput.addEventListener('input', function() {
        localStorage.setItem("emValue", emInput.value); // Guardar valor en localStorage
        calcularTotalHorasPersona(); // Calcular totalHP
    });

    // Insertar el input en la celda em
    emCell.appendChild(emInput);

    // Cargar horas totales en la celda eh desde tth y calcular totalHP
    const totalHoras = localStorage.getItem("totalHoras") || 0;
    document.getElementById("eh").textContent = totalHoras;

    // Guardar el valor en localStorage y calcular el valor de totalHP
    calcularTotalHorasPersona();
}

// Función para calcular el total de horas por persona
function calcularTotalHorasPersona() {
    const ehValue = parseFloat(document.getElementById("eh").textContent) || 0;
    const emValue = parseFloat(document.getElementById("inputEm").value) || 1; // Evitar división por cero

    const totalHP = ehValue / emValue;

    // Guardar totalHP en localStorage
    document.getElementById("temh").textContent = totalHP.toFixed(3);
    localStorage.setItem("totalHP", totalHP.toFixed(3));
}

// Función para cargar datos de localStorage
function loadStoredData() {
    // Cargar esfuerzoE y totales previos
    const storedEsfuerzoE = localStorage.getItem("esfuerzoE");
    if (storedEsfuerzoE) {
        document.getElementById("ttE").textContent = storedEsfuerzoE;
    }

    const storedTotalHoras = localStorage.getItem("totalHoras");
    if (storedTotalHoras) document.getElementById("tth").textContent = storedTotalHoras;

    const storedTotalHP = localStorage.getItem("totalHP");
    if (storedTotalHP) document.getElementById("temh").textContent = storedTotalHP;
}
function clearData() {
    localStorage.clear();
    location.reload();
}

// Función de inicialización al cargar la página
window.onload = () => {
    loadTableData1();
    loadTableData2();
    loadTableData3();
    loadTableData4();
    loadCFSelector();
    loadHorasPersonaTable(); 
    loadStoredData();
    updateTotalImpactEf();
    calcularTCF();
    calcularUCP();
    calcularEsfuerzo();
};