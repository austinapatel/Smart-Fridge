import requests

apikey = "01cf97dd"
appid = "b920660a822e1fddc5b10bdf50c890cf"
test = "https://api.edamam.com/api/food-database/parser?ingr=apple&app_id=b920660a822e1fddc5b10bdf50c890cf&app_key=01cf97dd"

response = requests.get("https://api.edamam.com/api/food-database/parser?ingr={}&app_id={}&app_key={}".format("apple", appid, apikey))
print(response.content)