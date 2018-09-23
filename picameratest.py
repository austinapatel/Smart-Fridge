from picamera import PiCamera
from time import sleep
from signal import pause

camera = PiCamera()

# Set up a gpiozero Button using the 4th pin on the vision hat expansion.
# button = Button(PIN_D)

# When the button is pressed, call the led.on() function (turn the led on)
camera.start_preview()
sleep(5)

filename = 'content.txt'
path = '/home/pi/Desktop/' + filename
camera.capture(path)
sleep(5)

# Wait for the user to kill the example.
# pause()

# When the button is released, call the led.off() function (turn the led off)
camera.stop_preview()

# cloud api ------------------------------------------

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient.from_service_account_json('Smart Fridge.json')

# The name of the image file to annotate
file_name = os.path.join(os.path.dirname(__file__),'Apple.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image = image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)


# get nutrition facts ------------------------------------------
import requests, json

linkfood = labels[2].description.lower()
appid = "01cf97dd"
apikey = "b920660a822e1fddc5b10bdf50c890cf"
test = "https://api.edamam.com/api/food-database/parser?ingr=apple&app_id=01cf97dd&app_key=b920660a822e1fddc5b10bdf50c890cf"

response = requests.get("https://api.edamam.com/api/food-database/parser?ingr={}&app_id={}&app_key={}".format(linkfood, appid, apikey))
(response.content.decode("utf-8"))

fooddata = json.loads(response.content.decode("utf-8"))
nutrientdata = fooddata["parsed"][0]["food"]["nutrients"]
food = fooddata["parsed"][0]["food"]["label"]

CALS = ('There are ' + str(nutrientdata['ENERC_KCAL']) + " calories in " + str(food) + ".")
CALS = CALS.lower().capitalize()
print(CALS)

PRTN = ('There are ' + str(nutrientdata['PROCNT']) + " grams of protein in " + str(food) + ".")
PRTN = PRTN.lower().capitalize()
print(PRTN)

FaT = ('There are ' + str(nutrientdata['FAT']) + " grams of fat in " + str(food) + ".")
FaT = FaT.lower().capitalize()
print(FaT)

CARBS = ('There are ' + str(nutrientdata['CHOCDF']) + " grams of carbohydrates in " + str(food) + ".")
CARBS = CARBS.lower().capitalize()
print(CARBS)

if 'CA' in nutrientdata:
    CLCM = ('There are ' + str(nutrientdata['CA']) + " milligrams of Calcium in " + str(food) + ".")
    CLCM = CLCM.lower().capitalize()
    print(CLCM)

if 'CHOLE' in nutrientdata:
    CLSTRL = ('There are ' + str(nutrientdata['CHOLE']) + " milligrams of cholestrol in " + str(food) + ".")
    CLSTRL = CLSTRL.lower().capitalize()
    print(CLSTRL)

if 'MONOFAT' in nutrientdata:
    MONOFAT = ('There are ' + str(nutrientdata['FAMS']) + " grams of Monounsaturated Fat in " + str(food) + ".")
    MONOFAT = MONOFAT.lower().capitalize()
    print(MONOFAT)

if 'POLYFAT' in nutrientdata:
    POLYFAT = ('There are ' + str(nutrientdata['FAPU']) + " grams of Polyunsaturated Fat in " + str(food) + ".")
    POLYFAT = POLYFAT.lower().capitalize()
    print(POLYFAT)

if 'SATFAT' in nutrientdata:
    SATFAT = ('There are ' + str(nutrientdata['FASAT']) + " grams of Saturated Fat in " + str(food) + ".")
    SATFAT = SATFAT.lower().capitalize()
    print(SATFAT)

if 'MONOFAT' in nutrientdata:
    TRANFAT = ('There are ' + str(nutrientdata['FATRN']) + " grams of Trans Fat in " + str(food) + ".")
    TRANFAT = TRANFAT.lower().capitalize()
    print(TRANFAT)

if 'IRN' in nutrientdata:
    IRN = ('There are ' + str(nutrientdata['FE']) + " milligrams of iron in " + str(food) + ".")
    IRN = IRN.lower().capitalize()
    print(IRN)

if 'FBR' in nutrientdata:
    FBR = ('There are ' + str(nutrientdata['FIBTG']) + " grams of fiber in " + str(food) + ".")
    FBR = FBR.lower().capitalize()
    print(FBR)

if 'PTSM' in nutrientdata:
    PTSM = ('There are ' + str(nutrientdata['K']) + " milligrams of potassium in " + str(food) + ".")
    PTSM = PTSM.lower().capitalize()
    print(PTSM)


    MGNSM = ('There are ' + str(nutrientdata['MG']) + " milligrams of magnesium in " + str(food) + ".")
    MGNSM = MGNSM.lower().capitalize()
    print(MGNSM)


    SDM = ('There are ' + str(nutrientdata['NA']) + " milligrams of sodium in " + str(food) + ".")
    SDM = SDM.lower().capitalize()
    print(SDM)


    SGR = ('There are ' + str(nutrientdata['SUGAR']) + " grams of sugar in " + str(food) + ".")
    SGR = SGR.lower().capitalize()
    print(SGR)


    VitE = ('There are ' + str(nutrientdata['TOCPHA']) + " milligrams of Vitamin E in " + str(food) + ".")
    VitE = VitE.lower().capitalize()
    print(VitE)


    VitA = ('There are ' + str(nutrientdata['VITARAE']) + " æ-grams of Vitamin A in " + str(food) + ".")
    VitA = VitA.lower().capitalize()
    print(VitA)


    VitB12 = ('There are ' + str(nutrientdata['VITB12']) + " æ-grams of Vitamin B12 in " + str(food) + ".")
    VitB12 = VitB12.lower().capitalize()
    print(VitB12)


    VitB6 = ('There are ' + str(nutrientdata['VITB6']) + " milligrams of Vitamin B6 in " + str(food) + ".")
    VitB6 = VitB6.lower().capitalize()
    print(VitB6)


    VitC = ('There are ' + str(nutrientdata['VITC']) + " milligrams of Vitamin C in " + str(food) + ".")
    VitC = VitC.lower().capitalize()
    print(VitC)


    VitD = ('There are ' + str(nutrientdata['VITD']) + " æ-grams of Vitamin D in " + str(food) + ".")
    VitD = VitD.lower().capitalize()
    print(VitD)


    VitK = ('There are ' + str(nutrientdata['VITK1']) + " æ-grams of Vitamin K in " + str(food) + ".")
    VitK = VitK.lower().capitalize()
    print(VitK)


# save data to file
f = open(path, "w")
f.write("calories" + CALS)

# upload to s3 ------------------------------------------

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
k.key = filename
k.set_contents_from_filename(path, cb=percent_cb, num_cb=10)
print('done')