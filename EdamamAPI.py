import requests, json

appid = "01cf97dd"
apikey = "b920660a822e1fddc5b10bdf50c890cf"
test = "https://api.edamam.com/api/food-database/parser?ingr=apple&app_id=01cf97dd&app_key=b920660a822e1fddc5b10bdf50c890cf"

response = requests.get("https://api.edamam.com/api/food-database/parser?ingr={}&app_id={}&app_key={}".format("apple", appid, apikey))
#print(response.content.decode("utf-8"))

fooddata = json.loads(response.content.decode("utf-8"))
nutrientdata = fooddata["parsed"][0]["food"]["nutrients"]
food = fooddata["parsed"][0]["food"]["label"]

CALS = ('There are ' + str(nutrientdata['ENERC_KCAL']) + " calories in " + str(food) + ".")
CALS = CALS.lower().capitalize()
print(CALS)

PRTN = ('There are ' + str(nutrientdata['PROCNT']) + " grams of protein in in " + str(food) + ".")
PRTN = PRTN.lower().capitalize()
print(PRTN)

CALS = ('There are ' + str(nutrientdata['FAT']) + " calories in " + str(food) + ".")
CALS = CALS.lower().capitalize()
print(CALS)

CALS = ('There are ' + str(nutrientdata['CHOCD']) + " calories in " + str(food) + ".")
CALS = CALS.lower().capitalize()
print(CALS)