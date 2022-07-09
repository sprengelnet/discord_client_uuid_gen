import base64
import time
from random import randint

import numpy as np


class UUID:
    increment = 0

    def __init__(self, token):
        try:
            value1 = (np.remainder(int(base64.b64decode(token.split('.')[0]).decode('utf-8')), 4294967296)).astype(np.int32)
            value2 = (int(base64.b64decode(token.split('.')[0]).decode('utf-8')) >> 32)
            value3 = randint(-2147483648, 2147483647)
            value4 = (np.remainder(round(time.time() * 1000), 4294967296)).astype(np.int32)
            value5 = (round(time.time() * 1000) >> 32)

            self.value1 = int(value1).to_bytes(4, byteorder="little", signed=True)
            self.value2 = value2.to_bytes(4, byteorder="little", signed=True)
            self.value3 = value3.to_bytes(4, byteorder="little", signed=True)
            self.value4 = int(value4).to_bytes(4, byteorder="little", signed=True)
            self.value5 = value5.to_bytes(4, byteorder="little", signed=True)
        except:
            return None

    def get(self):
        try:
            _increment = self.increment.to_bytes(4, byteorder="little", signed=True)
            uuid_bytes = np.frombuffer(self.value1 + self.value2 + self.value3 + self.value4 + self.value5 + _increment, dtype=np.uint8)
            uuid = base64.b64encode(uuid_bytes).decode("utf-8")

            self.increment += 1

            return uuid
        except:
            return None
