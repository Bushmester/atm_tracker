import {currencies, banks} from "../config.js"


export async function build_sidebar() {
    let currency_temp = await document.getElementById('currency-temp-id').content;

    for (let currency in currencies) {
        let copyHTML = await document.importNode(currency_temp, true)
        copyHTML.querySelector('input').setAttribute("value", currency)
        if (currency === "RUB") {
            copyHTML.querySelector('input').checked = true
        }
        copyHTML.querySelector('input').setAttribute("id", "currency-check "+ currency)
        copyHTML.querySelector('label').setAttribute("for", "currency-check "+ currency)
        copyHTML.querySelector('image').setAttribute("xlink:href", currencies[currency])
        copyHTML.getElementById('name_item_cur').textContent = currency
        await document.getElementById("currencies").appendChild(copyHTML)
    }

    let bank_temp = await document.getElementById('bank-temp-id').content;

    for (let bank in banks) {
        let copyHTML = await document.importNode(bank_temp, true)
        copyHTML.querySelector('input').setAttribute("value", bank)
        copyHTML.querySelector('input').setAttribute("id", "bank-check "+ bank)
        copyHTML.querySelector('label').setAttribute("for", "bank-check "+ bank)
        copyHTML.querySelector('img').setAttribute("src", banks[bank]["img"])
        copyHTML.getElementById('name_item_bank').textContent = bank
        await document.getElementById("banks").appendChild(copyHTML)
    }
}


export async function build_main_atm_content(atms) {
    let atm_info_temp = await document.getElementById("atm-info-temp-id").content;

    for (let atm of atms) {
        for (let address in atm) {
            let copyHTML = await document.importNode(atm_info_temp, true)
            copyHTML.getElementById("atm-info-address").textContent = address
            copyHTML.getElementById("atm-info-currency").textContent = atm[address]["currencies"][0]
            copyHTML.getElementById("atm-info-currency-amount").textContent = atm[address]["currencies"][1]
            await document.getElementById("main").appendChild(copyHTML)
        }
    }
}
