export async function get_data_from_sidebar() {
    let city = await document.getElementById('city').value

    let currency = await document.querySelector('input[name="currency_check"]:checked').value

    let banks = []
    let bank_check = await document.getElementsByName('bank_check').values()
    for (let bank of bank_check) {
        if (bank.checked) {
            banks.push(bank.value)
        }
    }

    return JSON.stringify({
        "city": city,
        "banks": banks,
        "currency": currency
    })
}

export async function get_data_using_websocket(socket) {
    socket.onmessage = async function (event) {
        console.log(event.data)
    }
}
