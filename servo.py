from machine import Pin, PWM
import time

servo_motor = PWM(Pin(18), freq=50)  # Set PWM on GPIO 18, 50Hz for servo

while True:
    servo_motor.duty(30)
    print("Position 1")
    time.sleep(1)
    servo_motor.duty(128)
    print("Position 2")
    time.sleep(1)
