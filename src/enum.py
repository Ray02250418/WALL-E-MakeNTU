from enum import IntEnum

class userCommand(IntEnum):
    NONE = 0
    FRONT = 1
    BACK = 2
    LEFT = 3
    RIGHT = 4

class modelResult(IntEnum):
    EMPTY = 0
    DETECTED = 1
    
class wallEState(IntEnum):
    USERCONTROL = 0
    AUTOMATIC = 1
    pass
