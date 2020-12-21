import sys

menu = []
allergen_options = dict()

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        i, a = line.strip(")\n").split(' (contains ')
        alist = a. split(', ')
        ilist = i.split(' ')
        menu.append({'i': ilist, 'a': alist})

        # add ingredients to allergen options if only a single allergen is mentioned for this meal
        for a in alist:
            for i in ilist:
                allergen_options.setdefault(a, set()).add(i)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# cycle through all allergen options and keep only ingredients that occur everytime the allergen is present in the meal
for a, ilist in allergen_options.copy().items():
    for f in menu:
        if a in f['a']:
            allergen_options[a] = intersection(allergen_options[a], f['i'])

# cycle over allergen_options while removing every allergen matching a single ingredient
# remove translated ingredients from the list of options for other allergens
# repeat until every allergen is translated
translated = dict()
while len(allergen_options) != 0:
    for a,ilist in allergen_options.copy().items():
        if len(ilist) == 1:
            translated[a] = ilist[0]
            del allergen_options[a]
        else:
            # remove translated ingredients from the options dict
            for ti in translated.values():
                if ti in allergen_options[a]:
                    allergen_options[a].remove(ti)

print("\nTranslated (allergen: ingredient)")
[print(f"{a}: {translated[a]}") for a in sorted(translated)]
sortedList = [translated[a] for a in sorted(translated)]
print(f"\nSolution: {','.join(sortedList)}\n")