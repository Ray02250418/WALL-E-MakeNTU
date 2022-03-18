import random
import time

def modelManager(modelResult):
    print("Starting model manager server.")
    while True:
        for i in range(3):
            modelResult[i] = random.random()
        modelResult[3] = 0
        time.sleep(0.1)
        
if __name__ == '__main__':
    pass