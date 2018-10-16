from enum import Enum
from collections import defaultdict


global_status = defaultdict(int)


RemoteStatus = Enum('RemoteStatus', [
    'COMPLETED',
    'DOWNLOADING',
    'INACTIVE',
    'UNKNOWN',
])


BetaStatus = Enum('BetaStatus', [
    'COMPLETED',
    'ENQUEUED',
    'FAILED',
    'IGNORED',
    'NEEDS_INPUT',
    'PROCESSING',
    'UNKNOWN',
    'WAITING',
])


def clear():
    global_status.clear()


def inc_key(key):
    global_status[key] += 1


def inc_enum_key(enum):
    print(str(enum))
    key = str(enum).split('.')[-1]
    inc_key(key)
