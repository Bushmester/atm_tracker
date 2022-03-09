import currencies from "./config"
import banks from "./config"


export function build_sidebar() {
    let currency_temp = document.getElementById('currency-temp-id').content;

    for (let currency of currencies) {
        let copyHTML = document.importNode(currency_temp, true)
        copyHTML.querySelector('input').setAttribute("value", currency)
        copyHTML.querySelector('label').textContent = currency
        document.getElementById("currencies").appendChild(copyHTML)
    }

    let bank_temp = document.getElementById('bank-temp-id').content;

    for (let bank in banks) {
        console.log(bank)
        let copyHTML = document.importNode(bank_temp, true)
        copyHTML.querySelector('input').setAttribute("value", banks[bank])
        copyHTML.querySelector('label').textContent = bank
        document.getElementById("banks").appendChild(copyHTML)
    }
}
