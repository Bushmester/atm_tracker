export async function get_data_from_sidebar() {
    let city = await document.getElementById('city').value

    let currencies = []
    let currency_check = await document.getElementsByName('currency_check').values()
    for (let currency of currency_check) {
        if (currency.checked) {
                currencies.push(currency.value)
        }
    }

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
        "currencies": currencies
    })
}
