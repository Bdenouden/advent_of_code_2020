import sys

menu = []
allergen_options = dict()
ingredients = set()

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        i, a = line.strip(")\n").split(' (contains ')
        alist = a. split(', ')
        ilist = i.split(' ')
        menu.append({'i': ilist, 'a': alist})

        # add ingredients to ingredient list
        for i in ilist:
            ingredients.add(i)

        # add ingredients to allergen options if only a single allergen is mentioned for this meal
        if len(alist) == 1:
            for i in ilist:
                allergen_options.setdefault(alist[0], set()).add(i)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# cycle through all allergen options and keep only ingredients that occur everytime the allergen is present in the meal
for a, ilist in allergen_options.copy().items():
    for f in menu:
        if a in f['a']:
            allergen_options[a] = intersection(allergen_options[a], f['i'])

# remove ingredients from the ingredient set if they can possibly match allergens
for a, ilist in allergen_options.items():
    for i in ilist:
        if i in ingredients:
            ingredients.remove(i)

# Count the occurences of ingredients that cannot match an allergen
count = 0
for i in ingredients:
    for f in menu:
        for ilist in f['i']:
            if i in ilist:
                count += 1

print(f"Ingredients that can't match any allergen occur {count} times")

# CORRECT!