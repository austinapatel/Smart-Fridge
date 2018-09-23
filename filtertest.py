options = [['produce', 'apple', 'fruit', 'food', 'mcintosh'], ['produce', 'apple', 'fruit', 'granny smith', 'food', 'plant'], ['produce', 'potato and tomato genus', 'tomato', 'fruit', 'vegetable', 'plum tomato', 'bush tomato', 'nightshade family', 'apple'], ['food', 'produce'], ['produce', 'fruit', 'apple']]

new_options = []

for option in options:
    for o in option:
        if not (o == 'produce' or o == 'fruit' or o == 'food' or o == 'plant' or o == 'vegetable' or o == 'potato and tomato genus'):
            new_options.append(o)
            break

print(new_options)