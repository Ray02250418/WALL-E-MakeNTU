from multiprocessing import Process, Value, Array, cpu_count
from manager.userManager import userManager
from manager.modelManager import modelManager
import random
import time


if __name__ == '__main__':
    cpu_count = cpu_count()
    print("This machine has {} cpus.".format(cpu_count))
    
    # Sharing State
    userControl = Value('i', 0) # signed integer
    modelResult = Array('d', [0.0, 0.0, 0.0]) # double precision float
    # Define process
    userProcess = Process(target=userManager, args=(userControl, ))
    modelProcess = Process(target=modelManager, args=(modelResult, ))
    # Start the processes
    userProcess.start()
    modelProcess.start()
    
    while True:
        print("value: ", userControl.value)
        print("model result: ", modelResult[0], modelResult[1], modelResult[2])
        time.sleep(1)
        
    pass