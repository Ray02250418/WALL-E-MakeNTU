import random
import time

def userManager(userControl):
    print("Starting user manager server.")
    while True:
        userControl.value = random.randrange(10)
        time.sleep(0.1)
        
if __name__ == '__main__':
    pass