from machine import Pin
import time
coil_A = Pin(12, Pin.OUT)
coil_B = Pin(13, Pin.OUT)
coil_C = Pin(14, Pin.OUT)
coil_D = Pin(15, Pin.OUT)

sequence = [[1 , 0 , 0 , 0] , [0 , 1 , 0 , 0] , [0 , 0, 1 , 0] , [0 , 0 , 0 , 1]]
while True:
    for step in sequence:
        coil_A.value(step[0])
        time.sleep(0.001)
        coil_B.value(step[1])
        time.sleep(0.001)
        coil_C.value(step[2])
        time.sleep(0.001)
        coil_D.value(step[3])
        time.sleep(0.001)



