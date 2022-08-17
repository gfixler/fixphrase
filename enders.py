import re
import json
from itertools import combinations

path_to_main = "/home/gfixler/.config/plover/main.json"

with open(path_to_main) as f:
    main = json.loads(f.read())

enderKeys = "FRPBLGTSDZ"
hasEnder = lambda e: lambda x: any(map(lambda y: re.match("[^" + enderKeys + "]" + e + "$", y), x.split("/")))

found = []
for n in range(len(enderKeys) + 1):
    for combo in combinations(enderKeys, n):
        ender = ''.join(combo)
        matches = filter(hasEnder(ender), main)
        found.append((len(matches), ender))
        print len(matches), ender

print sorted(found, key=lambda ab: ab[0])

