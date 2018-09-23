from picamera import PiCamera
from time import sleep
from signal import pause

camera = PiCamera()

# Set up a gpiozero Button using the 4th pin on the vision hat expansion.
# button = Button(PIN_D)

# When the button is pressed, call the led.on() function (turn the led on)
camera.start_preview()
sleep(5)

camera.capture('/home/pi/Desktop/image.jpg')

# Wait for the user to kill the example.
# pause()

# When the button is released, call the led.off() function (turn the led off)
camera.stop_preview()

