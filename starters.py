import re
import json
from itertools import combinations

path_to_main = "/home/gfixler/.config/plover/main.json"

with open(path_to_main) as f:
    main = json.loads(f.read())

starterKeys = "STKPWHR"
hasStarter = lambda s: lambda x: any(map(lambda y: re.match("^" + s + "[^" + starterKeys + "]", y), x.split("/")))

found = []
for n in range(len(starterKeys) + 1):
    for combo in combinations(starterKeys, n):
        starter = ''.join(combo)
        matches = filter(hasStarter(starter), main)
        found.append((len(matches), starter))

print sorted(found, key=lambda ab: ab[0])

