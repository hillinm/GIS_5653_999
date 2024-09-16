import pandas as pd

distance_from_lake = 0
increment = 500
max_distance = 5280

buffer_distances = []

while distance_from_lake < max_distance:
    distance_from_lake = distance_from_lake + increment
    buffer_distances.append(distance_from_lake)

print("Buffer distance (in feet)", buffer_distances)


