from datetime import timedelta
from enum import Enum


class ActionEnum(Enum):
    ACTIVATE = ('activate', timedelta(days=1))
    RESET = ('reset', timedelta(minutes=5))

    def __init__(self, token_type, ext_time):
        self.token_type = token_type
        self.ext_time = ext_time
