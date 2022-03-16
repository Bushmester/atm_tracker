async def serializer_response(response):
    payloads = response["payload"]["clusters"]
    data = {}

    for payload in payloads:
        for atm in payload["points"]:
            address = atm["address"]
            for limits in atm["atmInfo"]["limits"]:
                # print(atm_info)
                currency = limits["currency"]
                amount = limits["amount"]

                data.setdefault(address, {}).setdefault(currency, amount)

    return data
