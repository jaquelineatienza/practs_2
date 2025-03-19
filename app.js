const datos = [];

const n = parseInt(
  prompt("Ingrese el número de personas que desea cargar"),
  10
);

for (let i = 0; i < n; i++) {
  let nombre = prompt("Ingrese el nombre:");
  let edad = parseInt(prompt("Ingrese la edad:"), 10);
  let nota = parseFloat(prompt("Ingrese la nota:"));

  datos.push([nombre, edad, nota]);
}

const result = datos.sort((a, b) => b[2] - a[2]);
console.log(result);
