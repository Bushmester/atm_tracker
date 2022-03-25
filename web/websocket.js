import {build_main_atm_content, build_sidebar} from "./services/build_html.js";
import {send_data_using_websocket} from "./services/send_data.js";


window.onload = async function (){
    await build_sidebar()

    const socket = new WebSocket("ws://0.0.0.0:8000/ws")
    document.getElementById('search btn').onclick = async () => {
        await send_data_using_websocket(socket)
    }
    socket.onmessage = async function (event) {
        event.data.text().then(async function (value) {
            let values = JSON.parse(value)
            let atms = []
            atms.push(values["old"])
            atms.push(values["updated"])
            atms.push(values["new"])

            await build_main_atm_content(atms)
        })
    }
}
