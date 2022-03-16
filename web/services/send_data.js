import {get_data_from_sidebar} from "./get_data.js";

export async function send_data_using_websocket(socket) {
    await socket.send(await get_data_from_sidebar())
}
