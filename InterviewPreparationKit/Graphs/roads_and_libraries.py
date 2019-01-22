import math
import os
import random
import re
import sys
import collections

def roadsAndLibraries(n, c_lib, c_road, cities):
    if (c_lib < c_road):
        cost = n * c_lib
        return(cost)
    else:
        # Store the graph in a defaultdict that resembles an adjacency list
        roads = collections.defaultdict(list)
        for i in cities:
            roads[i[0]].append(i[1])
            roads[i[1]].append(i[0])
        print(roads)
        new_node = [True]*(n+1) #Mark all nodes not visited as True
        result = 0
        cache = collections.deque()
        for nd in range(1, n+1): # Iterate through all the nodes
            if (new_node[nd] == True): # If a node is not visited
                result += c_lib # Build a library at the node
                cache.append(nd) # Add that node to cache
                new_node[nd] == False # Mark the node as visited
                while cache: # While cache is not empty
                    for i in roads[cache.popleft()]: # Remove the first element from the left
                    # from the list of all nodes connected to node nd and iterate over all the
                    # other nodes
                        if new_node[i] == True: # If the node is not visited
                            cache.append(i) # Add the node to cache
                            new_node[i] = False # Mark the node as visited
                            result += c_road # Reconstruct the road to that node
                result -= c_road
        #result -= 1
        return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
