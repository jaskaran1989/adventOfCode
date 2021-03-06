#!/usr/bin/python3.4

from collections import defaultdict
from itertools import permutations

places = set()
graph = defaultdict(dict)
for line in open("inputs/9.txt"):
    src, _, dst, _, dist = line.split()
    places.add(src)
    places.add(dst)
    graph[src][dst] = int(dist)
    graph[dst][src] = int(dist)

distances = []
for perm in permutations(places):
    distances.append(sum(map(lambda x, y: graph[x][y], perm[:-1], perm[1:])))

# Part I
print(min(distances))
# Part II
print(max(distances))
