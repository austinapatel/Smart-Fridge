import requests, json
from googlecloudapi import *

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