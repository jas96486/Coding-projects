# This application is created to have connection between client side and server side in which they both connected to each other by using the help of vidstream libary.
from  vidstream import CameraClient # This vidstream is library in which you can create a camera function
from  vidstream import StreamingServer

import threading # Threading function is used to setup the target between server and client side
import time # time function is used to log the time between both sides like how much time they will connect to each other

r1 = StreamingServer('10.0.0.84',9999) # streaming server is a server address 
s1 = CameraClient('10.0.0.84',9999) # Cameraclient is a client address

t1 = threading.Thread(target=r1.start_server)
t1.start()  # start function is used to start the connection between server and client side

time.sleep(2)

t2 = threading.Thread(target=s1.start_stream)
t2.start()

while input("") != "STOP":
    continue

r1.stop_server() # stop function is used to stop the coonection between server and client side
s1.stop_stream()
