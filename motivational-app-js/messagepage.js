import { quotes } from './quotes.js'

export const messageRandom  =  (userSel, nombre) => {
    const fecha = new Date();

// Obtener la fecha y la hora actual
const fechaYHora = fecha.toLocaleString(); // Usa el formato de fecha y hora local


console.log("============================================================");
console.log(`${fechaYHora}`);
console.log(" ");
console.log(`Hola ${nombre} `);
console.log(" ");

let number = Math.floor(Math.random() * quotes.work.length);

// Select
let option = userSel;

switch (option) {
    case '1':
        console.log('Frase para el Trabajo:');
        console.log(quotes.work[number].frase);
        console.log(' ');
        console.log('Autor :');
        console.log(quotes.work[number].autor);
        break;
    case '2':
        console.log('Frase para las Familia:');
        console.log(quotes.family[number].frase);
        console.log(' ');
        console.log('Autor :');
        console.log(quotes.family[number].autor);
        break;
    case '3':
        console.log('Frase para el Estudio :');
        console.log(quotes.study[number].frase);
        console.log(' ');
        console.log('Autor :');
        console.log(quotes.study[number].autor);
        break;
    default:
        console.log('Seleccion una opcion valida')
}
console.log("============================================================");
};


