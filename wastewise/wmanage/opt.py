from math import radians, cos, sin, asin, sqrt
from itertools import permutations

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth specified in radians.
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

coordinates = [[10.029341928222076, 10.029341928222076], [10.03288491086065, 10.03288491086065], [10.03308592998687, 10.03308592998687], [10.030646484446297, 10.030646484446297], [10.02925340170595, 10.02925340170595]]

distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distances[(i, j)] = haversine(coordinates[i][1], coordinates[i][0], coordinates[j][1], coordinates[j][0])

def total_distance(path):
    total = 0
    for i in range(len(path)-1):
        total += distances[(path[i], path[i+1])]
    return total

def find_shortest_paths(num_paths):
    all_paths = []
    for perm in permutations(range(len(coordinates))):
        path = list(perm) + [perm[0]]
        all_paths.append(path)

    all_paths.sort(key=total_distance)
    
    return all_paths[:num_paths]

shortest_paths = find_shortest_paths(4)

for i, path in enumerate(shortest_paths):
    print(f"Shortest Path {i+1}: {' -> '.join(str(p+1) for p in path)}")
    print(f"Total Distance: {total_distance(path)} km")
