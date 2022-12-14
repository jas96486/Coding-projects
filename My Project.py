from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

r1 = StreamingServer('10.0.0.84',9999)
s1 = CameraClient('10.0.0.84',9999)

t1 = threading.Thread(target=r1.start_server)
t1.start()

time.sleep(2)

t2 = threading.Thread(target=s1.start_stream)
t2.start()

while input("") != "STOP":
    continue

r1.stop_server()
s1.stop_stream()