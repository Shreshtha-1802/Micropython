from machine import Pin, PWM
import time

# Define LED pins with PWM for smooth fading
led_pins = [15, 4, 5, 19]
leds = [PWM(Pin(pin), freq=500) for pin in led_pins]

# Function to fade LED smoothly
def fade_led(led, fade_in_time=0.03, fade_out_time=0.03):
    for duty in range(0, 1024, 64):  # Fade in
        led.duty(duty)
        time.sleep(fade_in_time)
    for duty in range(1023, -1, -64):  # Fade out
        led.duty(duty)
        time.sleep(fade_out_time)



while True:
    #Intro: Slow Fade In - Soft Glow (Like the Piano Part)
    fade_led(leds[0], 0.05, 0.05)
    fade_led(leds[1], 0.05, 0.05)
    fade_led(leds[2], 0.05, 0.05)
    fade_led(leds[3], 0.05, 0.05)
    time.sleep(0.2)

    #Verse: Pulse Effect (Like the Soft Beats)
    for _ in range(2):
        fade_led(leds[0], 0.02, 0.02)
        fade_led(leds[1], 0.02, 0.02)
        time.sleep(0.2)

    #Pre-Chorus: Faster Pulsing
    for _ in range(4):
        fade_led(leds[2], 0.01, 0.01)
        fade_led(leds[3], 0.01, 0.01)
        time.sleep(0.15)

    #CHORUS DROP: All LEDs Flashing in Sync
    for _ in range(6):
        for led in leds:
            led.duty(1023)  # Full brightness
        time.sleep(0.1)
        for led in leds:
            led.duty(0)  # Off
        time.sleep(0.1)

    #Post-Chorus: Slower Fade Out
    fade_led(leds[0], 0.05, 0.05)
    fade_led(leds[1], 0.05, 0.05)
    fade_led(leds[2], 0.05, 0.05)
    fade_led(leds[3], 0.05, 0.05)

    # Small pause before looping again
    time.sleep(0.5)
