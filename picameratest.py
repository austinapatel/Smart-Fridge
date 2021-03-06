from picamera import PiCamera
from time import sleep
import io
from random import random
import os

from signal import pause
from PIL import Image

import RPi.GPIO as GPIO
ledpin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin,GPIO.OUT)
GPIO.output(15,GPIO.LOW)

import json
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from signal import pause
import requests, json

import boto.s3
import sys
from boto.s3.key import Key

camera = PiCamera()

# Set up a gpiozero Button using the 4th pin on the vision hat expansion.
# button = Button(PIN_D)

# When the button is pressed, call the led.on() function (turn the led on)
camera.start_preview()
sleep(3)

try:
    while True:
        textfilename = 'content.txt'
        imagefilename = 'image.jpg'
        base = '/home/pi/Desktop/'
        imagepath = base + imagefilename
        textpath = base + textfilename


        camera.capture(imagepath)

        # Wait for the user to kill the example.
        # pause()

        # When the button is released, call the led.off() function (turn the led off)

        def crop(image_path, coords, saved_location):
            """
            @param image_path: The path to the image to edit
            @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
            @param saved_location: Path to save the cropped image
            """
            image_obj = Image.open(image_path)
            cropped_image = image_obj.crop(coords)
            cropped_image.save(base + saved_location)
            cropped_image.show()


        crop(imagepath, (0, 0, 230, 170), 'top_left.jpg')
        crop(imagepath, (0, 260, 185, 480), 'bottom_left.jpg')
        crop(imagepath, (200, 200, 350, 370), 'middle.jpg')
        crop(imagepath, (370, 270, 640, 480), 'bottom_right.jpg')
        crop(imagepath, (310, 100, 500, 300), 'top_right.jpg')

        names = ['top_left', 'bottom_left', 'middle', 'bottom_right', 'top_right']


        # Instantiates a client
        client = vision.ImageAnnotatorClient.from_service_account_json('Smart Fridge.json')

        image_label_list = []
        descriptions = []

        for i in range(len(names)):
            name = names[i]

            # cloud api ------------------------------------------

            # The name of the image file to annotate
            # file_name = os.path.join(os.path.dirname(__file__),'Apple.jpg')
            file_name = base + name + '.jpg'

            # Loads the image into memory
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            print('Labels: for', str(i))
            for c in labels:
                o = c.description
                print(o)
                if not (o == 'produce' or o == 'fruit' or o == 'food' or o == 'plant' or o == 'vegetable' or o == 'potato and tomato genus'):
                    # try:
                    # get nutrition facts ------------------------------------------


                    linkfood = o

                    appid = "01cf97dd"
                    apikey = "b920660a822e1fddc5b10bdf50c890cf"
                    test = "https://api.edamam.com/api/food-database/parser?ingr=apple&app_id=01cf97dd&app_key=b920660a822e1fddc5b10bdf50c890cf"

                    response = requests.get(
                        "https://api.edamam.com/api/food-database/parser?ingr={}&app_id={}&app_key={}".format(linkfood, appid,
                                                                                                              apikey))
                    (response.content.decode("utf-8"))


                    content = response.content.decode("utf-8")
                    if not content:
                        continue

                    try:

                        fooddata = json.loads(content)
                    except Exception as e:
                        continue

                    if len(fooddata['parsed']) == 0:
                        continue

                    nutrientdata = fooddata["parsed"][0]["food"]["nutrients"]
                    food = fooddata["parsed"][0]["food"]["label"]

                    CALS = nutrientdata['ENERC_KCAL']
                    print(CALS)

                    PRTN = nutrientdata['PROCNT']
                    print(PRTN)

                    FaT = nutrientdata['FAT']
                    print(FaT)

                    CARBS = nutrientdata['CHOCDF']
                    print(CARBS)

                    descriptions.append({linkfood: {'calories': CALS, 'protein': PRTN, 'fat': FaT, 'carbs': CARBS}})

                    # if 'CA' in nutrientdata:
                    #     CLCM = ('There are ' + str(nutrientdata['CA']) + " milligrams of Calcium in " + str(food) + ".")
                    #     CLCM = CLCM.lower().capitalize()
                    #     print(CLCM)
                    #
                    # if 'CHOLE' in nutrientdata:
                    #     CLSTRL = ('There are ' + str(nutrientdata['CHOLE']) + " milligrams of cholestrol in " + str(food) + ".")
                    #     CLSTRL = CLSTRL.lower().capitalize()
                    #     print(CLSTRL)
                    #
                    # if 'MONOFAT' in nutrientdata:
                    #     MONOFAT = ('There are ' + str(nutrientdata['FAMS']) + " grams of Monounsaturated Fat in " + str(food) + ".")
                    #     MONOFAT = MONOFAT.lower().capitalize()
                    #     print(MONOFAT)
                    #
                    # if 'POLYFAT' in nutrientdata:
                    #     POLYFAT = ('There are ' + str(nutrientdata['FAPU']) + " grams of Polyunsaturated Fat in " + str(food) + ".")
                    #     POLYFAT = POLYFAT.lower().capitalize()
                    #     print(POLYFAT)
                    #
                    # if 'SATFAT' in nutrientdata:
                    #     SATFAT = ('There are ' + str(nutrientdata['FASAT']) + " grams of Saturated Fat in " + str(food) + ".")
                    #     SATFAT = SATFAT.lower().capitalize()
                    #     print(SATFAT)
                    #
                    # if 'MONOFAT' in nutrientdata:
                    #     TRANFAT = ('There are ' + str(nutrientdata['FATRN']) + " grams of Trans Fat in " + str(food) + ".")
                    #     TRANFAT = TRANFAT.lower().capitalize()
                    #     print(TRANFAT)
                    #
                    # if 'IRN' in nutrientdata:
                    #     IRN = ('There are ' + str(nutrientdata['FE']) + " milligrams of iron in " + str(food) + ".")
                    #     IRN = IRN.lower().capitalize()
                    #     print(IRN)
                    #
                    # if 'FBR' in nutrientdata:
                    #     FBR = ('There are ' + str(nutrientdata['FIBTG']) + " grams of fiber in " + str(food) + ".")
                    #     FBR = FBR.lower().capitalize()
                    #     print(FBR)
                    #
                    # if 'PTSM' in nutrientdata:
                    #     PTSM = ('There are ' + str(nutrientdata['K']) + " milligrams of potassium in " + str(food) + ".")
                    #     PTSM = PTSM.lower().capitalize()
                    #     print(PTSM)
                    #
                    #
                    #     MGNSM = ('There are ' + str(nutrientdata['MG']) + " milligrams of magnesium in " + str(food) + ".")
                    #     MGNSM = MGNSM.lower().capitalize()
                    #     print(MGNSM)
                    #
                    #
                    #     SDM = ('There are ' + str(nutrientdata['NA']) + " milligrams of sodium in " + str(food) + ".")
                    #     SDM = SDM.lower().capitalize()
                    #     print(SDM)
                    #
                    #
                    #     SGR = ('There are ' + str(nutrientdata['SUGAR']) + " grams of sugar in " + str(food) + ".")
                    #     SGR = SGR.lower().capitalize()
                    #     print(SGR)
                    #
                    #
                    #     VitE = ('There are ' + str(nutrientdata['TOCPHA']) + " milligrams of Vitamin E in " + str(food) + ".")
                    #     VitE = VitE.lower().capitalize()
                    #     print(VitE)
                    #
                    #
                    #     VitA = ('There are ' + str(nutrientdata['VITARAE']) + " æ-grams of Vitamin A in " + str(food) + ".")
                    #     VitA = VitA.lower().capitalize()
                    #     print(VitA)
                    #
                    #
                    #     VitB12 = ('There are ' + str(nutrientdata['VITB12']) + " æ-grams of Vitamin B12 in " + str(food) + ".")
                    #     VitB12 = VitB12.lower().capitalize()
                    #     print(VitB12)
                    #
                    #
                    #     VitB6 = ('There are ' + str(nutrientdata['VITB6']) + " milligrams of Vitamin B6 in " + str(food) + ".")
                    #     VitB6 = VitB6.lower().capitalize()
                    #     print(VitB6)
                    #
                    #
                    #     VitC = ('There are ' + str(nutrientdata['VITC']) + " milligrams of Vitamin C in " + str(food) + ".")
                    #     VitC = VitC.lower().capitalize()
                    #     print(VitC)
                    #
                    #
                    #     VitD = ('There are ' + str(nutrientdata['VITD']) + " æ-grams of Vitamin D in " + str(food) + ".")
                    #     VitD = VitD.lower().capitalize()
                    #     print(VitD)
                    #
                    #
                    #     VitK = ('There are ' + str(nutrientdata['VITK1']) + " æ-grams of Vitamin K in " + str(food) + ".")
                    #     VitK = VitK.lower().capitalize()
                    #     print(VitK)
                    #


                    # except Exception as e:
                    #     pass

                    break


        print(json.dumps(descriptions))


        # save data to file
        f = open(textpath, "w")
        f.write(json.dumps(descriptions))
        f.close()

        # upload to s3 ------------------------------------------
        AWS_ACCESS_KEY_ID = open('AWS_ACCESS_KEY_ID.txt').read()
        AWS_SECRET_ACCESS_KEY = open('AWS_SECRET_ACCESS_KEY.txt').read()

        bucket_name = 'smart-fridge-basehacks'
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
                AWS_SECRET_ACCESS_KEY)

        bucket = conn.get_bucket(bucket_name)

        print('Uploading %s to Amazon S3 bucket %s' % (textpath, bucket_name))

        def percent_cb(complete, total):
            sys.stdout.write('.')
            sys.stdout.flush()

        # add new file
        k = Key(bucket)
        k.key = textfilename
        k.set_contents_from_filename(textpath, cb=percent_cb, num_cb=10)
        # print(str(options))

        print('done with update')

        GPIO.output(ledpin, GPIO.HIGH)
        sleep(3 + int(random() * 4))
        GPIO.output(ledpin, GPIO.LOW)

except KeyboardInterrupt as e:
    pass

camera.stop_preview()
GPIO.output(ledpin, GPIO.LOW)