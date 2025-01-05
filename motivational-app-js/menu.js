import promptSync from 'prompt-sync';
import { headerApp } from "./header.js";

export const menuOption = () => {
    const prompt = promptSync();

    headerApp;

    console.log(" ");
    console.log("==       MENU      ==");
    console.log(" ");
    
    console.log("Elige una opcion :");
    // Capturar datos del usuario
    console.log('1) For Work');
    console.log('2) For Family');
    console.log('3) For Study');
    let select = prompt('> ');

    console.log(" ");
    console.log("Iniciando...");
    console.log(" ");
    setTimeout(() => {
        console.log(`Has elegido, ${select}!`);
    }, 2000);

    setTimeout(() => {
        console.clear();
    }, 5000);
};

