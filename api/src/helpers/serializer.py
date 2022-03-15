async def serializer_response(response):
    payloads = response["payload"]["cluster"]
    data = {}

    for payload in payloads:
        for atm in payload["points"]:
            address = await atm["address"]
            for atm_info in atm:
                for limits in atm_info:
                    currency = await limits["currency"]
                    amount = await limits["amount"]

                    await data.setdefault(address, {}).setdefault(currency, amount)

    return data
