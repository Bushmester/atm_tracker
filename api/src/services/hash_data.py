from hashlib import sha256
from typing import List


def hash_data(city: str, currency: str, banks: List[str]):
    data = city + currency + "".join(banks)
    return sha256(data.encode()).hexdigest()
