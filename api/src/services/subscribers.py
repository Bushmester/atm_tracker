from typing import Dict, List

from fastapi import WebSocket

from src.services.singleton import Singleton


class Subscribers(metaclass=Singleton):
    subscribers: Dict[str, Dict[str, List[WebSocket]]]
