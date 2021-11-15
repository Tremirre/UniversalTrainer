import sys
from enum import Enum


class Mode(Enum):
    TEST = 1
    TRAIN = 2
    LIST = 3
    QUIT = 4


def parse_input():
    args = sys.argv[1:]
    if not args:
        print("Default mode - Train")
        return Mode.TRAIN
    mode = sys.argv[1]
    if mode == "-test":
        print("Selected mode - Test")
        return Mode.TEST
    elif mode == "-list":
        print("Selected mode - List")
        return Mode.LIST
    elif mode == "-train":
        print("Selected mode - Train")
        return Mode.TRAIN
    else:
        print(f"Unsupported mode {mode} - the application will terminate")
        return Mode.QUIT
