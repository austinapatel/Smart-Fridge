from picamera import PiCamera
from time import sleep
from signal import pause
from gpiozero import Button
from gpiozero import LED
from aiy.pins import LED_1
from aiy.pins import PIN_D

camera = PiCamera()

# Set up a gpiozero Button using the 4th pin on the vision hat expansion.
# button = Button(PIN_D)

# When the button is pressed, call the led.on() function (turn the led on)
camera.start_preview()
sleep(10)
# When the button is released, call the led.off() function (turn the led off)
camera.stop_preview()

# Wait for the user to kill the example.
pause()