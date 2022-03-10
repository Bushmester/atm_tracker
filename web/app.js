import {build_sidebar} from "./services/build_sidebar.js";
import {get_data_from_sidebar} from "./services/get_data.js";


window.onload = async function (){
    await build_sidebar()

    const socket = new WebSocket("ws://localhost:8000/ws/{client}")
    await document.getElementById('search btn').onclick = async () => {
        await socket.send(get_data_from_sidebar())
    }
}
