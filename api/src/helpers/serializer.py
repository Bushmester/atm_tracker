async def serializer_response(response, config_currency):
    payloads = response["payload"]["clusters"]
    data = {}

    for payload in payloads:
        for atm in payload["points"]:
            address = atm["address"]
            try:
                for limits in atm["atmInfo"]["limits"]:
                    currency = limits["currency"]
                    if currency != config_currency:
                        continue
                    amount = limits["amount"]
                    data.setdefault(address, {}).setdefault("currencies", {}).setdefault(currency, amount)
            except KeyError:
                pass

    return data
