import time
from ..enum import detectResult, wallEState

def globalUpdate():
    globals().update(detectResult.__members__)
    globals().update(wallEState.__members__)
    
def stateManager(userControl, modelResult, state):
    globalUpdate()
    print("Starting state manager server.")


if __name__ == "__main__":
    pass