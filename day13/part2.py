import sys
from pprint import pprint

with open(sys.path[0] + '/input.txt') as f:
    lines = f.read().splitlines()
busIds = sorted([{'id': int(id), 'dt': dt} for dt, id in enumerate(
    lines[1].strip().split(',')) if id != 'x'], key=lambda id: id['id'], reverse=True)

pprint(busIds, sort_dicts=False)


# dt ascends in the busIds dict
t = busIds[0]['id'] - busIds[0]['dt']
jump = busIds[0]['id']
matchedBusses = {}
while True:
    t += jump
    for id in busIds[1:]:
        if ((t + id['dt']) % id['id'] != 0): # no match
            break
        elif(id['id'] in matchedBusses and not matchedBusses[id['id']]['adjusted']):  # second match
            jump = t - matchedBusses[id['id']]['t']
            matchedBusses[id['id']]['adjusted'] = True
        elif(id['id'] not in matchedBusses):   # first match
            matchedBusses[id['id']]= {'t' : t, 'adjusted': False}

        # found them all!
        if(id == busIds[-1]):
            print(f"Valid timestamp = {t}")
            exit()
    if(t > 10**15):
        exit("this is reaaaaaaly large....")

# CORRECT!