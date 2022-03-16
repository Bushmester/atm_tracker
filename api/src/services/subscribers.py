from typing import Dict, List, Union

from fastapi import WebSocket

from helpers.singleton import Singleton


class Subscribers(metaclass=Singleton):
    def __init__(self):
        self.subscribers: Dict[str, Dict[str, Union[Dict[str, Union[str, List[str]]], List[WebSocket]]]] = {}
