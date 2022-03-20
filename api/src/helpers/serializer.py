async def serializer_response(response):
    payloads = response["payload"]["clusters"]
    data = {}

    for payload in payloads:
        for atm in payload["points"]:
            address = atm["address"]
            for limits in atm["atmInfo"]["limits"]:
                currency = limits["currency"]
                amount = limits["amount"]

                data.setdefault(address, {}).setdefault("currencies", {}).setdefault(currency, amount)

    return data
