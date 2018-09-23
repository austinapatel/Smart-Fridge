sample = '[{"apple": {"fat": 0.17, "carbs": 13.81, "calories": 52.0, "protein": 0.26}}, {"apple": {"fat": 0.17, "carbs": 13.81, "calories": 52.0, "protein": 0.26}}, {"tomato": {"fat": 0.2, "carbs": 3.89, "calories": 18.0, "protein": 0.88}}, {"apple": {"fat": 0.17, "carbs": 13.81, "calories": 52.0, "protein": 0.26}}]'

import json

d = json.loads(sample)

items = []
for item in d:
    items.append(list(item.keys())[0])

print("items:", items)

def get_nutrition(item, d, items):
    return d[items.index(item)][item]

print(get_nutrition('apple', d, items))