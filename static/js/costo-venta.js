function calculateCost() {
    // Obtener valores de los campos existentes
    var laborCost = parseFloat(document.getElementById('laborCost').value) || 0;
    var indCost = parseFloat(document.getElementById('indCost').value) || 0;
    
    // Calcular varCost, unitCost, y rateCIF
    var varCost = laborCost * 0.3;
    var unitCost = laborCost + varCost;
    var rateCIF = Math.round(indCost / laborCost) ;
    
    // Asignar valores calculados a los campos correspondientes
    document.getElementById('varCost').value = varCost.toFixed(2);
    document.getElementById('unitCost').value = unitCost.toFixed(2);
    document.getElementById('rateCIF').value = rateCIF.toFixed(2);

    // Calcular el CIF y el costo de venta
    var CIF = unitCost * (rateCIF/100);
    var saleCost = CIF + unitCost;

    document.getElementById('CIF').value = CIF.toFixed(2);
    document.getElementById('saleCost').value = saleCost.toFixed(2);
}