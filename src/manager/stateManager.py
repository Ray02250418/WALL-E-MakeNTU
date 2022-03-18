import time
from ..enum import detectResult, wallEState
from collections import deque
import time

class StateManager:
    def __init__(self):
        self.maxQueueLength = 50
        self.detectThresholdTime = 3
        self.emptyThresholdTime = 3
        self.fetchFrequency = 30
        self.prevDataID = None
        self.confidence = 0.0
        self.confidenceThreshold = 0.8
        self.detectQueue = deque([], self.maxQueueLength)
    
    def globalUpdate(self):
        globals().update(detectResult.__members__)
        globals().update(wallEState.__members__)
        
    def calConfidence(self):
        pass
        
    def stateManagerserver(self, userControl, modelResult, state):
        self.globalUpdate()
        print("Starting state manager server.")
        print("In state manager server: ", AUTOMATIC)
        # while True:
        #     DataID = modelResult[3]
            
        #     if DataID != self.prevDataID:    # Check if updated
        #         self.detectQueue.appendleft(modelResult[0])
        #     else: 
        #         time.sleep(1/self.fetchFrequency)
        #         continue
                
        time.sleep(1/self.fetchFrequency)


if __name__ == "__main__":
    pass