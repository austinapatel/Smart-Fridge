from signal import pause
from gpiozero import Button
from aiy.pins import PIN_D

# Set up a gpiozero Button using the 4th pin on the vision hat expansion.
button = Button(PIN_D)

# When the button is pressed, call the led.on() function (turn the led on)
button.when_pressed = lambda: print('pressed')
# When the button is released, call the led.off() function (turn the led off)
button.when_released = lambda: print('released')

# Wait for the user to kill the example.
pause()