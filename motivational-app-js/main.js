import { initial } from "./frontpage.js";
import { menuOption } from "./menu.js";
import { messageRandom } from "./messagepage.js";


let userNombre = initial();

let select = menuOption();

messageRandom(select, userNombre);

