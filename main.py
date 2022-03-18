from multiprocessing import Process, Value, Array, cpu_count
# from src.enum import userCommand, detectResult, wallEState
from src.enum import userCommand, detectResult, wallEState
from src.manager.userManager import userManager
from src.manager.modelManager import modelManager
from src.manager.stateManager import StateManager
import time

def globalUpdate():
    globals().update(userCommand.__members__)
    globals().update(detectResult.__members__)
    globals().update(wallEState.__members__)

if __name__ == '__main__':
    globalUpdate()
    cpu_count = cpu_count()
    print("This machine has {} cpus.".format(cpu_count))
    
    stateManager = StateManager()
    
    # Sharing State
    userControl = Value('i', NOCOMMAND) # user command
    modelResult = Array('d', [EMPTY, 0.0, 0.0, 0]) # model result [Yes/No, x, y, dataID]
    state = Value('i', USERCONTROL) # robot state
    # Define process
    userProcess = Process(target=userManager, args=(userControl, ))
    modelProcess = Process(target=modelManager, args=(modelResult, ))
    stateProcess = Process(target=stateManager.stateManagerserver, args=(userControl, modelResult, state))
    # Start the processes
    userProcess.start()
    modelProcess.start()
    stateProcess.start()
    
    while True:
        print("value: ", userControl.value)
        print("model result: ", modelResult[0], modelResult[1], modelResult[2])
        time.sleep(1)