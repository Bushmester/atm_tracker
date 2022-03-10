import {currencies, banks} from "../config.js"


export async function build_sidebar() {
    let currency_temp = await document.getElementById('currency-temp-id').content;

    for (let currency of currencies) {
        let copyHTML = await document.importNode(currency_temp, true)
        copyHTML.querySelector('input').setAttribute("value", currency)
        copyHTML.querySelector('input').setAttribute("id", "currency-check "+ currency)
        copyHTML.querySelector('label').setAttribute("for", "currency-check "+ currency)
        copyHTML.querySelector('label').textContent = currency
        await document.getElementById("currencies").appendChild(copyHTML)
    }

    let bank_temp = await document.getElementById('bank-temp-id').content;

    for (let bank in banks) {
        let copyHTML = await document.importNode(bank_temp, true)
        copyHTML.querySelector('input').setAttribute("value", banks[bank])
        copyHTML.querySelector('input').setAttribute("id", "bank-check "+ bank)
        copyHTML.querySelector('label').setAttribute("for", "bank-check "+ bank)
        copyHTML.querySelector('label').textContent = bank
        await document.getElementById("banks").appendChild(copyHTML)
    }
}
