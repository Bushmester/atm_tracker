from typing import Dict, List

from fastapi import WebSocket

from helpers.singleton import Singleton


class Subscribers(metaclass=Singleton):
    def __init__(self):
        self.subscribers: Dict[str, Dict[str, Dict[str, List[WebSocket]]]] = {}
