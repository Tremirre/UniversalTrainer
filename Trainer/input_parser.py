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
        return Mode.TRAIN, 20
    mode = args[0]
    if mode == "-test":
        print("Selected mode - Test")
        if len(args) < 2 or not args[1].isnumeric():
            print("Chosen test size:", 20)
            return Mode.TEST, 20
        elif int(args[1]) > 0:
            print("Chosen test size:", test_size := int(args[1]))
            return Mode.TEST, test_size
        print(f"Unsupported argument as number of questions:", args[1], "\nThe application will terminate")
        return Mode.QUIT, 0
    elif mode == "-list":
        print("Selected mode - List")
        return Mode.LIST, 20
    elif mode == "-train":
        print("Selected mode - Train")
        return Mode.TRAIN, 20
    else:
        print(f"Unsupported mode {mode} - the application will terminate")
        return Mode.QUIT, 0
