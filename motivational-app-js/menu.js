import { headerApp } from "./header.js";
import promptSync from 'prompt-sync';

export const menuOption = () => {
    const prompt = promptSync();

    headerApp;

    console.log(" ");
    console.log("==       MENU      ==");
    console.log(" ");
    
    console.log("Elige una opcion :");
    // Capturar datos del usuario
    console.log('1) Para el Trabajo');
    console.log('2) Para la Familia');
    console.log('3) Para el Estudio');
    let select = prompt('> ');
    console.log(" ");
    console.log(`Has elegido, ${select}!`);
    console.log(" ");

    return select;
};


