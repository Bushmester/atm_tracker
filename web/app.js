import {build_sidebar} from "./services/build_sidebar.js";
import {send_data_using_websocket} from "./services/send_data.js";


window.onload = async function (){
    await build_sidebar()

    const socket = new WebSocket("ws://localhost:8000/ws/{client}")
    document.getElementById('search btn').onclick = async () => {
        await send_data_using_websocket(socket)
    }
}
