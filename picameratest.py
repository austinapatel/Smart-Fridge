from picamera import PiCamera
from time import sleep
from signal import pause

camera = PiCamera()

# Set up a gpiozero Button using the 4th pin on the vision hat expansion.
# button = Button(PIN_D)

# When the button is pressed, call the led.on() function (turn the led on)
camera.start_preview()
sleep(5)

imagename = 'image.jpg'
path = '/home/pi/Desktop/' + imagename
camera.capture(path)
sleep(5)

# Wait for the user to kill the example.
# pause()

# When the button is released, call the led.off() function (turn the led off)
camera.stop_preview()

import boto.s3
import sys
from boto.s3.key import Key


AWS_ACCESS_KEY_ID = open('AWS_ACCESS_KEY_ID.txt').read()
AWS_SECRET_ACCESS_KEY = open('AWS_SECRET_ACCESS_KEY.txt').read()

bucket_name = 'smart-fridge-basehacks'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.get_bucket(bucket_name)


print('Uploading %s to Amazon S3 bucket %s' % (path, bucket_name))

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

# add new file
k = Key(bucket)
k.key = imagename
k.set_contents_from_filename(path, cb=percent_cb, num_cb=10)
print('done')