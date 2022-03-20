from helpers.singleton import Singleton


class Subscribers(metaclass=Singleton):
    def __init__(self):
        self.subscribers = {}
