from machine import Pin
import time

# Define LED pins
led_pins = [15, 4, 5, 19]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Define blink pattern for "Havana" beat
pattern = [
    (1, 0, 1, 0),  # LED 1 & 3 ON, LED 2 & 4 OFF
    (0, 1, 0, 1),  # LED 2 & 4 ON, LED 1 & 3 OFF
    (1, 1, 0, 0),  # LED 1 & 2 ON, LED 3 & 4 OFF
    (0, 0, 1, 1),  # LED 3 & 4 ON, LED 1 & 2 OFF
]

# Time delays to match the Havana rhythm
delays = [0.5, 0.5, 0.25, 0.25]  # Slow, slow, fast, fast

while True:
    for i in range(len(pattern)):
        for led, state in zip(leds, pattern[i]):
            led.value(state)
        time.sleep(delays[i])  # Wait according to the beat

