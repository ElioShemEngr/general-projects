import promptSync from 'prompt-sync';
import { headerApp } from "./header.js";

export const initial = () => {
    const prompt = promptSync();
    
    headerApp;

    // Capturar datos del usuario
    console.log('¿Cuál es tu nombre?');
    let nombre = prompt('> ');

    setTimeout(() => {
        console.log(`Bienvenido, ${nombre}!`);
    }, 2000);

    setTimeout(() => {
        console.clear();
    }, 5000);

    return nombre;
};
