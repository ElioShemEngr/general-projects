import promptSync from 'prompt-sync';
import { headerApp } from "./header.js";

export const initial = () => {
    const prompt = promptSync();
    
    headerApp;

    // Capturar datos del usuario
    console.log('¿Cuál es tu nombre?');
    let nombre = prompt('> ');

    console.log(`Bienvenido, ${nombre}!`);

    return nombre;
};
