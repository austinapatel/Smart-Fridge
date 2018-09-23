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

if 'ENERC_KCAL' in nutrientdata.keys():
    CALS = ('There are ' + str(nutrientdata['ENERC_KCAL']) + " calories in " + str(food) + ".")
    CALS = CALS.lower().capitalize()
    print(CALS)

if 'PROCNT' in nutrientdata.keys():
    PRTN = ('There are ' + str(nutrientdata['PROCNT']) + " grams of protein in " + str(food) + ".")
    PRTN = PRTN.lower().capitalize()
    print(PRTN)

if 'FAT' in nutrientdata.keys():
    FaT = ('There are ' + str(nutrientdata['FAT']) + " grams of fat in " + str(food) + ".")
    FaT = FaT.lower().capitalize()
    print(FaT)

if 'CHOCDF' in nutrientdata.keys():
    CARBS = ('There are ' + str(nutrientdata['CHOCDF']) + " grams of carbohydrates in " + str(food) + ".")
    CARBS = CARBS.lower().capitalize()
    print(CARBS)

if 'CA' in nutrientdata.keys():
    CLCM = ('There are ' + str(nutrientdata['CA']) + " milligrams of Calcium in " + str(food) + ".")
    CLCM = CLCM.lower().capitalize()
    print(CLCM)

if 'CHOLE' in nutrientdata.keys():
    CLSTRL = ('There are ' + str(nutrientdata['CHOLE']) + " milligrams of cholestrol in " + str(food) + ".")
    CLSTRL = CLSTRL.lower().capitalize()
    print(CLSTRL)

if 'FAMS' in nutrientdata.keys():
    MONOFAT = ('There are ' + str(nutrientdata['FAMS']) + " grams of Monounsaturated Fat in " + str(food) + ".")
    MONOFAT = MONOFAT.lower().capitalize()
    print(MONOFAT)

if 'FAPU' in nutrientdata.keys():
    POLYFAT = ('There are ' + str(nutrientdata['FAPU']) + " grams of Polyunsaturated Fat in " + str(food) + ".")
    POLYFAT = POLYFAT.lower().capitalize()
    print(POLYFAT)

if 'FASAT' in nutrientdata.keys():
    SATFAT = ('There are ' + str(nutrientdata['FASAT']) + " grams of Saturated Fat in " + str(food) + ".")
    SATFAT = SATFAT.lower().capitalize()
    print(SATFAT)

if 'FATRN' in nutrientdata.keys():
    TRANFAT = ('There are ' + str(nutrientdata['FATRN']) + " grams of Trans Fat in " + str(food) + ".")
    TRANFAT = TRANFAT.lower().capitalize()
    print(TRANFAT)

if 'FE' in nutrientdata.keys():
    IRN = ('There are ' + str(nutrientdata['FE']) + " milligrams of iron in " + str(food) + ".")
    IRN = IRN.lower().capitalize()
    print(IRN)

if 'FIBTG' in nutrientdata.keys():
    FBR = ('There are ' + str(nutrientdata['FIBTG']) + " grams of fiber in " + str(food) + ".")
    FBR = FBR.lower().capitalize()
    print(FBR)

if 'K' in nutrientdata.keys():
    PTSM = ('There are ' + str(nutrientdata['K']) + " milligrams of potassium in " + str(food) + ".")
    PTSM = PTSM.lower().capitalize()
    print(PTSM)

if 'MG' in nutrientdata.keys():
    MGNSM = ('There are ' + str(nutrientdata['MG']) + " milligrams of magnesium in " + str(food) + ".")
    MGNSM = MGNSM.lower().capitalize()
    print(MGNSM)

if 'NA' in nutrientdata.keys():
    SDM = ('There are ' + str(nutrientdata['NA']) + " milligrams of sodium in " + str(food) + ".")
    SDM = SDM.lower().capitalize()
    print(SDM)

if 'SUGAR' in nutrientdata.keys():
    SGR = ('There are ' + str(nutrientdata['SUGAR']) + " grams of sugar in " + str(food) + ".")
    SGR = SGR.lower().capitalize()
    print(SGR)

if 'TOCPHA' in nutrientdata.keys():
    VitE = ('There are ' + str(nutrientdata['TOCPHA']) + " milligrams of Vitamin E in " + str(food) + ".")
    VitE = VitE.lower().capitalize()
    print(VitE)

if 'VITA_RAE' in nutrientdata.keys():
    VitA = ('There are ' + str(nutrientdata['VITA_RAE']) + " æ-grams of Vitamin A in " + str(food) + ".")
    VitA = VitA.lower().capitalize()
    print(VitA)

if 'VITB12' in nutrientdata.keys():
    VitB12 = ('There are ' + str(nutrientdata['VITB12']) + " æ-grams of Vitamin B12 in " + str(food) + ".")
    VitB12 = VitB12.lower().capitalize()
    print(VitB12)

if 'VITB6' in nutrientdata.keys():
    VitB6 = ('There are ' + str(nutrientdata['VITB6']) + " milligrams of Vitamin B6 in " + str(food) + ".")
    VitB6 = VitB6.lower().capitalize()
    print(VitB6)

if 'VITC' in nutrientdata.keys():
    VitC = ('There are ' + str(nutrientdata['VITC']) + " milligrams of Vitamin C in " + str(food) + ".")
    VitC = VitC.lower().capitalize()
    print(VitC)

if 'VITD' in nutrientdata.keys():
    VitD = ('There are ' + str(nutrientdata['VITD']) + " æ-grams of Vitamin D in " + str(food) + ".")
    VitD = VitD.lower().capitalize()
    print(VitD)

if 'VITK1' in nutrientdata.keys():
    VitK = ('There are ' + str(nutrientdata['VITK1']) + " æ-grams of Vitamin K in " + str(food) + ".")
    VitK = VitK.lower().capitalize()
    print(VitK)