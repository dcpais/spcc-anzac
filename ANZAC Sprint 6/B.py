import math
import heapq

n, s = [int(x) for x in input().strip().split(" ")]

cities = []
for i in range(n):
    cities.append([int(x) for x in input().strip().split(" ")])

# Construct graph
edges = dict()
for i, (top, down) in enumerate(cities[:-1]):
    edges[i] = []
    for j, (top1, down1) in enumerate(cities[i+1:]):
        if top == top1 or down == down1:
            edges[i].append(j)


def doBFS(start, end, graph):

    frontier = [(start, 0)]
    visited = set()
    while frontier:
        current, step = frontier.pop(0)
        print(f"current: {current}")
        
        if current == end:
            return step
        
        for neighbour in graph[current]:
            if neighbour not in visited:
                frontier.append((neighbour, step + 1))
                visited.add(neighbour)

    return -1

q = int(input())
friendlies = []
for i in range(q):
    start, end = [int(x) - 1 for x in input().strip().split(' ')]
    friendlies.append(doBFS(start, end, edges))

for friend in friendlies:
    print(friend)




