import socket
import sys
import cv2
import pickle
import numpy as np
from model.detector import Detector

HOST = "10.10.2.238"
PORT = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

s.bind((HOST, PORT))
print("Socket bind complete")
s.listen(10)
print("Socket now listening")

conn, addr = s.accept()

detector = Detector(viewAngle=15, height=40, baseline=10)

while True:
    data = conn.recv(80)
    print(sys.getsizeof(data))
    frame = pickle.loads(data)
    print(frame)
    cv2.imshow("frame", frame)
