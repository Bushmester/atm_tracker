import {build_sidebar} from "./services/build_sidebar.js";
import {get_data_from_sidebar} from "./services/get_data.js";


window.onload = function (){
    build_sidebar()

    const socket = new WebSocket("ws://localhost:8000/ws/{client}")
    document.getElementById('search btn').onclick = () => {
        socket.send(get_data_from_sidebar())
    }
}
